import mysql.connector as m
con = m.connect(host="localhost", user="root", password="Maria@mysql", database="class_12")
cs = con.cursor()
n=input("Enter Name: ")
o=input("Enter your 5th OP: ")
s=input("Enter your section")
r= int(input("Enter your Scholar Number: "))

query = "insert into students values('{}', '{}', {})". format(n,s,o,r)

cs.execute(query)
con.commit()
cs.close()
con.close()

