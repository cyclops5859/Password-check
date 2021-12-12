# Created by Cyclops
import re

print ("For more secure password remember the following rules")
print ("")
print ("Minimum 8 characters.")
print ("The alphabets must be between [a-z]")
print ("At least one alphabet should be of Upper Case [A-Z]")
print ("At least 1 number or digit between [0-9].")
print ("At least 1 character from [ _ or @ or $ ].")
print ("")

password = (input("Enter your Password to check validity : "))
flag = 0
while True:  
    if (len(password)<8):
        flag = -1
        break
    elif not re.search("[a-z]", password):
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    elif not re.search("[_@$]", password):
        flag = -1
        break
    elif re.search("\s", password):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        break

if flag ==-1:
    print("Not a Valid Password")
