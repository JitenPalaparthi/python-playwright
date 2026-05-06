# threading
# multiprocessing
# async await async programming

# multiplexing
# scheduler 
# context switch

import threading
import time 

def worker(name):
    for i in range(10):
        print(name,"--> Working...",i)
        time.sleep(1/10)

t1 = threading.Thread(target=worker,args=("thread-1",))
t2 = threading.Thread(target=worker,args=("thread-2",))

t1.start()
t2.start()

t1.join() # join the threads so that main thread can wait until this thread can complete execution and then join
t2.join() # join the threads so that main thread can wait until this thread can complete execution and then join


# main thread is blocked until t1 and t2 are completed
print("Main thread continues...")

# GIL --> Global Interpretter Lock, Pytho bytecode can run only one thread at a time , bcz of GIL