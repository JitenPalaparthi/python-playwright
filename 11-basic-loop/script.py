# fib 
# 0 1 1 2 3 5 8 13 21 34 

# import utils.fib.fib1

# import utils.fib as f ,utils.even as e

# from utils import fib1,fib2,fib3,fib4,even1

# what is the use of __all__ in init.py file

from utils import *
import utils;

if __name__=="__main__": # to avoid auto execition

    print(utils.__all__)
    fib1(10)

    print()
    fib2(10)

    print()
    fib3(10)

    print()
    fib4(10)

    print()
    even1(20)


