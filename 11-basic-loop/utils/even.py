def even1(n):
    count=0
    while count<n:
        if count%2!=0:
            count+=1
            continue # just to show how continue work
        else:
            print(count,end=" ")
        count+=1