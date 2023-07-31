'''types of function:-
1. predefined functions ()
id, type, range, print, int

2. module
have to write import function






'''

import math   #math is a module   pow is the function
b=math.pow(2,3)   #answer is float(decimal)  pow function is exponent function
print(b)            #'ctrl'+'space' to show the function

import math 
a=math.sqrt(16)
print(int(a))

'''
or
import math 
a=int(math.sqrt(16))
print(a)
'''

import math                   #if you want to print it once, it should not be under the loop
for i in range(5):            #if you want to print in the loop, it should be under the loop
    b=int(math.pow(i,2))
    print(b)

import random       #used to generate random number between 0 and 1 where neither 0 nor 1 appears
b=random.random()   #signature of function    
print(int(b*10))


'''
import random       #used to generate random number
b=random.random()
print(b*10)

import random       #used to generate random number
b=random.random()
print(b)


'''

import random       #used to generate random number
b=random.randint(2,10)   #it wont be float   wont take float as range
print(b)


#random for float
#randint for integers


#lucky game
import random
b=random.randint(1,10)
for i in range(3):
    c=int(input("enter your number: "))
    if c==b:
        print("congo, you win")
        break
    elif i<2:
        print("sorry, you lost")
    else:
        print("sorry u lost the game")
        


    
