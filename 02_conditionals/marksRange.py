# check if mark of a subject are within range 0-100

marks = int(input("Enter marks: "))
if marks >= 0 and marks <= 100:           # here we used relational(comparison )operator and logical operator
    print("valid")
else:
    print("invalid")