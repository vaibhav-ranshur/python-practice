number = int(input("Enter a number: "))
rev = 0
while number > 0:
    r = number % 10
    number = number // 10
    rev = rev*10+r
#indentation is important for know why just remove empty space (move print statement parallel to line 6) and compare result with and without indentation.
print("the reverse of the number is",rev)

