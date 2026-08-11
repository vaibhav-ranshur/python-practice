"""
Python String Inquiry Methods

Inquiry methods are used to check properties of a string. They return:

True

or

False




1. isupper()

Checks whether all letters are uppercase.

s = "HELLO"
print(s.isupper())

Output:

True

Example:

"Hello".isupper()

Output:

False




2. islower()

Checks whether all letters are lowercase.

s = "hello"
print(s.islower())

Output:

True

Example:

"Hello".islower()

Output:

False




3. istitle()

Checks whether every word starts with a capital letter.

s = "Hello Dear"
print(s.istitle())

Output:

True

Example:

"hello Dear".istitle()

Output:

False




4. isalnum()

Checks whether string contains only letters and numbers.

(Alpha + Numeric)

"abc123".isalnum()

Output:

True

Example:

"abc 123".isalnum()

Output:

False

(space not allowed)





5. isalpha()

Checks whether string contains only letters.

"Python".isalpha()

Output:

True

Example:

"Python123".isalpha()

Output:

False






6. isspace()

Checks whether string contains only whitespace characters.

"   ".isspace()

Output:

True

Example:

" hello ".isspace()

Output:

False

Whitespace includes:

" "     # Space
"\t"    # Tab
"\n"    # New Line






7. isascii()

Checks whether all characters belong to the ASCII character set.

"Hello".isascii()

Output:

True

Example:

"हेलो".isascii()

Output:

False







8. isidentifier()

Checks whether a string is a valid Python variable name.

"name".isidentifier()

Output:

True

Example:

"123name".isidentifier()

Output:

False

Valid identifiers:

name
_name
student1

Invalid identifiers:

1name
my-name
class

(Note: class.isidentifier() returns True syntactically, but it is a Python keyword and cannot be used as a variable.)





9. isprintable()

Checks whether all characters can be printed.

"Hello".isprintable()

Output:

True

Example:

"Hello\n".isprintable()

Output:

False

because \n is not printable.






10. isdecimal()

Checks whether all characters are decimal digits (0–9).

"123".isdecimal()

Output:

True

Example:

"12.3".isdecimal()

Output:

False






11. isdigit()

Checks whether all characters are digits.

"123".isdigit()

Output:

True

Example:

"12²".isdigit()

Output:

True

Superscript digits are considered digits.






12. isnumeric()

Checks whether all characters are numeric values.

"123".isnumeric()

Output:

True

Example:

"Ⅳ".isnumeric()

Output:

True

(Roman numeral 4)





Difference: isdecimal vs isdigit vs isnumeric
isdecimal()  ⊂  isdigit()  ⊂  isnumeric()
Example Table
String	isdecimal	isdigit	isnumeric
"123"	True	True	True
"12²"	False	True	True
"Ⅳ"	False	False	True
Memory Trick
isdecimal()
→ Only normal digits (0-9)

isdigit()
→ Decimal + superscript digits

isnumeric()
→ Digits + fractions + Roman numerals + all numeric symbols






Quick Revision Notes (
isupper()

→ All letters uppercase?

islower()
→ All letters lowercase?

istitle()
→ Every word starts with capital letter?

isalnum()
→ Only letters and numbers?

isalpha()
→ Only letters?

isspace()
→ Only spaces/tabs/newlines?

isascii()
→ Only ASCII characters?

isidentifier()
→ Valid Python variable name?

isprintable()
→ Printable characters only?

isdecimal()
→ Only decimal digits (0-9)?

isdigit()
→ Digits including superscripts?

isnumeric()
→ Any numeric character?
Most Important Interview Question
isdecimal() ⊂ isdigit() ⊂ isnumeric()

Smallest → Largest

isdecimal -> only 0-9
isdigit -> 0-9 + superscripts
isnumeric -> digits + fractions + Roman numerals

This hierarchy is asked very frequently in Python interviews and MCQs.
"""