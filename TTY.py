from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class triangle(shape):
    def area(self):
        print("area of triangle=1/2*b*h")
r=triangle()
r.area()
class square(shape):
    def area(self):
        print("area of square=5*5")
r=square()
r.area()
