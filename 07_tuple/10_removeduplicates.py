"""
Given:

numbers = (10, 20, 10, 30, 20, 40, 30, 50)

Create a new tuple containing only unique values, while preserving their original order.

Expected output:

(10, 20, 30, 40, 50)
"""

numbers = (10, 20, 10, 30, 20, 40, 30, 50)
unique = []
for x in numbers:
    if x not in unique:
        unique.append(x)
numbers = tuple(unique)
print(numbers)




seen = set()
result = []

for x in numbers:
    if x not in seen:
        seen.add(x)
        result.append(x)
print(result)
print(seen)