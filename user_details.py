file1 = open("config.py","w")
USER_NAME = input("Enter Your E-Mail")
PASSWORD = input("Enter the Password")
file1.write('USER_NAME=("'+USER_NAME+'")\n')
file1.write('PASSWORD=("'+PASSWORD+'")\n')


file1.close() #to change file access modes

