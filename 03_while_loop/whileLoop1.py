# reverse the number

number = int(input("Enter a number: "))

while number > 0:
    reminder = number % 10
    number = number // 10
    print(reminder)
