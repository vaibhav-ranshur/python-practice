"""
find minimum index sum of two lists
"""

fav1 = ["pizza","nuggets","hotdog","noodles","pasta","burger"]
fav2 = ["burger","hotdog","noodles","pasta","nuggets","pizza"]

index1 =10
for i in range(len(fav1)):
    for j in range(len(fav2)):
        if fav1[i] == fav2[j]:
            index = i+j
            if index < index1:
                index1 = index
print("the minimum sum of the index is",index1)


    