#remove punctuation

s1 = """!@#$%^&*(){}[]<"'"'>?/.,|-_"""
s2 = "[vaibhav_nana@gmail.com]"
s3 = ""

for x in s2:
     if x not in s1:
        s3 += x
print(s3)