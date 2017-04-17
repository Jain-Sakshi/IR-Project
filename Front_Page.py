from Spellcheck import correct_phrase
from Account_Spellcheck import correct_name
import os.path
import sys

user_name = input("Enter your account name : ")
if (os.path.isfile(user_name+".txt")):
        file1 = open(user_name+".txt","a+")
else:
    print("\nDid you mean ")
    print(correct_name(user_name))
    choice = input("\n(y/n) : ")
    if choice == 'y':
        user_name = " ".join(str(x) for x in correct_name(user_name))
        file1 = open(user_name + ".txt", "a+")
    else:
        choice = input("\nDo you want to create a new account?\n(y/n) : ")
        if choice == 'y':
            file1 = open(user_name + ".txt", "a+")
            file2 = open("Account_Names.txt", "a+")
            file2.write('\n'+user_name)
            file2.close()
        else:
            print("\nThank you")
            sys.exit()

print ("\nReading file")
query = input("Enter your query :  ")
print("\nDid you mean ")
print(correct_phrase(query))
choice = input("\n (y/n) : ")

if choice == 'y':
    query = " ".join(str(x) for x in correct_phrase(query))
    file1.write('\n'+query)
else :
    file1.write('\n'+query)

file1.close()
file1 = open(user_name+".txt","r+")
print(file1.read());
print ("\nClosing file")
file1.close()
