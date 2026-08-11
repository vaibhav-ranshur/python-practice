# find the factorial of given number

n = int(input("enter a number"))
fact = 1
for i in range (1,n+1):
    fact *=  i

print("the factorial of ",n,"is ",fact)