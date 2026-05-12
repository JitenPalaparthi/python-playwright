from multiprocessing import Process,Queue,current_process 
import os
import time 

def worker(numbers, result_queue):

    process = current_process()

    print(f""" Process Started Name: {process.name} PID: {os.getpid()}""")

    results =[]

    for n in numbers:
        total=0
        for i in range(10):
            total+=1
            square = n * n
            print(f"{process.name} processed {n}") 

            results.append((n,square))
    
    result_queue.put(results)
    print(f"{process.name} finished")

def main():
    numbers = list(range(1,11))

    chunk1 = numbers[:3]
    chunk2 = numbers[3:6]
    chunk3 = numbers[6:]

    print(chunk1)
    print(chunk2)
    print(chunk3)



    result_queue = Queue()

    processes = [
        Process(target=worker,args=(chunk1,result_queue),name="worker-1"),
        Process(target=worker,args=(chunk2,result_queue),name="worker-2"),
        Process(target=worker,args=(chunk3,result_queue),name="worker-3")
    ]

    # Each Process has seperate memory, pid, python interpreter, runs on separte core(most probably)

    start = time.time()

    for p in processes:
        p.start()
    
    for p in processes:
        p.join()

    final_results=[]

    while not result_queue.empty():

        final_results.extend(result_queue.get())

        end = time.time()

    for number,square in sorted(final_results):
        print(f"{number} --> {square}")

    print(f"\nCompleted in {end - start:.2f} seconds")


if __name__=="__main__":
    main()