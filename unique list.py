#wap

size=int(input("enter the sixe of the list:- "))
list=[]
for i in range(size):
    num =int(input("enter element:- "))
    list.append(num)
    
unique=[]
count=[]
for i in list:
    if i not in unique:
        unique.append(i)
        b=l.count(i)
        count.append(b)
        print("count of", i, "is", b)

print(list)
print(unique)
print(count)
