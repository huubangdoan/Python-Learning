import numpy as np 
import random
def binarySearch(e, arr):
  low, high= 0, len(arr)-1
  mid=(low+high)//2
  print(mid)
  while arr[mid]!=e:
    low, mid, high=checkMid(e, arr, low, mid, high)
    if arr[mid]==e:
       print(f"found {e} in the index {mid}")
       break
    elif low>high:
       print(f"not found {e}")
       break
def checkMid(e, arr, low, mid, high):
    if e>arr[mid]:
      low=mid
      mid=(low+high)//2
    elif e<arr[mid]:
       high=mid
       mid=(low+high)//2
    return low, mid, high

def arrAscendingSort(arr):
    arr=np.sort(arr)
    print(arr)
    return arr

if __name__=="__main__":
    arr=np.random.randint(0,10, size=10)
    print(arr)
    binarySearch(5, arrAscendingSort(arr))
