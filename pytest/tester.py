#coding=UTF-8
class tester:
    def __init__(self,start):
        self.state = start

    def nested(self,label):
        print(label,self.state)
        self.state += 1

F = tester(0)

F.nested('spam')
F.nested('ham')

def f(a, *pargs, **kargs):
    print(a,pargs,kargs)

f(1,2,3,x=5, y=6)

"""
解包参数
"""

def func(a,b,c,d):
    print(a,b,c,d)

arg = (1,2)
arg += (3,4)

func(*arg)

args = {'a':1,'b':2,'c':3,'d':4}

func(**args)


def func1(*args):
    print args

action1,arg1 = func1,(1,)

action2,arg2 = func1,(1,2,3)

action1(*arg1)

action2(*arg2)






