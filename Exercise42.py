# Title: Exercise 42
# Author: Benjamin Lemery
# Date: 11/20
# This program demonstrates the use of classes and class methods

# Animal is an object
class Animal(object):
    pass

# Dog is an object
class Dog(Animal):
    def __init__(self,name):
        self.name = name
# Cat has a class relationship to Animal
class Cat(Animal):
    def __init__(self,name):
        self.name = name
# Person is an object
class Person(object):
    def __init__(self,name):
        self.name = name
# Employee has a class relationship to Person
class Employee(Person):
    def __init__(self,name,salary):
        super(Employee,self).__init__(name)
        self.salary = salary
# Fish is an object
class Fish(object):
    pass
# Salmon has a class relationship to Fish
class Salmon(Fish):
    pass
# Halibut has a class relationship to Fish
class Halibut(Fish):
    pass

rover = Dog("Rover")
print(rover)

satan = Cat("Satan")

mary = Person("Mary")
mary.pet = satan

frank = Employee("Frank",120000)
frank.pet = rover

flipper = Fish()
crouse = Salmon()

harry = Halibut()
