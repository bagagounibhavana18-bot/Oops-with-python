class Student:

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Creating an object
student1 = Student("Bhavana", 19)

# Calling the method
student1.display()
