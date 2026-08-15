"""
overlapping elements of two lists
"""

l1 = [1,5,3,4,9,7]
l2 = [5,2,8,9,1,6,7]

l3 = []
for x in l1 :
    if x in l2:
        l3.append(x)
print(l3)
