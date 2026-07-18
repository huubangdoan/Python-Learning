import numpy as np
def createFixedStack(size):
    stack=np.zeros(size)
    global top 
    top=-1
    print(stack)
    return stack
def pushStack(e, stack):
    global top
    size=len(stack)
    if top == size-1:
        return
    top+=1
    stack[top]=e
    print(stack)
def popStack(stack):
    global top
    if top == -1:
        return
    e = stack[top]      
    stack[top] = 0
    top -= 1             
    print(stack)
    
if __name__=="__main__":
    stack=createFixedStack(5)
    pushStack(10, stack )
    pushStack(9, stack )
    pushStack(2, stack )
    pushStack(3, stack )
    pushStack(8, stack )
    popStack(stack)
    popStack(stack)
    popStack(stack)
    popStack(stack)
    popStack(stack)
    popStack(stack)

    

        
