import numpy as np
def insertionSort(arr):
    n=len(arr)
    count=0
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        print(arr)            
if __name__=="__main__":
    arr=np.array((110,10,150,20))
    insertionSort(arr)