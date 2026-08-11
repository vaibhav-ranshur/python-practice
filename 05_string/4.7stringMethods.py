"""
1. replace()
Syntax
string.replace(old, new, count)
Purpose

Replaces one substring with another.

Example
text = "I like Java"
print(text.replace("Java", "Python"))

Output

I like Python

If count is given:

text = "apple apple apple"
print(text.replace("apple", "mango", 2))

Output

mango mango apple

Short Note: Replaces occurrences of a substring. count limits how many replacements happen.

2. join()
Syntax
separator.join(iterable)
Purpose

Joins elements of a list, tuple, or other iterable into a single string.

Example
words = ["I", "love", "Python"]
print(" ".join(words))

Output

I love Python

Another example:

print("-".join(words))

Output

I-love-Python

Short Note: Combines multiple strings using a specified separator.

3. split()
Syntax
string.split(sep, maxsplit)
Purpose

Splits a string from left to right.

Example
text = "Python Java C++"
print(text.split())

Output

['Python', 'Java', 'C++']

Using separator:

text = "A,B,C,D"
print(text.split(","))

Output

['A', 'B', 'C', 'D']

Using maxsplit:

text = "one two three four"
print(text.split(" ", 2))

Output

['one', 'two', 'three four']

Short Note: Splits a string into a list from the left.

4. rsplit()
Syntax
string.rsplit(sep, maxsplit)
Purpose

Splits a string from right to left.

Example
text = "one two three four"
print(text.rsplit(" ", 2))

Output

['one two', 'three', 'four']

Short Note: Same as split(), but splitting starts from the right side.

5. splitlines()
Syntax
string.splitlines(keepends=False)
Purpose

Splits a multiline string into separate lines.

Example
text = "Hello\nPython\nWorld"
print(text.splitlines())

Output

['Hello', 'Python', 'World']

With keepends=True:

print(text.splitlines(True))

Output

['Hello\n', 'Python\n', 'World']

Short Note: Splits text at line breaks. keepends=True keeps newline characters.

One-Line Revision Notes
Method	Purpose
replace()	Replace one substring with another.
join()	Join iterable elements into one string.
split()	Split string from left into a list.
rsplit()	Split string from right into a list.
splitlines()	Split multiline string into lines.
Interview Tip
split() → Left to Right
rsplit() → Right to Left
join() → List → String
replace() → Change text
splitlines() → Break multiline text into a list of lines
"""