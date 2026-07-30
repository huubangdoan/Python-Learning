import numpy as np
def mergeSort(arr):
    if len(arr)==1 or len(arr)==0:
        return arr
    left, right=divideArr(arr)
    left=mergeSort(left)
    right=mergeSort(right)
    print(left)
    return conquerArr(left, right)
def divideArr(arr):
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    return left, right
def conquerArr(arr1, arr2):
    ans=[]
    i=j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i] > arr2[j]:
            ans.append(arr2[j])
            j+=1
        else:
            ans.append(arr1[i])
            i+=1
    ans.extend(arr1[i:])
    ans.extend(arr2[j:])
    return ans


if __name__=="__main__":
    arr=np.random.randint(0,10,10).tolist()
    print(arr)
    print(mergeSort(arr))