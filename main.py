class Dog:
    def bark(self):
        print("Woof!")

class Math:
    def add(self, a, b):
        print(a + b)

class Person:
    def greet(self):
        print("Hello")

class Lamp:
    def turn_on(self):
        print("Lamp is on")

class Computer:
    def info(self):
        print("Computer is working")


dog = Dog()
math = Math()
person = Person()
lamp = Lamp()
computer = Computer()

dog.bark()
math.add(3, 4)
person.greet()
lamp.turn_on()
computer.info()
