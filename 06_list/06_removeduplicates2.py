"""
checking and removing if there is any duplicates in the list (dont create new list modify existing list)
"""

l1 = [3,5,7,9,3,6,5,2,3,7,10]

for i in range(0,len(l1)):
    for j in range(len(l1)-1,i,-1):
        if l1[i] == l1[j]:
            del l1[j]
print(l1)