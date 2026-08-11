# find the user id and domain name from email address

email = input("please enter your email: ")
atrate = email.find("@")
print("user id : ", email[:atrate])
print("domain name : ", email[atrate:])
