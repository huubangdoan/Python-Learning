import numpy as np
import random as rand
def bubbleSort(arr):
    arrLen=len(arr)
    for i in range(arrLen-1):
        for j in range(arrLen-1-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]
                print(arr)
if __name__=="__main__":
    arr=np.array((110,20,10,120,50,140))
    print(arr)
    bubbleSort(arr)




