# print n terms of AP (arithmatic progression) series

a = int(input("Enter initial term: "))
d = int(input("Enter a common differance: "))
n = int(input("Enter number of terms: "))


for i in range(a,a + n * d,d):
    print(i)
