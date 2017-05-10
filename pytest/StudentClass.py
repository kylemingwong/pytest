class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')

        if value <0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')

        self._score = value



s = Student()

s.score = 60

print s.score




class Student2(object):

    __slots__ = ('name', 'age')

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' %self.name


print Student2('Michael')