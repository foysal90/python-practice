def addition(a,b):
    c = a + b
    print(c)

addition(5,2)


def calculator(x,y):


    c = x + y
    d = x - y
    e = x * y
    f = x / y
    return c,d,e,f


sum, sub, mul, div = calculator(15,5)
print('Sum:', sum, 'sub:', sub, 'Multiplication:', mul, 'divided:', div)