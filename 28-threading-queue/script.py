import threading
import time 
import queue

q = queue.Queue(100) # back pressure

def producer():
    i = 1
    while True:
        print("producing->",i)
        q.put(i)
        i+=1
        #time.sleep(1)
        
    q.put(None) # stop signal
def consumer():
    while True:
        item = q.get()

        if item is None:
            q.task_done()
            break

        print(f"Consuming: {item}")
        time.sleep(0.02)

        q.task_done()

p_thread= threading.Thread(target=producer)
c_thread= threading.Thread(target=consumer,daemon=True)

p_thread.start()
c_thread.start()

p_thread.join()
c_thread.join()

q.join()

print("All tasks completed")


