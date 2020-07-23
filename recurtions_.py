# n! = n * n-1 * n-2 * n-3 * .... 1
# n! = n * (n-1)!
# nth factorial calculation


def iterative_function(n):
    """

    :param n: integer
    :return: n * n-1 * n-2 * n-3 * .... 1
    """
    fac = 1
    for i in range(n):
        fac = fac * (i + 1)
    return fac


def recursive_function(n):
    if n == 1:
        return 1
    else:
        return n * recursive_function(n-1)


def fibonacci_function(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_function(n-1) + fibonacci_function(n-2)


number = int(input("Enter the number: "))
# print("iterative function print", iterative_function(number))
# print("recursive function print", recursive_function(number))
print("fibonacci function print", fibonacci_function(number))
