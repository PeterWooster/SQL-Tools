#!/usr/bin/env python

#
# a simple iterator example that uses a generator 
#

class myIterator:
    def __init__(self, n):
        self.last = n
        self.next = self.myGenerator().next  # Use the generator `.next`

    def __iter__(self):
        return self

    def myGenerator(self):
        prev = 0
        fib = 1
        while fib < self.last:
            res = fib
            yield res
            fib += prev
            prev = res
                                            
mi = myIterator(1000)

print mi.next()
print mi.next()
print mi.next()
print mi.next()
for i in mi: print "fib=%d" % i            