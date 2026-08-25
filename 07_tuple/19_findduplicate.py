"""
Given:

numbers = (10, 20, 30, 20, 40, 10, 50, 30)

Create a new tuple containing the values that appear more than once, with each value appearing only once.

Expected:

(10, 20, 30)
"""
numbers = (10, 20, 30, 20, 40, 10, 50, 30)
l3 = []
l1 = tuple(numbers)
for i in range(0,len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i] == l1[j]:
            if l1[i] not in l3:
                l3.append(l1[i])
print(tuple(l3))
