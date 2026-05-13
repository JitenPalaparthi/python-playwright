# is your task CPU heavy or IO based ?

# async await --> Usually they run on single thread 
# EventLoop --> Loop that keeps on running the scheduled tasks
# Do they run parallel --> Usually No 
# How do they run concurrently ? 
# Any IO operation happens --> Python calls the syscall , the os has to reposnd back to Python after completing the task, that time it takes to respond back 
# is effectively used by excecuting the other task which is again an async tack
# how Python knows that the task is completed from the system side? epoll, kqueue,kctl

# Threads have stack , coroutines are stackless

import asyncio 
import time 

async def task1():
    print("Task1 Started")
    #time.sleep(3) #blocking
    await asyncio.sleep(3)
    print("Task1 Completed")

async def task2():
    print("Task2 Started")
    #time.sleep(3) #blocking
    print("Task2 Completed")

async def main():
    await task1() # after executing task1 task2 starts
    await task2()

async def mainc():
    await asyncio.gather(task1(),task2())

if __name__=="__main__":
    #asyncio.run(main())
    asyncio.run(mainc())

