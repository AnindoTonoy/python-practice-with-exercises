
def add(a, b):
    return a + b


minus = lambda x, y: x - y  # it's lambda function

print(add(5, 5))
print(minus(10, 5))


# sorting of a list using a function
def a_first(a):
    return a[1]


a = [[5, 15], [2, 6], [1, 2]]
a.sort(key=a_first)
print(a)


# sorting of a list using lambda function also

a = [[5, 15], [2, 6], [1, 2]]
a.sort(key=lambda x: x[1])
print(a)

