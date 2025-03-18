username = input("Enter the User Name: ")
password = input("Enter the password: ")

login_username = input("Enter the User Name: ")
login_password = input("Enter the password: ")

if username == login_username and password == login_password:
    print("Authendicated Successfull")
elif username == login_username or password == login_password:
    print("User name or password incorrect!!!")
else:
    print("Both username and password incorrect!!!")