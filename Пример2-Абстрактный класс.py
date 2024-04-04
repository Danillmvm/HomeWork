from abc import ABC, abstractmethod

class shape(ABC):
    def __init__(self,perimeter):
        self.perimeter = perimeter
 

    @abstractmethod
    def get_shape(self):
        pass

class cube(shape):
    def get_shape(self):
        print(f'"{self.perimeter/4}"cm - одна сторона куба')

class circle(shape):
    def get_shape(self):
        print(f'"{self.perimeter/(2*3.14)}"cm - радиус круга')

class Poetry(shape):
    pass

square_cube = cube(14)
circle_shape = circle(30)
square_cube.get_shape()
circle_shape.get_shape()