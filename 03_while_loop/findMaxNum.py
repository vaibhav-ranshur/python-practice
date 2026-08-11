# find the maximum number from the given number

num = int(input("Enter a number of numbers you want to check: "))
count = 0
max = 0

while count < num:
    numbers = int(input("Enter a number: "))
    count += 1
    if numbers > max:
        max = numbers

print("the max number from given number is",max)

# but in this method we cant check negative(-) number and also zero(0)
# so we have another method

num = int(input("Enter a number of numbers you want to check: "))
count = 0
max = int(input("Enter a number: ")) # taking first number as a max number.
# If we initialize max = 0, the program will fail for all-negative inputs.
while count < num - 1:   # we did -1 because we already took 1st no as a max number
    numbers = int(input("Enter a number: "))
    if numbers > max:
        max = numbers
    count += 1

print("the max number from given number is",max)


