"""
numbers = (10, 20, 30, 40, 50, 60)

Create a new tuple containing only the even numbers greater than 25.

Expected output:

(30, 40, 50, 60)
"""
numbers = (10, 20, 30, 40, 50, 60)
new_numbers = []
for x in numbers:
    if x > 25 and x % 2 == 0:
        new_numbers.append(x)
print(tuple(new_numbers))
