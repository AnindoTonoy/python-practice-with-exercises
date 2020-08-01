# ----------------------------------MAP----------------------------------------


numbers = ["1", "2", "3", "4"]

# Converting strings of numbers list into a int using for loop
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

print("Numbers as int: ", list(numbers))
print(type(numbers[2]))
numbers[2] = numbers[2] + 1
print("Adding using for loop:", numbers[2])

# Converting strings of numbers list[] into a int using map function
list1 = list(map(int, numbers))
list1[2] = list1[2] + 1
print("Adding using map function:", list1[2])


# Converting strings of numbers str_num[] into a square of int() using map and lambda function
str_num = ['1', '2', '3', '4']
# num[0] = num[0] + 1
# print(type(num))
# print(num[0])
num = list(map(int, str_num))

square = list(map(lambda x: x * x, num))
print("\nSquare of str_num list:", square)

# map function


def square(a):
    return a*a


def cube(a):
    return a*a*a


l1 = [square, cube]
for i in range(5):
    val = list(map(lambda x: x(i), l1))
    print(val)


# ----------------------------------FILTER----------------------------------------

lis1 = [1, 2, 5, 1, 2, 8, 1, 7, 11, 3, 0]
lis2 = ['1', '90', '2', '40', '30']


def is_grater_5(num):
    return 5 < num


value = list(filter(is_grater_5, lis1))
print("Grater than 5 of List1", value)

# Converted from list of strings into int and sorted them
lis3 = list(map(int, lis2))
value2 = list(filter(is_grater_5, lis3))
value2.sort()
print("sorted list of int of lis2:", value2)


# ----------------------------------REDUCE----------------------------------------


from functools import reduce

list_10 = [1, 2, 3, 4, 5]

num_all = reduce(lambda x,y: x+y, list_10)
print("Sum of List_10:",num_all)


