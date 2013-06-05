#!/usr/bin/env python
#
# Splits SQL statements out of a file

import re 

#
# class that implements a sql splitting generator and iterator
# input is an open file like object
# instead of using a very complex (and difficult to debug) regular expression we use
# a simple regular expression that finds the interesting tokens such as quotes and comments
# and then feed those to a Finite State Machine to interpret the syntax
# 

class SQLStatements :

#
# initialize the class, compiles the regex and reads the first block of data
#
    def __init__(self, input, bufsize=10000) :
        self.bufsize = bufsize
        rex = r';|\\*"|\n|#|/\*|\*/|`' + r"|\\*'|--\s"
        self.starttags = {'"' : '"', "'": "'", '/*': '*/', '`' :'`'}
        self.state = 'normal'
        self.pattern = re.compile(rex)
        self.endtag = ''
        self.start = 0
        self.fh = input
        self.data = self.fh.read(self.bufsize)
        self.next = self.statements().next

#
# return our statements generator as the class iterator
#
    def __iter__(self) :
        return self
    
    def next(self) :
        return self.next()
    

#
# a statement generator
# read a statement from the data
# and yield it to our caller
#    
    def statements(self):
        while self.data :
            self.state = 'normal'
            self.start = 0
            r = self.pattern.finditer(self.data)
            for m in r :
                res = (self.fsm(m)).strip()
                if res : yield res
            remains = self.data[self.start:]
            self.data = ''
            fr = self.fh.read(self.bufsize)
            if fr :
                self.data = remains + fr
        
        remains = remains.strip()         
        if remains: yield(remains)
                     
        raise StopIteration

#
# a simple finite state machine that interprets the tokens found by the regex
# the input is a regex token
# it returns a non empty result when a complete statement is found
#
    def fsm(self, m) :
        end = m.end(0)
        token = self.data[m.start(0):end]
        near = self.data[m.end(0):10+end]
        if self.state == 'normal':
            if token == ';':
                res = self.data[self.start:end]
                self.start = end
                return res
            elif token in self.starttags :
                self.endtag = self.starttags[token]
                self.state = 'paired'
            elif token == '#' or token == '-- ' :
                self.state = 'comment'
            elif token == '/*' :
                self.state = 'mlcomment'     
        elif self.state == 'paired' :
            if token == self.endtag :
                self.state = 'normal'
        elif self.state == 'comment' :
            if token == "\n" :
                self.state = 'normal'
                res = self.data[self.start:end]
                self.start = end
                return res
        elif self.state == 'mlcomment' :
            if token == '*/' :
                self.state = 'normal'
        return ''                 
