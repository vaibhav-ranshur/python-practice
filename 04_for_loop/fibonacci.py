# find the n term of fibonacci series.

n = int(input("enter the term of fibonacci"))
a = 0
b = 1

for i in range(n+1):
    print(a)
    c = a + b
    a = b
    b = c
