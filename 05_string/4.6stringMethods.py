"""
1. startswith()

Checks if a string starts with a specified prefix.

Syntax
s.startswith(prefix, start, end)
Example
s = "python is very easy"

print(s.startswith("python"))   # True
print(s.startswith("is", 7))    # True
2. endswith()

Checks if a string ends with a specified suffix.

Syntax
s.endswith(suffix, start, end)
Example
s = "python is very easy"

print(s.endswith("easy"))   # True
print(s.endswith("python")) # False
3. removesuffix()

Removes the given suffix if it exists.

Syntax
s.removesuffix(suffix)
Example
s = "hello.py"

print(s.removesuffix(".py"))
# hello

If suffix is not present, original string is returned.

4. removeprefix()

Removes the given prefix if it exists.

Syntax
s.removeprefix(prefix)
Example
s = "Mr.John"

print(s.removeprefix("Mr."))
# John
5. partition()

Splits the string into 3 parts using the first occurrence of the separator.

Syntax
s.partition(sep)
Example
s = "python is very easy"

print(s.partition("is"))
Output
('python ', 'is', ' very easy')

Return value:

(before_separator, separator, after_separator)
6. rpartition()

Same as partition(), but searches from the right side (last occurrence).

Example
s = "one-two-three"

print(s.rpartition("-"))
Output
('one-two', '-', 'three')
Quick Interview Notes
Method	Purpose
startswith()	Checks beginning of string
endswith()	Checks ending of string
removeprefix()	Removes prefix if present
removesuffix()	Removes suffix if present
partition()	Split at first occurrence
rpartition()	Split at last occurrence
Easy Memory Trick
startswith → Beginning check
endswith → Ending check
removeprefix → Remove from front
removesuffix → Remove from back
partition → First occurrence split
rpartition → Last occurrence split
"""