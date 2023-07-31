#wap to take and age from the user as input and check whether user is adult or not.

 
name= input("enter your name: ")
age= int(input("Enter your age: "))
if age>= 18:
    print("hello", name, "you are an adult by ", age-18, "years.")
else:
    print("hello", name, "you are not an adult by ", 18-age, "years")

