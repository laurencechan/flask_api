# coding:utf-8
__author__ = 'hcy'
from flask import Blueprint, request
from functools import wraps
import threading
from time import ctime, sleep


class getshu(object):
    pro = {}

    def set(self, apro={}):
        self.pro = apro

    def get(self):
        return self.pro

    def other_handle(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            # print "zhuangshiqi",request.get_data()
            # print "1:",args
            # print "2:",kwargs
            a = f()
            agc = self.get()
            # print "3:",agc
            print "I was listening to %s. %s" % (str(agc), ctime())
            # return f(*args,**kwargs)
            return a

        return wrapper


sss = getshu()


@sss.other_handle
def abc():
    p = {"abc": "111"}
    ab = sss.set(p)
    # print "4:hahahaha"

    return "dd"


@sss.other_handle
def bbb():
    p = {"bbb": "222"}
    ac = sss.set(p)
    # print "5:sdfsf"
    # print "I was listening to %s. %s" %("bbb",ctime())
    return "cc"


#####################################################################################
#
# @sss.other_handle
# def asbc():
#     p = {"dd":"bbbeee"}
#     ab = sss.set(p)
#     print "4543"
#     return  "dd"

#
# def other_handle(f):
#     @wraps(f)
#     def wrapper(*args,**kwargs):
#
#         return f(*args,**kwargs)
#     return wrapper
#
#
# @other_handle
# def bbbb():
#     def b1():
#         p = {"dd":"bbbeee"}
#         return  p
#     print "4:hshaha"
#     return  "dd"
#
#

threads = []


def addthresad():
    threads.append(threading.Thread(target=bbb))
    for i in range(0, 10):
        threads.append(threading.Thread(target=abc))
    for i in range(0, 10):
        threads.append(threading.Thread(target=bbb))
    for i in range(0, 10):
        threads.append(threading.Thread(target=abc))


if __name__ == "__main__":
    pass

    # addthresad()
    # for t in threads:
    #     t.setDaemon(True)
    #     t.start()
    #     # abc()
        # asbc()
        # bbbb()
        # bbb()
