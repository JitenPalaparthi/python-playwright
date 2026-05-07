import threading
import time

counter = 0 
lock = threading.Lock() # can be similar to mutex

def increment():
    global counter

    for _ in range(100000):
       
       # with lock:
        lock.acquire()
        temp = counter
        time.sleep(0.000005)
        counter= temp+1
        lock.release()

def decrement():
    global counter
    for _ in range(100000):
        with lock:
            temp = counter
            time.sleep(0.000008)
            counter= temp-1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=decrement)

t1.start()
t2.start()


t1.join()
t2.join()

print("Final Counter:",counter)
