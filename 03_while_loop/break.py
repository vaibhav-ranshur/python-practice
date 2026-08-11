# infinite loop - break -continue - pass

#------------------------------- break statement ---------------------------------------------
""""
infinite loop

while True:
print("hello")                 # this loop will will never stop because condition never false this type of loops called infinite loop


count = 0                     # also this one is infinite loop because we are not updating  count
while count < 10:
    print("hello")


while True:                                   # the block of code inside infinite loop never stop
 n = int(input("Enter a number: "))           # but we need to stop it
 if n > 0:                                    # for that we have break statement
 print("positive number")                     # break is used for stopping the loop at some point
 else:
 print("negative number")")

"""

while True:
    n = int(input("Enter a number: "))

    if n > 0:
        print("positive number")
    elif n < 0:
        print("negative number")
    else:
        break


count = 0
while count < 10:
    print(count)
    count += 1
    if count > 5:
        break

# -------------------------------- continue statement ---------------------------------

count = 0
while count < 10:
    n = int(input("Enter a number: "))
    if n % 3 == 0:                          #if you input number which is divisible by 3 it will not print no
        continue                  # and ask for another no (loop will start not break only no which divisible by 3 not printing)
    print(n)                      # continue statement is used for logic design such as in this example
    count += 1

#-----------------------------------pass statement -----------------------------------------

count = 0
while count < 10:
    n = int(input("Enter a number: "))
    if n % 3 == 0:
        pass                            # do nothing
    else:
     print(n)
     count += 1

# we can write this program in other way
# only the differance if writing the program in different way(only the program definition is change)
count = 0
while count < 10:
    n = int(input("Enter a number: "))
    if n % 3 != 0:
     print(n)
     count += 1
