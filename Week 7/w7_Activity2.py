### Factory Method Pattern
# The Factory Method Pattern is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

from abc import ABC, abstractmethod
 
class Factory(ABC):
   
    @abstractmethod
    def create_product(self, kind=None):
        pass
 
class AnimalFactory(Factory):
    def __init__(self):
        pass
 
    def create_product(self, kind=None):
        if kind == "dog":
            animal = Dog()
        elif kind == "cat":
            animal = Cat()
 
        return animal
 
class DogFactory(Factory):
   
    def create_product(self, kind=None):
        return Dog()
 
class CatFactory(Factory):
   
    def create_product(self, kind=None):
        return
 
class Animals(ABC):
 
    @abstractmethod
    def run(self):
        pass
 
class Dog(Animals):
 
    def run(self):
        print(f"I'm a Dog, I can run!!")
        return
 
 
class Cat(Animals):
    def __init__(self):
        pass
 
    def run(self):
        print(f"I'm a Cat, I can run!!")
 
 
 
 
 
# client
factory = DogFactory()
dog = Dog()
dog = factory.create_product()
dog.run()