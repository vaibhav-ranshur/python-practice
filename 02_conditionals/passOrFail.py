# check if student has passed or failed by taking marks in 3 subjects

english = int(input("Enter English marks: "))
math = int(input("Enter Math marks: "))
chemistry = int(input("Enter Chemistry marks: "))
percentage = ((math+english+chemistry)/300)*100
print("your percentage is: ", percentage)
if percentage <= 37:
    print("failed")
else:
    print("pass")

    # or

english = int(input("Enter English marks: "))
math = int(input("Enter Math marks: "))
chemistry = int(input("Enter Chemistry marks: "))
if chemistry >= 45 and math >= 45 and english >= 45:
    print("pass")
else:
    print("failed")