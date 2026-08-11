"""
What is an Else Suite?

In Python, an else block can be attached to a loop (while or for).

The else block executes only when the loop finishes normally.

It does not execute if the loop is terminated using break.
"""

count  = 1

while count <= 10:
    print(count)
    count += 1
else:
    print("all numbers 1 to 10 are printed successfully")

"""
Explanation
Loop runs for 1, 2, 3 ....... 10.
Condition becomes false (11 <= 10 is False).
Loop ends normally.
else block executes.
"""

count  = 1

while count <= 10:
    print(count)
    count += 1
    if count > 5:
        break
else:
    print("all numbers 1 to 10 are printed successfully")

"""
Explanation
When count becomes 6, break executes.
Loop stops immediately.
Since loop did not finish normally, else block is skipped.
"""