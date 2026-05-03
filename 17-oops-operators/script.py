
class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    
    def __add__(self,other):
        if not isinstance(other,Point):
            return NotImplemented
        else:
            return Point(self.x+other.x,self.y+other.y)
        
def main():
    p1 = Point(23.23,20)
    p2 = Point(23.23,20)
    if p1==p2:
        print("p1 and p2 are same")
    else:
        print("p1 and p2 are different")

    p3 = p1 + p2

    print("x:",p3.x,"y:",p3.y)

    try:
        p4 = p1+100
    except TypeError:
        print("some type issue")

if __name__=="__main__":
    main()
    # print(globals())
    # print(locals())

   

# == __eq__
# + __add__
# - __sub__
# * __mul__
# /__truediv__
# += __iadd__
