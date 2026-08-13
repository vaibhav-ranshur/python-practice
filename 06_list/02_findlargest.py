"""
Write a Python program to find the largest number in the list without using max().
"""
numbers = [100, 20, 130, 40, 50]
largest = numbers[0]
for x in numbers:
    if x > largest:
        largest = x

print(largest)