age = int(input('Enter your age: '))

if age < 7 or age > 100:
    print("Invalid age! input age between 7 to 100.")
    age = int(input("Enter your age again: "))

    if 18 < age < 100:
        print('You can drive.')

    elif age == 18:
        print('You are 18. please come to our office, then we decide.')

    else:
        print('You can not drive.')


"""if else condition checking in list"""
# list1 = [1, 2, 3, 4]
# num = int(input("Enter your num: "))
#
# print(num in list1)
#
# if num in list1:
#     print("Yes! it's in the list.")
#
# else:
#     print("No! it's not in the list.")
