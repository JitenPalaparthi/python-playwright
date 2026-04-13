import sys

x = 10
# python creates an integer object
# 10 is an integer object and stored in heap memory
# name binding --> the name x is created in current namespace and x is bound to the object 10

print(type(x))
print("init id of x",id(x))
print(globals())

y = x
print(id(y))

x = 20
print("mutated id of x",id(x))

z = 1231.123
print("z id:",id(z))

z = z+1
print("z id:",id(z))

# reference counting 

x = 9999
y = x 
z = x

print(id(x),id(y),id(z))

print("Ref Count:",sys.getrefcount(9999)/2)


# def demo():
#     x1 = 100
#     print(id(x1))
#     print("Locals","\n")
#     print(locals())

# demo()

#4331286784
#4331287104

# mutable and immutable objects