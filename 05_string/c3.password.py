# check if password and confirm password are same/

password = input("enter your password: ")
confirm_password = input("re-enter your password: ")

if password == confirm_password:
    print("password match")
else:
    if password.casefold() == confirm_password.casefold():
        print("please check for the cases")
    else:
        print("password does not match please re enter the same password")