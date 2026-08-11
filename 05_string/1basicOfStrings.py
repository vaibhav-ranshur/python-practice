"""
What is a String?

A string is a sequence of characters enclosed in quotes.

definition:- A string in Python is an immutable sequence of Unicode characters enclosed in single quotes, double quotes,
or triple quotes. Strings support indexing, slicing, iteration, and many built-in methods for text processing.

s1 = 'Hello'
s2 = "Hello"

Both are strings.

Creating Strings
Single Quotes
s1 = 'Hello'


Double Quotes
s2 = "Hello"


Triple Quotes (Multiline Strings)
s3 = '''Hello
How are you?'''

or
"""
s4 = """Hello
How are you?"""
"""
Used for multiline text.





Quotes Inside Strings

If the string contains a single quote ('), use double quotes:

name = "John's"
print(name)

Output:

John's

❌ Wrong:

name = 'John's'

This gives a SyntaxError because Python thinks the string ends after John.





Strings are Objects

Check the type:

s = "Hello"
print(type(s))

Output:

<class 'str'>



Taking String Input
name = input("Enter a string: ")
print(name)

Input:

welcome

Output:

welcome

input() always returns a string.

Length of a String
Use len().

s = "welcome"
print(len(s))

Output:

7

Characters count:

w e l c o m e
1 2 3 4 5 6 7
Strings are Arrays of Characters
s = "Hello"

Internally:

H   e   l   l   o
0   1   2   3   4

Each character has an index.

Positive Indexing
s = "Hello"

print(s[0])
print(s[1])
print(s[4])

Output:

H
e
o
Negative Indexing

Python also supports indexing from the end.

H   e   l   l   o
-5 -4 -3 -2 -1

Example:

s = "Hello"

print(s[-1])
print(s[-4])

Output:

o
e
Iterating Through a String

Using a for loop:

s = "Hello"

for ch in s:
    print(ch)

Output:

H
e
l
l
o

Here ch gets one character at a time.

Accessing Characters by Index
s = "Hello"

for i in range(len(s)):
    print(s[i])

Output:

H
e
l
l
o
String Immutability (Important Interview Question)

Strings cannot be changed after creation.

❌ Wrong:

s = "Hello"
s[0] = "h"

Output:

TypeError

✅ Correct:

s = "Hello"
s = "hello"

A new string is created.

Quick Summary
s = "Hello"

type(s)      # str
len(s)       # 5
s[0]         # H
s[1]         # e
s[-1]        # o

for ch in s:
    print(ch)
Interview Definition

A string in Python is an immutable sequence of Unicode characters enclosed in single quotes, double quotes, 
or triple quotes. Strings support indexing, slicing, iteration, and many built-in methods for text processing.



"""