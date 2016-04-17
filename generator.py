# -*- coding: UTF-8 -*-
l = [x for x in xrange(16)]
print l
g = (x for x in xrange(16))
print g


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n += 1


fib(10)


def fib_g(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1


for x in fib_g(10):
    print x
