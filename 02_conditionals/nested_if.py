# check exam results.conditions: 1. attendance must be 75% 2.marks must be 35.  output: 1.pass 2.fail

attendance = int(input("Enter your attendance: "))
marks = int(input("Enter your marks: "))

if attendance >= 75:
    if marks >= 35:
       print("pass")
    else:
       print("fail")

# if you enter attendance less than 75 it gives no output
# because when you entered attendance less than 75 the outer block never executes
# and when outer block not execute it stop execution for inner block

attendance = 75
marks = int(input("Enter your marks: "))

if attendance >= 75:
    if marks >= 35:
       print("pass")
    else:
       print("fail")
