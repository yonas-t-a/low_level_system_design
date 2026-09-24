from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass 

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, width, hight):
        super().__init__()
        self.width = width 
        self.hight = hight
    
    def area(self):
        return self.width * self.hight

    def perimeter(self):
        return 2*(self.width + self.hight)

class Circle(Shape):
    def __init__(self,rad):
        self.rad =  rad
    
    def area(self):
        return  math.pi * self.rad ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.rad
        

if __name__ == "__main__":
    mySqr = Square(4,5)
    print(mySqr.area())
    print(mySqr.perimeter())
    
    myCir = Circle(5)
    print(myCir.area())
    print(myCir.perimeter())