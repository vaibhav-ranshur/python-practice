# find the sum of given numbers as input

numberOfNums = int(input("Enter how many numbers do you want to add: "))
counter = 0
sum = 0

while counter < numberOfNums:
    num = int(input("Enter a number: "))
    sum += num
    counter +=1

print("sum =",sum)