'''
54321
4321
321
1

'''
'''

1. print= i/j      same = i   differen t= j
2. j=loop ka first number is the start range of j
   what ever i or j, ckeck 1st number of the pattern
3. 1st row = 1 number, i and j will start the same
   1st row = 5 numbers, then i and j will start with opposite number. 

'''

'''
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end='')
    print()    

'''


'''
54321
4321
321
21
1
'''


'''
for i in range(1,6):
    for j in range(5,i-1,-1):     #5>0 4>0 3>0 2>0 1>0
        print(j,end='')
    print()


 '''

'''
1
12
123
1234
12345
'''

'''
for i in range(1,6):
    for j in range(1,):    #1<2 t ; 2<2f     #1<3 t ; 2<3 t ; 3<3 f
        print(j,end='')
    print()    

'''

'''
12345
1234
123
12
1
'''

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print()    





'''
12345
2345
345
45
5
'''





'''
1
22
333
4444
5555
'''

'''
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end='')
    print()    

'''


'''
a
bb
ccc
dddd
eeeee
ffffff
'''

'''
for i in range(97,103):
    for j in range(97, i+1 ):
        print(chr(i),end='')
    print()
'''

'''

ord() gives ordinal number

chr() marks preceding arguments as positional
opposite of ord()


'''


'''
A
AB
ABC
ABCD
'''

'''
dddd
ccc
bb
a
'''


'''
    a
   ab
  abc
 abcd
abcde 
'''

'''
for i in range():
    for k in range(space):
        print(" ",end='')
    for j in range( ):
        print(,end='')
    print()    
'''
