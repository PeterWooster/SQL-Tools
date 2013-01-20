#!/usr/bin/env python
#
# SQLRunner.py
# A simple script to run a script of mysql commands
# it turns off foreign key checks
# and commits every so often, by default every 100 rows
#
# syntax is:
# SQLRunner Host Database User Password File [Rows per commit]
# Each command must be on a single line in the file 
#
 
import MySQLdb, sys, os, SQLStatements, codecs

if len(sys.argv) > 5 :
    host = sys.argv[1] 
    db = sys.argv[2]
    user = sys.argv[3]
    pw = sys.argv[4]
    fname = sys.argv[5]
    if len(sys.argv) > 6 :
        rows = int(sys.argv[6])
    else:
        rows = 100
    if len(sys.argv) > 7 :
        charset = sys.argv[7]
    else :
        charset = 'utf8'
        
    print "Host=%s, Database=%s, User=%s, File=%s, Rows=%d Charset=%s" % (host, db,user,fname, rows, charset)
else:
    print "not enough arguments"
    print "SQLRunner Host Database User Password File [Rows per commit] [charset]"
    sys.exit()

fn = codecs.open(fname,'r',charset)
statements = SQLStatements.SQLStatements(fn)
con = None
hasTransaction = 0
commands = 0
lineno = 1

try:
    con = MySQLdb.connect(host=host, user=user,passwd=pw,db=db)
    cur = con.cursor()
#     con.set_character_set(charset)
    print "disabling foreign key checks"
    cur.execute("set foreign_key_checks=0;")

    cur.execute("use %s"%db)
    
    print "processing statements"
    for line in statements:
        if not line: continue
        if hasTransaction and commands >= rows:
            con.commit
            hasTransaction = 0
            print "Commit: statement # %d" % (lineno-1)
            commands = 0
        print "%d#%s" % (lineno,line)
        cur.execute(line)
        hasTransaction = 1
        lineno = lineno +1
        commands = commands + 1
		
    if hasTransaction:
        con.commit()
        hasTransaction = 0
        print "Commit: statement # %d" % (lineno-1)
    print "Done" 
    
except MySQLdb.Error, e:
    if hasTransaction:
        con.rollback()
        hasTransaction = 0
    print "Error %d: %s" % (e.args[0], e.args[1])
    con = None
	
finally:
    if con:
        cur = con.cursor()
        cur.execute ("set foreign_key_checks=1;")
        print("foreign key checks enabled")
        con.close()
    if fn :
        fn.close
