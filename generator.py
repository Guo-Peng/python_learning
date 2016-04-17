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


def consumer():
    n = 0
    while True:
        n = yield n
        n -= 1
        print 'consume 1 ,left %d' % n


def producer(c):
    n = 0
    c.next()
    while n < 10:
        n += 2
        print 'produce 2 ,left %d' % n
        n = c.send(n)
        print 'confirm %d' % n
    c.close()


c = consumer()
producer(c)
