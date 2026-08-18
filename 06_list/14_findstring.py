""""
find the word starting with the given letter in the list
"""

food = ["pizza","nuggets","hotdog","noodles","pasta","burger"]

letter = input("enter the letter").lower()
for x in food:
     if x.startswith(letter):
         print(x)
