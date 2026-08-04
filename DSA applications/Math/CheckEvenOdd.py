import numpy as np

def checkEvenOdd(arr):
    for i in range(len(arr)):
        if (arr[i]&1)==0:
            print(f"{arr[i]}:even", end=" ")
        else:
            print(f"{arr[i]}:odd", end=" ")    
    print()
if __name__=="__main__":
    arr=np.random.randint(0,10,10)
    print(arr)
    checkEvenOdd(arr)