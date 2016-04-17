# -*- coding: UTF-8 -*-
import gevent


# todo
# change crawler to coroutine
def consumer():
    n = 0
    while True:
        n = yield n
        n -= 1
        print 'consume 1 ,left %d' % n


def producer(c):
    n = 0
    # 使用next开始generator后才能进行send
    c.next()  # 等于 s.send(None)
    while n < 10:
        n += 2
        print 'produce 2 ,left %d' % n
        n = c.send(n)
        print 'confirm %d' % n
    c.close()


c = consumer()
producer(c)
