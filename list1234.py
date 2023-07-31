list1=[]
list2=[]
no=int(input("number of elements in list"))
for i in range(no):
    elements=int(input("Enter the numbers: "))
    list1.append(elements)
for j in list1:
    if j%5==0 or j%7==0:
        list2.append(j)
        j+=1

print(list1)
print(list2)
