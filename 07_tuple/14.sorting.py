"""
You have:

records = (
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 95),
    ("Eva", 88)
)

Create a new tuple where the records are sorted by score from highest to lowest.

Expected result:

(
    ("David", 95),
    ("Bob", 92),
    ("Eva", 88),
    ("Alice", 85),
    ("Charlie", 78)
)
"""

records = (
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 95),
    ("Eva", 88)
)

new_records = tuple(sorted(records, key=lambda record: record[1],reverse = True))
print(new_records)