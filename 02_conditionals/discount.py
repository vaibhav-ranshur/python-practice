#calculate discounted amount 1.amount <= 1000 = 10%, 2.1000<amount<=5000 = 20%, 5000<amount <=10000 = 30% and amount<10000 = 50%

amount = float(input("Enter amount: "))

if amount <= 1000:
    discount = amount * 10 / 100
elif amount <= 5000:
    discount = amount * 20 / 100
elif amount <= 10000:
    discount = amount * 30 / 100
else:
    discount = amount * 50 / 100

dis_amount = amount - discount

print("Discount =", discount)
print("Payable Amount =", dis_amount)