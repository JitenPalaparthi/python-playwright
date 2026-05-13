import asyncio
import time 

async def get_even(n):
    even = []
    for i in range(n):
        # time.sleep(0.1)
        if await is_even(i):
            print("even:",i)
            even.append(i)
    return even

async def is_even(n):
    await asyncio.sleep(0.1)
    if n%2==0:
        return True
    else:
        return False
    
def is_evenseq(n):
    asyncio.sleep(0.1)
    if n%2==0:
        return True
    else:
        return False
    
async def get_odd(n):
    odd = []
    for i in range(n):
        await asyncio.sleep(0.1)
        if i%2==0:
            continue 
        print("odd:",i)
        odd.append(i)

    return odd

async def sumof(n):
    sum=0
    for i in range(n):
        await asyncio.sleep(0.1)
        sum+=i
    
    return sum

async def main():
    even,odd,sum = await asyncio.gather(get_even(10),get_odd(20),sumof(50))
    print("even",even)
    print("odd",odd)
    print("sum:",sum)

if __name__=="__main__":
    asyncio.run(main())