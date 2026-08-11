# print prime number 1 to 100


for i in range(1,101):
    count = 0
    for j in range(1,101):
        if i%j == 0:
            count += 1
    if count == 2:
        print(i)

