#input marks 90-100 = A,89-75 = B,74-50 = C, below = fail.

marks = int(input("Enter marks: "))

if marks >= 90 and marks <= 100:
    print("A")
elif marks >=75 and marks <= 89:
    print("B")
elif marks >= 50 and  marks <= 74:
    print("C")
else:
    print("fail")