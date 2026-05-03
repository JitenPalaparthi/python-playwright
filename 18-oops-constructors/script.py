class Student:

    def __init__(self,name="unknown",age=0):
        self.name=name
        self.age=age

s1 = Student()

s2 = Student("Jiten")

s3 = Student(age=43)

print(s1.name,s1.age)
print(s2.name,s2.age)
print(s3.name,s3.age)


class Student:

   # def __init__(self,name="unknown",age): # the default arguments should come after non default arguments
     def __init__(self,age,name="unknown"): # the default arguments should come after non default arguments
        self.name=name
        self.age=age

s1 = Student(43)

s2 = Student(43,"Jiten")

s3 = Student(name="Jiten",age=43)

print(s1.name,s1.age)
print(s2.name,s2.age)
print(s3.name,s3.age)

# create a list 

class MyList:
    def __init__(self, items=None):
        if items is None:
            items=[]
        self.items= items
    
    def sumOf(self):
        sum = 0 
        for i in self.items:
            sum+=i 
        return sum
    
    def max(self):
        if len(self.items)<=0:
            return 0

        max = self.items[0]
        for i in self.items:
            if i>max:
                max = i 
        return max

    def what():
        return "class:MyList"
        


mylist = MyList()

print(mylist.items)
print("Sum:",mylist.sumOf())
print("Max:",mylist.max())

print(MyList.what())

mylist = MyList([1,2,3,4,5])
print(mylist.items)
print("Sum:",mylist.sumOf())

mylist=MyList([23,3,54,2,45,6,7,24,645,3,43,65,32,24646,33334])
print("Sum:",mylist.sumOf())
print("Max:",mylist.max())





