#
from pickletools import string1

str = input("enter the string")
str2 = input("enter the string2")

if len(str) != len(str2):
    print("not anagram")
else:
    for x in str:
        if x not in str2:
            print("not anagram")
            break;
    else:
        print("anagram")


