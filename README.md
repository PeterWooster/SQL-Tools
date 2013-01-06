SQL-Tools
=========

A collection of Python script to help with SQL tasks

SQLStatements
-----------

SQLStatements reads the content of a file as multiple SQL statements.  It is a class that provides an iterator over the statements. Statements are delimited by unquoted ; anywhere in the text and newline at the end of single line comments starting with # and -- .  Single, double and back quotes and multiline comments can span over semicolons. 

The SQL syntax is based on MySQL, but will work with most ANSI SQL.

This script provides a simple example of the use of the iterator and generator features of Python.  The statements function is a generator using yield and the class returns it as the result of __iter__ to behave as an iterator.

The strategy for splitting the text is to find the interesting delimiters using a simple regular expression and then parse the text using a simple finite state machine.  This is much easier than trying to find the statement ends using regular expressions.  I'm not certain that is even possible given the complexity of the rules.

The testStatements.py and testStatements.sql files provide a simple test of the SQLStatements class.

SQLRunner
---------

SQLRunner reads a file of SQL statements and executes them one at a time.  This can be used to perform bulk import.    It uses the SQLStatements to extract statements from the file.
