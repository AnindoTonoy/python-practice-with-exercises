"""
Exercise 2: Faulty Calculator
Design a calculator which will correctly solve all the problem except
the following ones:
45 * 3 = 555, 56 + 9 = 77, 56 / 2 = 4
Your program should take operator and two numbers as inputs and the return
the result
"""

# Taking inputs from user for calculate two number:
operator = input("Enter your arithmetic operator such as (+ or - or * or / ): ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# assign operators as strings for compering between input operator in conditions
add = '+'
sub = '-'
mul = '*'
div = '/'

# faulty operational conditions and correct calculation
if operator == add:
    if num1 == 56 and num2 == 9:
        print(f"Result of {num1} + {num2} = 77")

    else:
        print(f"Result of {num1} + {num2} =", num1 + num2)

elif operator == sub:
    print(f"Result of {num1} - {num2} =", num1 - num2)

elif operator == mul:
    if num1 == 45 and num2 == 3:
        print(f"Result of {num1} * {num2} = 555")

    else:
        print(f"Result of {num1} * {num2} =", num1 * num2)

elif operator == div:
    if num1 == 56 and num2 == 6:
        print(f"Result of {num1} / {num2} = 4")

    else:
        print(f"Result of {num1} / {num2} =", num1 * num2)
