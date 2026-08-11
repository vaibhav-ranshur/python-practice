# display data in given format (25 letter)
#                productName.........price
#                pizza.................300

"""product = str(input("enter a product name"))
price = input("enter a price")

totalLength = len(product) + len(price)
print(totalLength)
dots = "." * (25 - totalLength)
print(product+dots+price)"""

str = input("enter a string")
num = input("enter a number")

length = len(str) + len(num)
dots = "." * (30-length)
print(str+dots+num)