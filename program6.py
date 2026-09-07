class Animal:

    def eat(self):
        print("Animal is eating.")

    def sleep(self):
        print("Animal is sleeping.")
class Dog(Animal):

    def bark(self):
        print("Dog is barking.")
d1 = Dog()
d1.eat()
d1.sleep()
d1.bark()
