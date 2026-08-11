# find date,month and year from date

mydate = input("enter the date in format dd/mm/yyyy")

date = mydate.split("/")
print("date :",date[0])
print("month :",date[1])
print("year :",date[2])