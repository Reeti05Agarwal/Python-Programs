import mysql.connector as mc

print("Press 1 for login", "\n", "2 for Sign up", "\n", "3 for Password Reset", "\n", "4 for  " "\n")
choise =int(input("Enter your choice: "))

def pass_check():
    

def login():
    id_ = input("Enter your ID: ")
    pasw= input("Enter your password: ")
    con = mc.conect(host = 'localhost', user = 'root', password = 'Maria@mysql', database = 'test')
    cs=con.cursor()
    query = "select* from reeti value({''}),({})". format(stud, id)
    cs.execute(query)
    
    
    

def update():
    id_ = input("")
