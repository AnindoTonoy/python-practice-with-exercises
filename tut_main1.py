def print_fun(str):
    return f"The funny joke is:{str}"


def add(num1, num2):
    return num1 + num2 + 10


print("this is normal tut_main1 print.\n")

if __name__ == '__main__':
    print(add(1, 9))
    obj = print_fun("Anindo is a superman")
    print(obj)