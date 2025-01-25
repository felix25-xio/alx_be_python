import math

class Shape:
    def area(self):
        raise NotImplementedError("The area method must be overridden by the subclass.")


class Rectangle(Shape):
    def __init__(self, length, width):
        #nitialize a Rectangle instance.
        self.length = length
        self.width = width

    def area(self):
        #alculate the area of the rectangle.
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        #itialize a Circle instance.
        self.radius = radius

    def area(self):
      #calculate thearea of the circle.
        return math.pi * (self.radius ** 2)

from polymorphism_demo import Shape, Rectangle, Circle

def main():
    # List of shapes demonstrating polymorphism
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        # Polymorphic behavior: invoking the overridden area method
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()

