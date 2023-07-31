
#FUNCTIONS:

#signature
'''
1. func name
2. return type
3. parameterize/non parameterize

len(L)= calling
l.pop()= pop, (it will remove last element of list) object (that object maybe any datatype. it should be any valid element of the sequence.), non-para
'''

#def --- it means its signature

#types of function:
'''
    1. built in function - python lib pre def
    2. function defined in modules - import (module_name.function_name)
    3. User defined function
    
len - 1
print - 1
sum - 1
max - 1
math.pow - 2
random.rand - 2

pow - which is 1
return type - integer

math.pow - which is 2
return type - float


to write m instead of math-
import math as m
m.pow
then you cant use math.pow now
it will show error if we use that
'''



#4 ways se ban sakte hai:-
'''
1. (non para)
2. (para)
3. with return type
4. without return type
'''
#with non parametrise-
def even(): #(fixed way to define prototype) (no space, no key words, )
    a=int(input("enter a number: "))
    if a%2==0:
        print("even")
    else:
        print("odd")

#with parameterise:-
def even1(a): 
    
    if a%2==0:
        print("even")
    else:
        print("odd")  


