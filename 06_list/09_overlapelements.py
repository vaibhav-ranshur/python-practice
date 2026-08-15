"""
overlapping elements of two lists
"""

l1 = [1,5,3,4,9,7]
l2 = [5,2,8,9,1,6,7]

l3 = []
for i in range(0,len(l1)):
    if l1[i] in l2:
        l3.append(l1[i])
print(l3)

