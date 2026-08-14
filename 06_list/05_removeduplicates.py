"""
checking and removing if there is any duplicates in the list
"""

l1 = [3,5,7,9,3,6,5,2,3,7,10]
l2 =[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)

