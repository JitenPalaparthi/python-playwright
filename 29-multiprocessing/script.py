from multiprocessing import Process

def work():
    print("Process is running")

if __name__=="__main__":
    p= Process(target=work)
    p.start()
    p.join()