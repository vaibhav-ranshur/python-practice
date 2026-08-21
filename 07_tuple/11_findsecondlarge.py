"""
Given:

numbers = (10, 50, 20, 50, 40, 30, 40)

Find the second-largest unique value.

Expected output
40
"""

numbers = (10, 50, 20, 50, 40, 30, 40)
l1 = []

for x in numbers:
    if x not in l1:
        l1.append(x)
l1.sort()
print(l1[-2])

