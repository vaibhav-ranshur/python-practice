"""
Given:

numbers = (10, 20, 30, 40, 50)

You need to change:

30 → 35

Task
Modify the tuple so the final result becomes:

(10, 20, 35, 40, 50)
"""
numbers = (10, 20, 30, 40, 50)
l1 = list(numbers)
l1[2] = 35
numbers = tuple(l1)
print(numbers)

"tuples are immutable so we cant modify directly so we convert tuple into listthen modify.after modification we convert list into tuple"
