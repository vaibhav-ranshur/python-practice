# display multiplication table for given number.

number = int(input("Enter a number: "))
count = 1
while count <= 10:
    mul = number * count
    print(number,"*",count,"=", mul)
    count += 1

