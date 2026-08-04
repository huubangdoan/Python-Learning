def sumOfNaturalNum(num):
    if num==1:
        return 1
    return num+sumOfNaturalNum(num-1)
if __name__=="__main__":
    print(sumOfNaturalNum(4))