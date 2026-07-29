import numpy as np
import random
def countingSort(arr):
    cntArr=countFrequency(arr)
    culcArr=calculatePrefixFrequency(cntArr)
    outputArr=[0]*(len(arr))
    for i in range(len(arr)-1,-1,-1):
        outputArr[culcArr[arr[i]]-1]=arr[i]
        culcArr[arr[i]]-=1
        print(outputArr)
    return outputArr

def countFrequency(arr):
    max_value=max(arr)
    cntArr=[0]*(max_value+1)
    for num in arr:
        cntArr[num]+=1
    return cntArr

def calculatePrefixFrequency(cntArr):
    for i in range(1,len(cntArr)):
        cntArr[i]+=cntArr[i-1]
    return cntArr


if __name__=="__main__":
    arr=np.random.randint(0,10,10).tolist()
    print(arr)
    countingSort(arr)