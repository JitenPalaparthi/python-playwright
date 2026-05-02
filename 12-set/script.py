# similar to mathematical set 

# no duplicates 

# order is not guaranteed 

# fast operations, set uses hashing

list = [10,10,22,23,24,23,24]

print(list)

s1 = {1,2,3,4,1,2,3,4}

print(s1)

s2 = set([1,2,3,4,1,2,3,4])

print(s2)

s3 = {} # this would never create a empty set,this creates a dictionary

print(type(s3))

s3= set() # creats an empty set 

print(type(s3))

s3 = {3,1,2,4,5,6,8,7,9}

print(s3)

s3.add(100)
try: 
    s2.remove(101)
except KeyError: 
    print("to remove, key is not available")

print(s3)

s3.discard(110) # if element is not available , no ops 
print(s3)



