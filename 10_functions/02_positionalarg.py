"""
writing a function using positional arguments
"""
def net_sal(basic,allowance,deduction):
    net = basic + allowance - deduction
    return net

n = net_sal(15000,3000,2500)
print(n)
