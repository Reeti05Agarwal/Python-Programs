'''
>>> dec1={}
>>> dec1
{}
>>> dict1={}
>>> dict2=dict()
>>> dict2
{}
>>> dict3 = {"key":89,"abs":12}
>>> dict3
{'key': 89, 'abs': 12}
>>> dict3["key"]
89
>>> d1={1:34, 2:45}
>>> d1[1]
34
>>> d1[5]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    d1[5]
KeyError: 5
>>> d1[1]=7
>>> d1[1]
7
>>> d1[5]="reeti"
>>> d1
{1: 7, 2: 45, 5: 'reeti'}
>>> 1 in d1
True
>>> 9 in d1
False
>>> len(d1)
3
>>> len(d1[1])
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    len(d1[1])
TypeError: object of type 'int' has no len()
>>> len(d1(1))
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    len(d1(1))
TypeError: 'dict' object is not callable
>>> len(len[5])
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    len(len[5])
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> len(d1[5])
5
>>> d1.keys()
dict_keys([1, 2, 5])
>>> d1.values()
dict_values([7, 45, 'reeti'])
>>> d1.items()
dict_items([(1, 7), (2, 45), (5, 'reeti')])
>>> d1.get(7)
>>> d1.get(1)
7
>>> d1.del('reeti')
SyntaxError: invalid syntax
>>> del dict1['reeti']
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    del dict1['reeti']
KeyError: 'reeti'
>>> del dict1[1]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    del dict1[1]
KeyError: 1
>>> del d1['reeti']
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    del d1['reeti']
KeyError: 'reeti'
>>> del d1[1]
>>> del dictionary name [key]



'''

#dictionary is mutable



#creat a dictionary


#del dictionary name [key]
'''
you cant make a dictionary if the key is mutable.
key should always be immutable.
therefore key should always be mutable.
value can be mutable or immutable.

its not sequence
indexing is not applicable
keys are always unit. we cant repeat the keys.
but values can be repeated.
'''


'''
 b={1:["pakhi",98,46,28,32,56], 2:("achal", 97,23,54,67,87), 3: {"reeti": [90,34,55,76,54]}}

'''


'''
c={}
sum1=0
for i in range(3):   #for names 
    list1=[]
    rno=int(input("enter the roll number: ")
    name=input("enter the name: ")
    list1.append(name)
    for j in range(5):
        marks=int(input("enter the marks: "))
        list1.append(marks)
        sum1+=marks        
    list1.append(sum1)
    list1.append(sum1/5)        
    a[rno]=list1    
'''

'''
d1={5:"Number",\
    "a": "string",\
    (1,2): "Tuple"}
for key in d1:
    print(key,":", d1[key])
print(type(d1))    
'''

'''
d2={}
for i in range(3):
    name=input("enter the name: ")
    telephone=int(input("enter the phone number: "))
    d2[name]=telephone
    
print(d2)
for x in d2:
    print(x,":",d2[x])
'''


'''
m={}
list1=[]
length=int(input("length of dictionary: "))
for i in range(length):
    rollno=int(input("enter the roll. number: "))
    marks=int(input("enter the marks: "))
    list1.append(marks)
    score=

'''

'''
m={}
n=int(input("how many students? "))
for i in range(n):
    r,n=eval(input("roll_no, marks:"))
    m[r]=n

print(m)    
'''


#wap to store name of states and their CAPITAL
'''
d1={}
no=int(input("enter the number of states: "))
for i in range(no):
    s=input("enter the states: ")
    c=input("enter the capital: ")
    d1[s]=c

print(d1)
'''

#in list form
'''
d1={}
listc=[]
lists=[]
no=int(input("enter the number of states: "))
for i in range(no):
    s=input("enter the states: ")
    c=input("enter the capital: ")
    lists.append(s)
    listc.append(c)
    d1[lists[i]]=listc[i]
print(lists)
print(listc)
print(d1)
'''

#store roll name and marks. name of those students whose marks is greater then 75
'''
d1={}

no=int(input("enter the number of students: "))
for i in range(no):
    rollno=int(input("enter the roll number: "))
    name=input("enter the name: ")
    marks=int(input("enter the marks: "))
    if marks.=75:
        d1[rollno]=[name,marks]

print(d1)
'''
 
    


