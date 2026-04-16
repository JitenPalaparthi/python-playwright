
age = 14

gender = 'G' #M means male and F means female

# age >=18 and True and (True or False) and (10+20)>20

# True and True and True and True

# if age >=18 and True and (True or False):
# print(age >=18 and True and (True or False))

if age >=18:
    if gender=='M' or gender=='m':
        print("Adult male")
    elif gender=='F' or gender=='f':
        print("Adult female")
    else:
        print("unknown gender")
else:
     if gender=='M' or gender=='m':
        print("Minor male")
     elif gender=='F' or gender=='f':
        print("Minor female")
     else:
        print("Minor unknown gender")
# write in another way

if age>=18 and (gender=='M' or gender=='m'):
      print("Adult male")
elif age>=18 and (gender=='F' or gender=='f'):
     print("Adult female")
elif age<18 and (gender=='M' or gender=='m'):
     print("Minor male")
elif age<18 and (gender=='F' or gender=='f'):
    print("Minor female")
else:
    if age>=18:
        print("Adult,unknown gender")
    else:
        print("Minor,unknown gender")

  






