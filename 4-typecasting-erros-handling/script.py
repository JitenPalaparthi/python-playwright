
value = "Hello Python Learners!"

try:
    num =int(value)
    print(num)
except ValueError:
     print("there seems to be invalid input to cast")

##  Multiple try except blocks

try:
    num =int(value)
except ValueError:
    try:
        num= float(value)
    except:
        print("the value cannot be converted to int or float")
        num = None
print(num)


