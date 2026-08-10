#find differance bertween two numbers

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
#differance  = num1 - num2
if num1 < num2:
    print("differance =",num2-num1)
else:
    print("differance =",num1-num2)

# 2nd way

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
#differance  = num1 - num2
if num1 - num2 < 0:                                   #just the condition differance
    print("differance =",num2-num1)
else:
    print("differance =",num1-num2)

