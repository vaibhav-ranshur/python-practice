# display multiplication table for given number

n = int(input("enter the number"))

for count in range(1, 11):
    print(n,"*",count,"=",n*count)