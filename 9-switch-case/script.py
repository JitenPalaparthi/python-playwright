
def sun():
    return "Sunday"

def mon():
    return "Monday"

def tue():
    return "Tuesday"

def wed():
    return "Wednesday"

def thu():
    return "Thursday"

def fri():
    return "Friday"

def sat():
    return "Saturday"

def default():
    return "noday"

def somef():
    return 10  * 10

switch = {
    1:sun,
    2:mon,
    3:tue,
    4:wed,
    5:thu,
    6:fri,
    7:sat,
    #8: somef
}

day = 4

result = switch.get(day,default)
print(result())

f = sat # what does it mean?

print(f())

f = sat  # storing a func in an another variable
print(type(f))

print(id(f))

f = sat() # calling a function
print(type(f))