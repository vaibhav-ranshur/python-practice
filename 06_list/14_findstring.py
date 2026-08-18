""""
find the word starting with the given letter in the list
"""

food = ["pizza","nuggets","hotdog","noodles","pasta","burger"]

letter = input("enter the letter").lower()
found = "false"

for x in food:
     if x.startswith(letter):
         print(x)
         found = "true"

if not found:
    print("not found")
