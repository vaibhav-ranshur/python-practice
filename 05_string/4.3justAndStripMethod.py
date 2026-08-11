"""
Python String Methods


1. just() Methods (Alignment)

Used to align a string within a specified width by adding spaces or a custom character.

syntax:-
ljust(width, fillchar)
Left-aligns the string.

s = "python"

print(s.ljust(10))
# 'python    '

print(s.ljust(10, '*'))
# 'python****'
rjust(width, fillchar)

Right-aligns the string.

print(s.rjust(10))
# '    python'

print(s.rjust(10, '.'))
# '....python'
center(width, fillchar)

Centers the string.

print(s.center(10))
# '  python  '

print(s.center(10, '*'))
# '**python**'

Note:

width = total length of the final string.
fillchar is optional (default is space).




2. strip() Methods (Removing Characters)

Used to remove spaces or specified characters from the beginning/end of a string.

strip()

Removes spaces from both sides.

s = "   python   "

print(s.strip())
# 'python'
lstrip()

Removes spaces from the left side.

print(s.lstrip())
# 'python   '
rstrip()

Removes spaces from the right side.

print(s.rstrip())
# '   python'
Removing Specific Characters
s = "...++aaapython"

print(s.lstrip('.+'))
# 'aaapython'

print(s.lstrip('.+a'))
# 'python'

Important:
strip(chars) removes all matching characters from the ends until a different character is found.
"""