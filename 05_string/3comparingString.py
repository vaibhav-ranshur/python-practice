"""
1. What is String Comparison?

String comparison means checking whether two strings are equal, different, or which one comes first alphabetically.

Python compares strings character by character using their Unicode (ASCII) values.

2. Relational Operators Used
Operator	Meaning
==	Equal to
!=	Not equal to
<	Less than
>	Greater than
<=	Less than or equal to
>=	Greater than or equal to
3. Examples
Equality Comparison
s1 = "abcde"
s2 = "abcde"

print(s1 == s2)   # True
print(s1 != s2)   # False
Alphabetical Comparison
s1 = "Alaska"
s2 = "Canada"

print(s1 < s2)    # True

Why?

First character of "Alaska" = A → ASCII 65
First character of "Canada" = C → ASCII 67

Since 65 < 67, "Alaska" < "Canada".

Uppercase vs Lowercase
s1 = "Alaska"
s2 = "alaska"

print(s1 < s2)    # True

Because:

A = 65
a = 97

Uppercase letters have smaller ASCII values than lowercase letters.

Difference at Last Character
s1 = "abcde"
s2 = "abcdf"

print(s1 < s2)    # True

Comparison:

a = a
b = b
c = c
d = d
e < f

Therefore s1 < s2.

4. Important Rules

✅ Comparison starts from the first character.

✅ If characters are equal, Python checks the next character.

✅ Comparison stops when a difference is found.

✅ Uppercase and lowercase letters have different ASCII values.

✅ Strings are compared lexicographically (dictionary order).

Quick Revision
"abc" == "abc"    # True
"abc" != "xyz"    # True
"apple" < "banana"  # True
"zebra" > "apple"   # True
"A" < "a"          # True


Interview One-Liner
Python compares strings lexicographically (dictionary order) by comparing the Unicode/ASCII value of characters from
left to right until a difference is found.
"""