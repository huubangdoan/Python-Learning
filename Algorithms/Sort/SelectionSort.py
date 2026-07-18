import numpy as np 
def selectionSort(arr):
    n=len(arr)
    for i in range(n-1):
        minIndex=i
        for j in range(i+1, n):
            if arr[j]<arr[minIndex]:
                minIndex=j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
        print(arr)
if __name__=="__main__":
    arr=np.array((72,4
                  ,12,53,15,2,8,16,40,21,7,87,35))
    selectionSort(arr)