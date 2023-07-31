import mysql.connector as mc
import smtplib as sm

choice = print("1. signup \n 2. signin \n 3. changepass \n 4. forgotpass")

def signup():
    con = mc.connect(host="localhost",user="root",password="Maria@mysql",database="reeti")
    cs = con.cursor()
    ch = 'y'
    while ch == 'y':
        name = input(print('Enter the name: '))
        id1 = input(print('Enter the id: '))
        passw = input('Enter the password: ')
        query = "insert into reeti values('{}', '{}', '{}')". format(name, id1, passw)
        ch = input(print('Enter "y" if you want to continue: '))
        cs.execute(query)
    con.commit()
    cs.close()
    con.close()

def signin():
    con = mc.connect(host="localhost",user="root",password="Maria@mysql",database="reeti")
    cs = con.cursor()
    while True:
        id1 = input(print("Enter your ID: "))
        passw = input(print("Enter your password: "))
        query = "select* from reeti where IDNO='{}' and password='{}'". format(id1, passw)
        cs.execute(query)
        result = cs.fetchone()
        if result == None:
            print("Id or password is wrong")
            ch = input(print("Do you want to try again? \n Select 'y' to continue: "))
            if ch == 'y':
                True
            else:
                False
        else:
            print(result)
            print("You have login successfully!!!  :)")   
            False
    con.commit()
    cs.close()
    con.close()

def changepass():
    con = mc.connect(host="localhost",user="root",password="Maria@mysql",database="reeti")
    cs = con.cursor()
    id1 = input(print("Enter your ID: "))
    passw1 = input(print("Enter your old password: "))
    passw = input(print("Enter your new password: "))
    query= "update reeti set password='{}' where password='{}'". format(passw, passw1)
    cs.execute(query)
    con.commit()
    cs.close()
    con.close()

def forgotpass():
    con = mc.connect(host="localhost",user="root",password="Maria@mysql",database="reeti")
    cs = con.cursor()
    id1 = input(print('Enter your ID: '))
    query= ""    




 