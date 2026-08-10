#check if a person is authorised for admin access

username = "vaibhav"
username1 = "gajanan"
password = input("Enter your password: ")
if password == username or password == username1:
    print("Authorised")
else:
    print("not authorised")