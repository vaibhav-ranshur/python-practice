"""
writing function using keyword argument
"""

def net_sal(basic,allowance,deduction):
    net = basic + allowance - deduction
    return net

n = net_sal(basic =16000,deduction =3000,allowance = 2100)
print(n)
