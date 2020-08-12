# args and kwargs - learning


def fun(normal, *args, **kwargs):
    """
    :param normal: Takes normal arguments
    :param args: Takes arguments as tuple
    :param kwargs: Takes arguments as dictionary
    :return: all prints
    """
    print(normal)

    for item in args:
        print(item)

    print("\nNow i want to introduce some heroes:")

    for key, value in kwargs.items():
        print(f"{key} is {value}")


_normal = "The list of students are:"
student_list = {"Anindo", "Harry", "Rohan", "Arpon"}
_speciality = {"Anindo": "Captain", "Harry": "Instructor", "Rohan": "Coordinator", "Arpon": "Cook"}

print(fun.__doc__)
fun(_normal, *student_list, **_speciality)