"""
exercise - 4
Print * pattern in by input row
and the boolean type order:
such as-
if true: print 1,2, ... n
if false: print n, .. 2,1
"""

row_num = int(input("input row numbers: "))
inp_num = int(input("input a number 0/1. "
                    "Here 1 = True, 0 = False: "))

inp_bool = bool(inp_num)

if inp_bool:
    for n in range(1, row_num + 1):
        print(n * "*", end="\n")

elif not inp_bool:
    for n in range(row_num):
        print((row_num - n) * "*", end="\n")

# if bool1 == 1:
#     bool1 = bool(True)
#
# elif bool1 == 0:
#     bool1 = bool(False)
#
# if bool1:
#     for n in range(1, num1+1):
#         print(n*"*" + "\n")
#
# elif bool2:
#     for n in range(1, num1+1):
#
#         print(num1 * "*" + "\n")
#         num1 -= 1


# for n in range(num1):
#     print((num1 - n) * "*", end="\n")
