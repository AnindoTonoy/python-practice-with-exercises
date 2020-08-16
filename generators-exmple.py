# Generator practices
def name(a):
    for i in a:
        yield i


a = 'Anindo'
p = name(a)
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())

# Factorial generator
def factorial_gen(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)

    yield fac
    # return fac


number = int(input('Enter the number:'))
fac = factorial_gen(number)
print(f'\nThe Factorial of {number} is', fac.__next__())

# Fibonacci series


def fibonacci_gen(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a+b


# number = int(input('Enter the number for fibonacci:'))
fib = fibonacci_gen(5)

for i in fib:
    print(i)
