"""
# String Methods in Python – Short Notes

## What are String Methods?

String methods are **built-in functions** that perform operations on strings.

A string is an object of the `str` class.



```python
s = "hello"

print(type(s))
# <class 'str'>
```

Methods help us manipulate, search, modify, and validate strings.

---




## How to View String Methods

### Using `dir()`

```python
dir(str)
```

Displays all methods available for strings.

Example output contains:

```python
capitalize()
upper()
lower()
find()
replace()
split()
join()
startswith()
endswith()
strip()
```

---




## How to Get Help About a Method

### Using `help()`

```python
s = "hello"

help(s.endswith)
```

or

```python
help(str.endswith)
```

Shows:

* Purpose
* Syntax
* Parameters
* Return type

---





# Common String Methods

## 1. upper()

Converts all characters to uppercase.

```python
s = "hello"

print(s.upper())
```

Output:

```python
HELLO
```

---

## 2. lower()

Converts all characters to lowercase.

```python
s = "HELLO"

print(s.lower())
```

Output:

```python
hello
```

---

## 3. capitalize()

Makes the first character uppercase.

```python
s = "python"

print(s.capitalize())
```

Output:

```python
Python
```

---

## 4. title()

Converts the first letter of each word to uppercase.

```python
s = "hello world"

print(s.title())
```

Output:

```python
Hello World
```

---

## 5. swapcase()

Changes uppercase to lowercase and vice versa.

```python
s = "PyThOn"

print(s.swapcase())
```

Output:

```python
pYtHoN
```

---

## 6. find()

Finds the position of a substring.

```python
s = "hello"

print(s.find("l"))
```

Output:

```python
2
```

If not found:

```python
print(s.find("z"))
```

Output:

```python
-1
```

---

## 7. replace()

Replaces one substring with another.

```python
s = "hello"

print(s.replace("hello", "hi"))
```

Output:

```python
hi
```

---

## 8. startswith()

Checks whether a string starts with a given value.

```python
s = "python"

print(s.startswith("py"))
```

Output:

```python
True
```

---

## 9. endswith()

Checks whether a string ends with a given value.

```python
s = "python"

print(s.endswith("on"))
```

Output:

```python
True
```

---

## 10. split()

Splits a string into a list.

```python
s = "Python Java C++"

print(s.split())
```

Output:

```python
['Python', 'Java', 'C++']
```

---

## 11. join()

Joins list elements into a string.

```python
languages = ["Python", "Java", "C++"]

print("-".join(languages))
```

Output:

```python
Python-Java-C++
```

---

## 12. strip()

Removes spaces from both ends.

```python
s = "  hello  "

print(s.strip())
```

Output:

```python
hello
```

---

## 13. isalpha()

Checks whether all characters are alphabets.

```python
print("Python".isalpha())
```

Output:

```python
True
```

---

## 14. isdigit()

Checks whether all characters are digits.

```python
print("123".isdigit())
```

Output:

```python
True
```

---

## 15. isalnum()

Checks whether all characters are alphabets or digits.

```python
print("Python123".isalnum())
```

Output:

```python
True
```

---

# Quick Revision Table

| Method         | Purpose                     |
| -------------- | --------------------------- |
| `upper()`      | Convert to uppercase        |
| `lower()`      | Convert to lowercase        |
| `capitalize()` | First letter uppercase      |
| `title()`      | Every word starts uppercase |
| `swapcase()`   | Reverse letter cases        |
| `find()`       | Find substring index        |
| `replace()`    | Replace text                |
| `startswith()` | Check starting text         |
| `endswith()`   | Check ending text           |
| `split()`      | Convert string to list      |
| `join()`       | Convert list to string      |
| `strip()`      | Remove spaces               |
| `isalpha()`    | Only letters                |
| `isdigit()`    | Only digits                 |
| `isalnum()`    | Letters + digits            |

# Interview One-Liner

**String methods are built-in functions of the `str` class used to search, modify, validate, and manipulate
string data efficiently.**

"""