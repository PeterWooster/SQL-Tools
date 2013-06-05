#!/usr/bin/env python

import sys, codecs, MySQLdb

def showhex(s) : 
    r = ''
    for c in s :
    	r = "%s %02X" %(r, ord(c))
    print r

f = file('utftest.txt')
dat = f.read()
con = MySQLdb.connect(host='localhost', user='root',passwd='8turnip',db='benchmark')
cur = con.cursor()
    
con.set_character_set('utf8')
sql = "INSERT INTO utftest VALUES ('" + dat + "')"
cur.execute(sql)
con.commit()
cur.execute ("select * from utftest")
a = (cur.fetchall())[0][0]
showhex(a)
print a
con.close()
f.close
