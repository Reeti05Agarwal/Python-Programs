import mysql.connector as m
import smtplib as s 
import random


def login():
   id=int(input("enter id"))
   password=input("enter password")
   con=m.connect(host="localhost",user="root",password="prak_1135",database="test")
   cs=con.cursor()
   query="select * from test where id={} and password='{}'". format(id,password)
   cs.execute(query)
   result=cs.fetchone()
   if result==None:
      print("id or password is wrong")
      
   else:
      print(result[0],"\t",result[1],"\t",result[2])
      
   print("you have done your login successfully!!!")
   cs.close()
   con.close()


            


def signup():
   con=m.connect(host="localhost",user="root",password="prak_1135",database="test ")
   cs=con.cursor()
   id=int(input("enter id in digits"))
   name=input("enter name")
   email=input("enter email address")
   
   while True:
      pwd=input("enter password of atleast 8 characters(numbers and alphabets both)")
      if pwd.isalnum() and len(pwd)>=8:
         password=pwd
         break
      else:
         print("please re-enter a new password as it doesn't satisfy conditions")
         pass

   query="insert into test values({},'{}','{}','{}')". format(id,name,password,email)
   print("signed up successfully :)")
   cs.execute(query)
   con.commit()
   cs.close()
   con.close()

def changepwd():
   con=m.connect(host="localhost",user="root",password="prak_1135",database="test")
   cs=con.cursor()
   id=int(input("enter id"))
   name=input("enter your name")
   
   for i in range(3):
      pwd=input("enter old password")
      newpwd=input("enter new password of atleast 8 characters(numbers and alphabets both)")
      if newpwd.isalnum() and len(newpwd)>=8:
         break
      else:
         print("please re-enter again as it doesn't satisfy conditions")
         continue
   query="update test set password='{}' where password='{}'". format(newpwd,pwd)
   print("password changed successfully")
   cs.execute(query)
   con.commit()
   cs.close()
   con.close()

def forgotpwd():
   con=m.connect(host="localhost",user="root",password="prak_1135",database="test")
   cs=con.cursor()
   name=input("enter your name")
   id=int(input("enter your id"))
   query="select email from test where id={}". format(id)
   cs.execute(query)
   result=cs.fetchone()
   email=result[0]
   otp=int(random.randint(1000,5000))
   server=s.SMTP_SSL("smtp.gmail.com",465)
   server.login("cutepanda1135@gmail.com","cutestpanda_1135")
   server.sendmail("cutepanda1135@gmail.com","%s"%email,"%d"%otp)
   server.quit()
   
   print("an OTP mail has been sent to your registered email address which is %s"%email)
   otpent=int(input("enter otp"))
   if otpent==otp:
        print("otp verified :)")
        newpwd=input("enter new password")
        while True:
            if newpwd.isalnum() and len(newpwd)>=8:
                break
            else:
                print("please re-enter again as it doesn't satisfy conditions")
        query="update  test set password='{}' where id={}". format(newpwd,id)
        print("new password has been set successfully :)")
        cs.execute(query)
        con.commit()
        cs.close()
        con.close()
   else:
        print("otp entered is wrong,please try again later")
      
while True:
   print("press:","\n","1 for login","\n","2 for signup","\n","3 for change password","\n", "4 for forgot password","\n", "5 to quit")
   choice=int(input("enter choice"))
   if choice==1:
      login()
   elif choice==2:
      signup()
   elif choice==3:
      changepwd()
   elif choice==4:
      forgotpwd()
   else:
      print("thanks for using our program :)")
      break
   
'''
Menu:
Choice 1 - 
'''

         
