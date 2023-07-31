#mail id
'''
no space done
domain done
there should be come characters in mail id prefix done
'''
#password
'''
Min 8 char
The alphabets must be between [a-z]
min 1 Upper Case 
min 1 no.
min 1 special char
'''
#functions
'''
isupper
islower
isdigit
isalnum
'''

eid=input("Enter your mail id: ")

domain="@gmail.com"

elen,dlen=len(eid),len(domain)   #elen = length of email id
                                 #dlen = length of domain
prelen= elen-dlen                #prelen = length of mail prefix
prefix=eid[:prelen]              #prefix of the mail id
good=0
dm= eid[prelen:]                 #dm - second name for domain

if dm==domain:   #1st condition
    if elen>dlen:   #2nd condition to insure that mail id has prefix
        for i in prefix:
            if i==" ":
                print("Space is not allowed")                               #3rd condition space
            elif i.isupper():
                print("Capital letters are not allowed")                    #4th condition capital
            elif i.isalnum(): 
                good+=1
            elif i=="_":  
                pas=input("Enter your password:- ")
            else:
                print("no special character is allowed other than '_'")
    else:
        print("there should be something written")
else:
    print("write correct domain")
                    
            
                
                
            




             
            





                







    
    
