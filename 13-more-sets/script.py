
a = {1,2,3}
b = {3,4,5}

# union 

c = a | b 

print(c)

# intersection

c = a & b

print(c)

# set difference , take all elements from a those are not preset in b

c = a-b 
print(c)

# symmetric difference 

c = a ^ b 

print(c)

lst = [1,2,3,3,4,5,1,2]

s = set(lst)

print(s)


s = {True,10,10.10,"Hello World",'A',(1,False,0)}

print(s)


lst=[1,2,3]
s =set(lst)

# iterate thru a set 

s = {10,11,1,2,3,4,5,6,7,8,9}

sum = 0
for item in s:
    sum= sum+item
    print(item)

print("sum:",sum)

# print only even elements from a set 

for item in s:
    if item % 2==0:
        print(item)

# iterator 

print("iter")
it = iter(s)

print(next(it))
print(next(it))
print(next(it))

s = {1,2,3}
it = iter(s)
print(next(it))
print(next(it))
print(next(it))

s = {10,11,1,2,3,4,5,6,7,8,9}

it = iter(s)

while True:
    x = next(it,None)
    if x is None:
        print("Found None so breaking the loop")
        break 
    print(x)

if 10 in s:
    print("yes")






# O(n)