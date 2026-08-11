# match case
from unittest import case
"""
match-case is a structural pattern matching feature introduced in Python 3.10 that allows matching 
values and data structures against patterns, providing a more readable and powerful alternative to 
long if-elif-else chains.

Use it when:

1,There are many possible values to check.
2.You need to match complex data structures (lists, tuples, dictionaries).
3.Code becomes cleaner than long if-elif-else chains.

Avoid it when:

You only have 2–3 simple conditions.
"""

day = int (input ("Enter a day: "))

match day:
    case 1:
        print ("sunday")
    case 2:
        print ("monday")
    case 3:
        print ("tuesday")
    case 4:
        print ("wednesday")
    case 5:
        print ("thursday")
    case 6:
        print ("friday")
    case 7:
        print ("saturday")
    case _:
        print ("holiday")


