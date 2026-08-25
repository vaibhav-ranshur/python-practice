"""
Given:

numbers = (10, 20, 30, 40, 50)

Create a new tuple by moving the last element to the beginning.

Expected output
(50, 10, 20, 30, 40)
"""

numbers = (10, 20, 30, 40, 50)
t1 = numbers[-1:]
t2 = numbers[:-1]
t3 = t1 + t2
print(t3)
