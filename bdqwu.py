'''

c=0
a=input("enter your text:- ")
for i in a:
    if i in 'Gg':
        c+=1
print("total number of g:-", c)        

'''
'''

c=0
a=("enter the value:- ")
for i in a:
    if i.isdigit():  
        c=c+int(i)
print(c)

'''
'''

.a=79

if a>=50\
       
or a<=89:
          
   print("valid")

else:
               
  print("not valid")

'''
'''

str = input("Enter the string: ")
sum = 0
digitStr = ''
for ch in str :
    if ch.isdigit() :
        digitStr += ch
        sum += int(ch)
if not digitStr :
    print(str, "has no digits")
else :
    print(str, "has the digits", digitStr, "which sum to", sum)

'''



