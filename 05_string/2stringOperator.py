"""
String Operators in Python

Python provides several operators that work specifically with strings.

s1 = "Hello"
s2 = "World"
1. Concatenation (+)

Used to join two or more strings.

Syntax
string1 + string2
Example
s1 = "Hello"
s2 = "World"

result = s1 + " " + s2
print(result)

Output:

Hello World
Important

Both operands must be strings.

❌ Wrong

"Hello" + 10

Output:

TypeError

✅ Correct

"Hello" + str(10)

Output:

Hello10
2. Repetition (*)

Used to repeat a string multiple times.

Syntax
string * number
Example
s = "Hi "

print(s * 3)

Output:

Hi Hi Hi

Another example:

print("*" * 10)

Output:

**********
3. Indexing ([])

Used to access individual characters.

s = "Hello"
Positive Indexing
H   e   l   l   o
0   1   2   3   4
print(s[0])
print(s[1])
print(s[4])

Output:

H
e
o
Negative Indexing
H   e   l   l   o
-5 -4 -3 -2 -1
print(s[-1])
print(s[-2])

Output:

o
l
4. Slicing ([:])

Used to extract part of a string.

Syntax
string[start:end]
Start index included
End index excluded
s = "Hello"
Example 1
print(s[1:4])

Output:

ell
Example 2
print(s[:3])

Output:

Hel
Example 3
print(s[2:])

Output:

llo
Example 4
print(s[:])

Output:

Hello
Slicing with Step

Syntax:

string[start:end:step]
s = "HelloWorld"

print(s[::2])

Output:

Hlool

Every second character is selected.

Reverse a String
s = "Hello"

print(s[::-1])

Output:

olleH
5. Membership Operator (in)

Checks whether a character or substring exists.

Syntax
value in string
Example
s = "Hello"

print("e" in s)
print("ll" in s)

Output:

True
True
Example
print("z" in s)

Output:

False
6. Membership Operator (not in)

Checks whether a character or substring does NOT exist.

Syntax
value not in string
Example
s = "Hello"

print("z" not in s)

Output:

True
Example
print("e" not in s)

Output:

False
Complete Example
s = "Hello"

# Concatenation
print(s + " World")

# Repetition
print(s * 2)

# Indexing
print(s[1])

# Slicing
print(s[1:4])

# Membership
print("e" in s)

# Not Membership
print("z" not in s)

Output:

Hello World
HelloHello
e
ell
True
True
Quick Interview Notes
Operator	Purpose	Example
+	Concatenation	"Hi" + "All"
*	Repetition	"Hi" * 3
[]	Indexing	s[0]
[:]	Slicing	s[1:4]
in	Check presence	"e" in "Hello"
not in	Check absence	"z" not in "Hello"
Expected Output Questions
s = "Python"

print(s[1:5])

Output:

ytho
print(s[::-1])

Output:

nohtyP
print("th" in s)

Output:

True

These six operators (+, *, [], [:], in, not in) are the most important string operations you'll use
daily and are commonly asked in Python interviews.
"""