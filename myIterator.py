#!/usr/bin/env python

#
# a simple iterator example that uses a generator 
#

class myIterator :
    
    def __init__(self, n) :
    	self.last = n
    	self.myGen = self.myGenerator() 
    	
    def __iter__(self) :
        return self.myGenerator()
    
    def next(self) :
        return self.myGen.next()
    
    def myGenerator(self) :
        prev = 0
        fib = 1
        while fib < self.last :
            res = fib
            yield res
            fib = fib + prev
            prev = res
            
        raise StopIteration
