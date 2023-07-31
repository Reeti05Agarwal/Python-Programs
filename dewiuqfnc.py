'''
len takes no integers

sum of digit
reverse
palidrome
armstring

164 = 1+6+4=11
kartik =164
mridul (sum)=0
step1:
    r=164%10   r=4
    mridul     0+4 = 4
    164//10
    kartik=16
step2:
    r=kartic%10





SUM OF DIGITS:- 


'''
'''
a=int(input("enter a no.:- "))
sum=0
while a>0:
    r=a%10
    sum=sum+r
    a=a//10
print("sum of digit is:- " ,sum)    

'''
'''

i=1
while True:
    print(i)
    i+=1
    if 1==10:
        break


'''
'''

a=int(input("enter a no.:- "))
sum,temp=0,a    #variable decleration
#logic
while a>0:
    r=a%10
    sum=sum*10+r
    a=a//10
print("sum of digit is:- " ,sum)   
if temp==sum:
    print("it is palindrome")
else:
    print("it is not palindrome")

'''

#armstring   sum of the cude of every digit in a number should be same as the original number


a=int(input("enter a no.:- "))
arm,temp=0,a    #variable decleration
#logic
while a>0:
    r=a%10           # r is a remainder
    arm=arm+r**3     # OR s=s+r*r*r   #OR arm=arm+math.pow(r,3)
    a=a//10 
if temp==arm:
    print("it is armstrong")
else:
    print("it is not armstrong")



