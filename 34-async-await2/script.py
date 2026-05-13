import asyncio

async def task1():
    for i in range(10):
        await asyncio.sleep(0.1) # the moment is is being slept , the eventloop executes the next task
        print("task-1-->",i)

async def task2():
    for i in range(10):
        await asyncio.sleep(0.1)
        print("task-2-->",i)

async def main():
    await task1()
    await task2()

async def mainc():
    await asyncio.gather(task1(),task2())


asyncio.run(mainc())