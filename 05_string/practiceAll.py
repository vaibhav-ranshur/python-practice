
"""
Question 2 (Beginner)
Now we'll move one step up in difficulty.

Question

Count how many even numbers are present between 1 and N.
"""

n = int(input("enter the positive number"))

total = 0

for i in range(1,n+1):
    if i % 2 == 0:
        total += 1
print("the total even number from 1 to",n,"is",total)

