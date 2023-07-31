#employ and its salary and tax.
sal= int(input("enter your salary: "))
if sal>=100000:
    print("you will get 15% off on tax")
    print[sal-(sal*15/100)]
elif 100000>sal>=75000:
    print("you will get 10% off on tax")
    print[sal-(sal*10/100)]
else:
    print("no tax")
    
