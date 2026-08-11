# display creditcard number in given format 1234 4569 1235 1222  --> **** **** **** 1222

cardNum = input("please input the 16 digit card number ")
lastDigits = cardNum[15::]
str = "*" * 4 + " "
displayNum = str * 3 + lastDigits
print(displayNum)

