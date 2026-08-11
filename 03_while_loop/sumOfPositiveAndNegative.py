# find sum of positive and negative numbers.

numbers = int(input("enter the numbers of number you want to add"))
counter = 1
NegativeSum = 0
PositiveSum = 0

while counter <= numbers:
  n = int(input("enter the number you want to add"))
  counter += 1
  if n >= 0:
     PositiveSum+= n
  else:
      NegativeSum += n

sum = PositiveSum + NegativeSum
print("sum =",sum)
