"""
1. capitalize()

Converts the first character to uppercase and the rest to lowercase.

s = "hello dear"
print(s.capitalize())

Output:

Hello dear
2. lower()

Converts all alphabetic characters to lowercase.

s = "HeLLo"
print(s.lower())

Output:

hello
3. upper()

Converts all alphabetic characters to uppercase.

s = "HeLLo"
print(s.upper())

Output:

HELLO
4. title()

Makes the first letter of every word uppercase.

s = "hEllO deAr"
print(s.title())

Output:

Hello Dear
5. swapcase()

Changes uppercase letters to lowercase and lowercase letters to uppercase.

s = "HEllo"
print(s.swapcase())

Output:

heLLO
6. casefold()

Converts a string to lowercase in a more aggressive Unicode-aware way.

s = "HELLO"
print(s.casefold())

Output:

hello
Difference Between lower() and casefold()

Most of the time they produce the same result:

s = "HELLO"

print(s.lower())     # hello
print(s.casefold())  # hello
Special Unicode Characters

German Sharp S (ß):

s = "straße"

print(s.lower())
print(s.casefold())

Output:

straße
strasse
Why?
lower() only converts characters to lowercase.
casefold() is designed for case-insensitive comparisons across different languages.
It performs extra conversions for Unicode characters.
Another Example
s1 = "straße"
s2 = "STRASSE"

print(s1.lower() == s2.lower())
print(s1.casefold() == s2.casefold())

Output:

False
True

So for comparing user input:

username1.casefold() == username2.casefold()

is safer than:

username1.lower() == username2.lower()
Quick Notes (Exam / Interview Revision)
capitalize()
→ First letter uppercase, rest lowercase.

lower()
→ Converts all letters to lowercase.

upper()
→ Converts all letters to uppercase.

title()
→ First letter of each word uppercase.

swapcase()
→ Uppercase ↔ Lowercase.

casefold()
→ Stronger version of lower().
→ Unicode-aware.
→ Best for case-insensitive string comparison.

lower() vs casefold()

lower():
✓ Simple lowercase conversion

casefold():
✓ More aggressive lowercase conversion
✓ Handles Unicode characters
✓ Best for comparisons

Example:
"straße".lower()     → "straße"
"straße".casefold()  → "strasse"
Memory Trick
capitalize() → One word starts with capital
title()      → Every word starts with capital
upper()      → ALL CAPS
lower()      → all small
swapcase()   → Reverse case
casefold()   → lower() + Unicode handling
"""