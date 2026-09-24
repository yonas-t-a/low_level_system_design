from abc import ABC, abstractmethod


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



if __name__ == "__main__":
    mySqr = Square(4,5)
    print(mySqr.area())
    print(mySqr.perimeter())