class MyClass(object):
    gender = 'Male'

    def __init__(self,who):
        self.name = who

    def sayHi(self):
        print 'Hello, '+self.name


me = MyClass('Tom')

me.sayHi()






