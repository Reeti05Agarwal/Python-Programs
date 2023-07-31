#
'''

a,c=input("enter a line "),0
for i in range(len(a)):
    if a[i]=='a' or a[i]=='e':
        c+=1
print("total no of vowels: ",c)

'''
'''

a,c=input("enter a line "),0
for i in range(len(a)):
    if a[i] in "aeiouAEIOU":
        c+=1
if c==0:
    print("there is no vowels")
else:
    print("total no of vowels: ",c)
    
'''
'''

a,c=input("enter a line "),0
for i in a:    #the variable should be a sequence.
    if i in "aeiouAEIOU":
        c+=1
if c==0:
    print("there is no vowels")
else:
    print("total no of vowels: ",c)

'''
'''

a,c=input("enter a line "),-1
for i in a:
    print(i, " ", a[c])
    c=c-1

'''

a=input("enter a line ")
b=''
for i in a:
    if i not in "aeiouAEIOU":
        b+=1
print("new string without vowel:- ",b)




#no arithmetic opperation can be done on string as it is immutable
