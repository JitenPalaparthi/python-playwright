x = "100"

print(type(x),id(x))

y = x # ref copy, shallow copy

print(type(y),id(y))

y = int(x) # type casting, coversion, the date is stored as a different object and that object ref is assigned to y

print(type(y),id(y))

x = "10.123"
y = float(x)

print(type(y),id(y))


x = 42323
y = str(x)

print(type(y),id(y))

x = "Flase"
y = bool(x)

print(type(y),id(y),y)

# bool cast is tricky, it only checks whether the value is there or not.
# is it empty , zero or None --> Flase
# If there is some value , irrespective of data it is considered as True


x = "false"

y = bool(x) # y cannot be false reason is there is a value .. it is not empty, 0 nor None

print(y)

y = x.upper() == "TRUE" ## using == comparision operator

print(y)

z = 100 

k = z+10 +(z *2 )+100 > 200

print(k)



