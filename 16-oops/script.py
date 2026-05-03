class Student:
    pass 

s1 = Student()
s2 = Student()

print("Student 1:",s1)
print("Student 2:",s2)

print(s1 is s2)
print(s1 == s2)

if s1 is s2:
    print("Both are equal")

if s1 == s2:
    print("Both are equal")

## implement eauality

class Student:

    def  __init__(self, name,age): # self means the current object which is equal to this keyword in some other programming
        self.name = name
        self.age = age

    def __eq__(self,other): # kind of a operator overloading in c++
        return self.name==other.name and self.age==other.age

s1 = Student("Jiten",43)
s2 = Student("Jiten",43)
s3 = Student("Jiten",43)


# print(s1.__eq__(s2))

if s1==s2==s3:
    print("objects are equal")
else:
    print("not equal")

