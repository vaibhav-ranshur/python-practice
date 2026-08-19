"""
Consider:

data = (
    "Python",
    [10, 20, 30],
    "Data Engineering"
)
Question

Can you change 20 to 25?

Try to modify it so the final result becomes:

('Python', [10, 25, 30], 'Data Engineering')
"""
data = (
    "Python",
    [10, 20, 30],
    "Data Engineering"
)
data[1][1]= 25
print(data)