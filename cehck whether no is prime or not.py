###wap to take a number and check whether given number is prime or not

a=int(input("enter a number "))
for i in range(2,a//2):
    if a%i==0:
        print(a, " is not prime")
        break
else:
    print(a, " is prime")
    






#if the loop lives its whole life without gettung forcefully killed, then else is executed.
#if the loop if statement getstrue, then it is forcefully killed.   

#break forfully breaks the loop when the condition becomes true
        

#write a programme to print buz number from 1 to n (taken by user)
    '''write a programme to calculate the following series
    1+2+3+4+.....+n
    fina i/p 5    1+2+3+4+5
    o/p=15

    1^1+2^2+3^3+.......n^n

    1^2+2^2+3^2+.......n^2'''
