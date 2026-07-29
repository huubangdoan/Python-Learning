import numpy as np
def linearSearch(e, arr):
    for i in range(len(arr)):
        if arr[i]==e:
            print(f"Found {e} at index {i}")
if __name__=="__main__":
    arr=np.array([0,20,30])
    linearSearch(0,arr)