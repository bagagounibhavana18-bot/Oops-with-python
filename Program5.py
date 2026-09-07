class Rectangle:

    # Constructor
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to calculate area
    def calculate_area(self):
        return self.length * self.width

    # Method to calculate perimeter
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


# Creating an object
rectangle1 = Rectangle(10, 5)

# Calling methods
print("Area of Rectangle:", rectangle1.calculate_area())
print("Perimeter of Rectangle:", rectangle1.calculate_perimeter())
