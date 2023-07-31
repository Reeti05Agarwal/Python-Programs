#WAP to print a string in reverse order

def pushstack(stack, ch):
    stack.append(ch)
    return

def popstack(stack):
    if isempty(stack):
        return
    else:
        top=len(stack)-1
        for a in range(top, -1, -1):
            print(stack[a])
        return

stk=[]
top=None
str = input("Enter the string: ")
for a in str:
    pushstack(stk, a)


