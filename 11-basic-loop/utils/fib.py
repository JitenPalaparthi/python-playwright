# fib 
# 0 1 1 2 3 5 8 13 21 34 


def fib1(n):
    a,b = 0,1 
    for _ in range(n):
        print(a,end=" ")
        a,b = b,a + b

def fib2(n):
     a,b = 0,1
     count = 0 
     while count<n:
         print(a,end=" ")
         a,b = b,a + b
         count+=1
def fib3(n):
     a,b = 0,1
     for i in range(0,n,2):
         print(a,end=" ")
         a,b = b,a + b

def fib4(n):
     a,b = 0,1 
     count=0
     while True:
         print(a,end=" ")
         a,b = b,a + b
         count+=1
         if count==n:
             break



