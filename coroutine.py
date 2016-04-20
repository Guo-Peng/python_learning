# -*- coding: UTF-8 -*-
# http://xlambda.com/gevent-tutorial/
import gevent.monkey

gevent.monkey.patch_socket()
import gevent
import requests
import time
from multiprocessing.dummy import Pool as ThreadPool

# # todo
# # change crawler to coroutine
# def consumer():
#     n = 0
#     while True:
#         n = yield n
#         n -= 1
#         print 'consume 1 ,left %d' % n
#
#
# def producer(c):
#     n = 0
#     # 使用next开始generator后才能进行send
#     c.next()  # 等于 s.send(None)
#     while n < 10:
#         n += 2
#         print 'produce 2 ,left %d' % n
#         n = c.send(n)
#         print 'confirm %d' % n
#     c.close()
#
#
# c = consumer()
# producer(c)

# # simple usage
# def f1():
#     print 'f1 running ...'
#     gevent.sleep(0)
#     print 'switch to f1 ...'
#
#
# def f2():
#     print 'f2 running ...'
#     gevent.sleep(0)
#     print 'switch to f2 ...'
# gevent.joinall([
#     gevent.spawn(f1),
#     gevent.spawn(f2)
# ])
#
#
# start = time.time()
# during = lambda: time.time() - start
#
#
# def fetch(n):
#     s = time.time()
#     requests.get('http://www.baidu.com')
#     print 'process %d : %1.2fs -- %1.2fs' % (n, time.time() - s, during())
#
#
# def synchronous():
#     for x in xrange(10):
#         fetch(x)
#
#
# def thread():
#     pool = ThreadPool(10)
#     for x in xrange(100):
#         pool.apply_async(fetch, args=(x,))
#     pool.close()
#     pool.join()
#
#
# def asynchronous():
#     gevent.joinall([gevent.spawn(fetch, x) for x in xrange(100)])
#
#
# start = time.time()
# print 'synchronous'
# synchronous()
# print 'during %1.2f ' % during()
# start = time.time()
# print 'thread'
# thread()
# print 'during %1.2f ' % during()
# start = time.time()
# print 'asynchronous'
# asynchronous()
# print 'during %1.2f ' % during()

from gevent.pool import Pool

start = time.time()
during = lambda: time.time() - start


def fetch(n):
    s = time.time()
    requests.get('http://www.baidu.com')
    print 'process %d : %1.2fs -- %s' % (n, time.time() - s, during())


pool = Pool(5)
pool.map(fetch, xrange(10))
# 是否需要等待结束
# pool.join()
print 'test'
print during()
