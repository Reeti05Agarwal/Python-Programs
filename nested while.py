 
# wpa to take a number and print the list of prime from 1 to input
#armstrong
'''
for i in range(1,501):
    temp,arm=i,0
    while temp>0:
        r=temp%10
        arm=arm+r**3
        temp=temp//10
    if i==arm:
        print(i)  

'''
'''

i=1
while i<=500:
    temp,arm=i,0
    while temp>0:
        r=temp%10
        arm=arm+r**3
        temp=temp//10
    if i==arm:
        print(i) 
    i=i+1  

'''
'''
#list of prime 
a=int(input("enetr a number:- "))
for i in range(2,a+1):
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag=1
            break
        if flag==1:
            print(i)

         
#or 
a=int(input("enetr a number:- "))
for i in range(2,a+1):
    for j in range(2,i):
        if i%j==0:
            break   # if break works, then else me nahi jaega
    else:
        print(i)
'''
a=int(input("enetr a number:- "))
for i in range(2,a+1):
    j=2
    while j<i:
        if i%j==0:
            break
        j=j+1
    else:
        print(i)    
        


      
