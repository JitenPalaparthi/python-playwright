from abc import ABC

class Shape(ABC):
   
    @classmethod
    def area():
        pass

    @classmethod
    def perimeter():
        pass

    def info(self):
        print("Some shape to be implemented")

class Rect(Shape):

    def __init__(self,l,b):
        self.l=l
        self.b=b
    
    def area(self):
        return self.l * self.b

    def perimeter(self):
        return 2 *(self.l+self.b)
    

s1 = Rect(10.1,12.3)

print("Area of Rect:",s1.area())

print("Perimeter of Rect:",s1.perimeter())


class Circle(Shape):
    pass 

c1= Circle()

# the below gives type error becase @classmethod has been given and removed self 
# c1.area()
# c1.perimeter()
c1.info()