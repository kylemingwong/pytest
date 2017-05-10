class Animal(object):
    def run(self):
        print 'Animal is running!'



class Dog(Animal):
    def run(self):
        print 'Dog is running!'
    def eat(self):
        print 'Dog is eating'

class Cat(Animal):
    def run(self):
        print 'Cat is running!'

    def eat(self):
        print 'Cat is eating fish!'

dog = Dog()

cat = Cat()

a = list()

dog.run()

cat.run()

print isinstance(a,list)

print isinstance(dog,Animal)

print isinstance(cat,Animal)

