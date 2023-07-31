'''
wap that inputs a main string and then create an encrypted
string byembendding a short symbol vased string after after
each character. also able to prduce decrypted string
from encrypted string
'''

mainstring = input("Enter main String: ")
encrypkey = input("Enter encrypted key: ")
encrypstr = encrypkey.join(mainstring)
decrypstr = encrypstr.split(encrypkey)
print("The encrypted string is: ", encrypstr)
print("The decrypted string is: ", "".join(decrypstr))
#to convert decrypstr from list to string
