
day = 4

match day:
    case 1:
        print("Sunday")
    case 2:
         print("Monday")
    case 3:
         print("Tuesday")
    case 4:
         print("Wednesday")
    case 5:
         print("Thursday")
    case 6:
         print("Friday")
    case 7:
         print("Saturday")
    case _:  # default: _ is called as blank identifier
          print("no day")

data = ("mul",10,20) # (str,int,int)

match data:
     case ("add",a,b):
          print("add:",a+b)
     case ("sub",a,b):
          print("sub:",a-b)
     case ("mul",a,b):
          print("mul:",a*b)
     case ("div",a,b):
          print("div:",a/b)
     case _:
        print("no operation")

char = 'E'
print(type(char))

match char: # match with or
     case 'a' | 'e' | 'i' | 'o' | 'u':
          print(char,"is lower case vovel")
     case 'A' | 'E' | 'I' | 'O' | 'U':
        print(char,"is Upper case vovel")
     case _:
          print(char,"is either a upper|lowe case consonent or even a special char")

# captured pattern

x = ("cube",100)

match x:
     case ("sq",value):
          print("sq of value:",value * value)
     case ("cube",value):
          print("cube of a number:",value * value * value)
     case _:
          print(value,"invalid operation")

# list 

lst = [10,20,30,40]

match lst:
     case [10,20,30]:
          print(lst,"exact match")
     case [10,*rest]: # * is used for the sequence unpacking
          print(10,"first match,",rest)

a,b,c,_,*rest = [1,2,3,4,5,6,7,8,9,10] # a=1,b=2,c=3,ignore 4, and rest of the sequence is into *rest

print(a)
print(b)
print(c)
print(rest)

a,b = 10,20 

a,b,*all = 10,20,30,40,50

a,b,*_= 10,20,30,40, # ignore all rest of the value