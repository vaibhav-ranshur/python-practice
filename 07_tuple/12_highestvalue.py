"""
Given:

records = (
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 95),
    ("Eva", 88)
)

Each inner tuple contains:

(name, score)
Task

Find and print:

The name of the student with the highest score
The highest score
"""

records = (
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 95),
    ("Eva", 88)
)
highestname = ""
highestscore = 0

for name,score in records:
    if score > highestscore:
        highestscore = score
        highestname = name
print(highestname)
print(highestscore)

"""
for record in records:
    if record[1] > highestscore:
        highestscore = record[1]
        highestname = record[0]
print(highestname)
print(highestscore)
"""
