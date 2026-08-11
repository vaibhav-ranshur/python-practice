# Print numbers from 1 to 10 using a while loop.

count = 1

while count <= 10:
    print("count",count)
    count = count + 1

#Print numbers from 10 to 1.

counter = 10
while counter <= 10 and counter > 0:
    print("counter",counter)
    counter = counter - 1

#Print all even numbers between 1 and 20.

even = 1
while even <= 20 and even >= 0:
    if even % 2 == 0:
        print("even",even)
    even += 1

            # or

even = 0
while even <= 20 and even >= 0:
    print("even", even)
even += 2

#Print all odd numbers between 1 and 20.

num = 1
while num <= 20 and num >= 1:
    if num % 2 != 0:
        print("even",num)
    num += 1

#Find the sum of numbers from 1 to 100.

number = 1
sum = 0

while number <= 100:
    sum += number
    number += 1

print("sum =",sum)

