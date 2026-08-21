"""
Given:

records = (
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 95),
    ("Eva", 88)
)

Find all students who scored 90 or higher.

Expected output:

Bob 92
David 95
"""
records = (
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 95),
    ("Eva", 88)
)
new_records = []
for name,record in records:
    if record >= 90:
        new_records.append((name,record))
print(tuple(new_records))