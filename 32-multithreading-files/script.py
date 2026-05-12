from threading import Thread
from queue import Queue
import os

VOWELS=set("aeiouAEIOU")

def count_vowels_in_files(file_path,result_queue):
    count = 0 
    with open(file_path,"r",encoding="utf-8",errors="ignore") as file:
        for line in file:
            for ch in line:
                if ch in VOWELS:
                    count+=1
        
        result_queue.put((file_path,count,os.getpid()))

def main():

    file1 = "file1.txt"
    file2 = "file2.txt"

    result_queue= Queue()

    p1 = Thread(target=count_vowels_in_files,args=(file1,result_queue),name="File-Reader-1")

    p2 = Thread(target=count_vowels_in_files,args=(file2,result_queue),name="File-Reader-2")

    p1.start()
    p2.start()


    p1.join()
    p2.join()

    while not result_queue.empty():
       file_path,vowel_count,pid = result_queue.get()
       print(f"File:{file_path}")
       print(f"PID:{pid}")
       print(f"Vowel Count:{vowel_count}")
       print("-" * 30)
    
if __name__=="__main__":
    print("")
    main()