"""
Given:

records = (
    ("Alice", 85),
    ("Bob", 92),
    ("Alice", 85),
    ("Charlie", 78),
    ("Bob", 92),
    ("David", 95)
)

Find the duplicate records and store each duplicate only once.

Expected output
(('Alice', 85), ('Bob', 92))
"""
records = (
    ("Alice", 85),
    ("Bob", 92),
    ("Alice", 85),
    ("Charlie", 78),
    ("Bob", 92),
    ("David", 95)
)

seen = []
duplicates = []
for x in records:
    if x not in seen:
        seen.append(x)
    else:
        if x not in duplicates:
            duplicates.append(x)
print(tuple(duplicates))

