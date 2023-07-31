#string family functions

#(,) comma is used to start a new parameter
#period(.) separate name and function


'''
capitalize()

when using family function, it will only be only use for that family.
max("string") we will check the first letter's ascii number of the strings,
sum(string) - it will show error. it will show unsupported operant


function/ method signature/ definition/ prototype
rn we are simply calling the function i.e using the function
1. Name of the function
2. argument ()  {when the parathensis is empty}- non argumnet  non parameterised functon
(----){when there is some arguement in it} parameterised function
which type of parameterised function. number of paramertrised
3. return type of the function. when there is no return type- its 'void'. a function which brings a new thing - return type

exit() is viod


math.pow() return type is float.
pow takes exactly 2 arguments 

#STRING FAMILY:-    { .FUNCTION  }
variable.capitalize()
name: capitalize
argument: non parameterised
function: capitalised teh first letter of the string or sentence.
return type: string


.slipt


.upper

'''
'''

.isalpha()   check if the string have all the characters as alphabet
a= reeti agarwal
a.isalpha()0 
#is function will give the answer in bool

'''
'''

c=0
a=input("enter a line:- ")
for i in a:
    if i.isalpha():
        c+=1
print("total number of alphabets", c)

'''
'''

scope of variable
1. local scope  scope means the indentation the variable was introduced and the body it was introduced was like a country
2. global scope   in this, the scope of the variable is now global. i.e. it can be used in the whole programme

'''
'''

isdigit()

islower()

isupper()

'''
'''

al=s=d=sp=l=u=0
a=input("enter a line:- ")
for i in a:
    if i.isalpha():
        al+=1
        if i.islower():
            l+=1
        else:
            u+=1
    elif i.isdigit():
        d+=1
    elif i.isspace():
        s+=1
    else:
        sp+=1

    
print("total number of alphabets ", al)
print("total number of space", s)
print("total number of special", sp)
print("total number of lowercase",l )
print("total number of uppercase", u)
print("total number of digits", d)

''' 

#wap to count the number of specific word in a sentence

a=input("enter the sectence:- ")
b=input("enter the word:- ")
start,end,count= 0,len(a),0

while True:
    result= a.find(b,start.end)
    if result>=0:
        count+=1
        start=result + len(b)
    else:
        break
print(count)    
        
    





a="delhi public school"
a.find("delhi"):- answer would be 0 as the d is in zero index. 
a.find("pub",8):- i want to start finding from 7 index
a.find("pub", 2,6):- from 2 to 5 index.
a.find("pub", 2,8):- from 2 to 7. it will be false as the b in pub exits in 8 index.

when the word exists in the sentence:- posivite

when the word doesnt exits in the sentance:- negative

    
#reeti@gmail.com
1. charater beofre @
2. @gmail.com domain should be there. 

STRING:-


PARTISION;-
b= a.partition("x")

class type of b is tuple.









