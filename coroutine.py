# -*- coding: UTF-8 -*-
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