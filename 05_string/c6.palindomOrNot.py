# check if string is palindrom or not

str = input("enter the string")
rev = str[::-1]

if str == rev:
    print("yes'its pelindrom")
else:
    print("no'its not pelindrom")

# convert input string into palindrome

str1 = input("enter the string")
rev1 = str1[::-1]
print(str1 + rev1)