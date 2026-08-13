""""
calculating the salary of weekly working hours(working hours and wage take input from users)
"""

working_hours = [int(x)for x in input("enter the working hours,enter each hours using space").split()]
wage = int(input("enter hourly wage "))

total_hours = sum(working_hours)
total_salary = total_hours*wage
print(total_salary)
