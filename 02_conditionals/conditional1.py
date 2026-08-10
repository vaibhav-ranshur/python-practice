# if ..... else statement
#if else statement is a conditional statement used to make decision in a program
# if checks the condition if condition is true then if block executes
# else block execute when condition is false

# write a program to check input number taken from user is negative or positive

num = int(input("Enter a number: "))
if num < 0:
    print("Sorry, the number is negative.")
else:
    print("The number is positive.")

#write a program to check given num is even or odd

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num," is even number.")
else:
    print(num,"is odd number,")

