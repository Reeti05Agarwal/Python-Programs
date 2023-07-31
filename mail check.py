eid=input("enter your mail id: ")
domain="@gmail.com"
elen,dlen=len(eid),len(domain)


dm=eid[elen-dlen:]

if dm==domain:   #1st validation
    if elen>dlen:  #2nd validation
        if " " in eid[:elen-dlen] and eid[:elen-dlen].isalum():
            print("space is not allowed")
        else:
            pas=input("enter your password: ")#password
            if len(pas)>=8:
                for i in pas:
                    if 
     else:
        print("please write some characters before domain")        
else:
    print("please give a valid domain")
    

'''
password
min: 8 char
minimum one capital letter
min one special char
min one small letter

1-10 average
11-15 good strength

'''
