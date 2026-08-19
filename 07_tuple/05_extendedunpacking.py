"""
Given:

numbers = (10, 20, 30, 40, 50, 60)

Use tuple unpacking to get:

first → 10
second → 20
middle → (30, 40, 50)
last → 60

Expected:

10
20
(30, 40, 50)
60
"""

numbers = (10, 20, 30, 40, 50, 60)
first,second,*middle,last = numbers
print(first)
print(second)
print(middle)
print(last)