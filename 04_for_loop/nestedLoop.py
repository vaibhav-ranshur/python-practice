# nested for loop
# A nested for loop means a for loop inside another for loop.
# The inner loop runs completely for each iteration of the outer loop.

#basic nested loop
for i in range(0,5):
    for j in range(0,5):
        print(i, j)



for i in range(0,5):
    for j in range(0,5):
        print("(",i, j,")", end = '')
    print('')

for i in range(0, 5):
    for j in range(0, 5):
        print("(", i+j, ")", end='')
    print('')

# pattern printing

for i in range(0, 5):
    for j in range(0, 5):
        print("*", end = '')
    print()

# 2nd pattern printing
for i in range(0, 5):
    for j in range(0, 5):
        if i <= j:
         print( "*", end='')
    print('')

# 3rd pattern printing
for i in range(0, 5):
    for j in range(0, 5):
        if i >= j:
            print("*", end='')
    print('')

s1 = "xyz"
s2 =  "abc"

for i in s1:
    for j in s2:
        print(i,j,end=" ")
    print('')