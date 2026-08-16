"""
add two matrix
"""
l1 = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
l2 = [[5,6,7,8],[5,6,7,8],[5,6,7,8]]

l3 = []

for i in range(3):
    s = []
    for j in range(4):
        s.append(l1[i][j]+l2[i][j])
    l3.append(s)
print(l3)