class Fib(object):
    __slots__ = ('num','a','b')
    def __init__(self,num):
        self.num = num
        self.a, self.b = 0,1

    def __iter__(self):
        return self

    def next(self):
        self.a, self.b = self.b, self.a + self.b

        self.num = self.num -1

        if self.num < 0:
            raise  StopIteration()
        return self.a



for n in Fib(100):
    print n

