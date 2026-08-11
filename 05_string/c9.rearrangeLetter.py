# re-arrange the letter(lowercase then uppercase)

str = input("enter te string (should having upper and lower case letters)")

upper = ""
lower = ""

for x in str:
    if x.islower():
        lower += x
    else:
         upper += x

rearrange = lower + upper
print (rearrange)