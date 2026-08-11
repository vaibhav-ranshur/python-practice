# counting the number of digits in number

number = int(input("Enter a number: "))
count = 0
while number > 0:
    number = number // 10
    count = count + 1
print("number of digits are = ", count)
