#Set a bit in the number
def setBit(num, pos):
    num = num|(1<<pos)
    return num
#unset/clear a bit at n'th position in the number
def removeBit(num, pos):
    num&=(~(1<<pos))
    return num
#Toggling a bit at nth position
def toggleBit(num, pos):
    num^=(1<<pos)
    return num
if __name__=="__main__":
    print(setBit(10,2))
    print(removeBit(10,2))
    print(toggleBit(10,2))
