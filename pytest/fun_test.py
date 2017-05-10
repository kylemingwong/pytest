from math import sqrt
def add(x,y,f):
    return  f(x) + f(y)

print add(3,12,abs)


def d_fun(x,*fs):
    s= [fun(x) for fun in fs]
    return s

print d_fun(9,abs,sqrt)



def s_fun(vs=[],*fs):
    return [f(s) for s in vs for f in fs]

print s_fun([0,4,9,16],abs,sqrt)

def f(x):
    return x * x

print map(f,[2,3,4,5,6,7,8,9])



def f_redu(x,y):
    return x * 10 + y

print reduce(f_redu,[1,3,5,7,9])


def str2num(str):
    a = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return a[str]

print map(str2num,'23455')

print reduce(lambda x,y : x*10+y,map(str2num,'23567686'))

##########################################


from string import lower
from string import  upper
def extran(str):
    return upper(str[0]) + lower(str[1:])

def nomal(strs):
    return map(extran,strs)

print nomal(['WERE','you','pleAse'])

def prod(nums):
 #   i = 1
    return reduce(lambda x,y=1:x*y,nums)

print prod([2,2,3,4])


def is_not_sushu(x):
    flag = True
    if x == 1:
        return False
    elif x == 2:
        return True
    elif x > 2:
        for i in range(2,int(sqrt(x)+1)):
            if x % i == 0:
                flag = False
                break
    return flag


def filter_sushu( x = [] ):
    return filter(is_not_sushu,x)

import  datetime
start_time = datetime.datetime.now()
print filter_sushu(range(1,101))
end_time = datetime.datetime.now()
print end_time - start_time

##############################################################

def count():
    fs = []
    for i in range(1,4):
        def f(j = i):
            return j * j
        fs.append(f)
    return fs

f_ls = count()

print f_ls[0]()
print f_ls[1]()
print f_ls[2]()

####################################################################

def log(func):
    def zsq():
        print 'call %s()' %func.__name__
        return func()
    return zsq

@log
def now():
    print '2017-03-01'

now()


def makebold(fun):
    def wrapped():
        return "<b>" + fun() + "</b>"
    return wrapped


def makeitalic(fun):
    def wrapped():
        return "<i>" + fun() + "</i>"
    return wrapped


@makebold
@makeitalic
def hello():
    return "hello world!"

print hello()





