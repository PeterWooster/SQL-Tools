#!/usr/bin/env python

# test the sql statements splitter

from SQLStatements import SQLStatements

# use an open file and a very small buffer to give it a thorough test
fh = file("testStatements.sql")
statements = SQLStatements(fh, 20) 
for statement in statements :
    print ">>>>%s<<<<" % statement
fh.close