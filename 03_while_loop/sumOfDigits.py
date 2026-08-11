#find sum of digits in number

number = int(input("Enter a number: "))
sum = 0
while number > 0:
    r = number % 10
    sum = sum + r
    number = number // 10

print ("The sum of a digits is = ", sum)

number = 1
sum = 0

while number <= 100:
    sum += number
    number += 1
print("sum =",sum)