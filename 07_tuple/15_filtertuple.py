"""
Given:

numbers = (5, 10, 15, 20, 25, 30, 35)

Create a new tuple containing only the values greater than 15.

You may use a loop and a temporary list.

Expected:

(20, 25, 30, 35)
"""
numbers = (5, 10, 15, 20, 25, 30, 35)
filter_value = []
for x in numbers:
    if x > 15:
        filter_value.append(x)
print(tuple(filter_value))
