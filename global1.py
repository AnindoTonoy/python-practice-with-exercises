# x = 50 #global variable


def function1():
    x = 10

    def function2():
        global x
        # x = 80
    print("before you calling function2", x)
    function2()
    print("before you calling function2", x)


function1()
# print(x)
# function1()
