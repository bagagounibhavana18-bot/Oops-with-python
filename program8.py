class Animal:

    def sound(self):
        print("Animal makes a sound.")

class Dog(Animal):

    def sound(self):
        print("Dog barks.")

d1 = Dog()
d1.sound()
