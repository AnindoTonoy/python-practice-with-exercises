# print the sorted list from the given list, in which the list item
# is numeric and grater than equal 6

list1 = ["Anindo", 2, 10, 9, 52, 8, "Harry", "Marie", 98, 3, 200, 7, 6]
new_list = []

for item in list1:
    if str(item).isnumeric() and item >= 6:
        new_list.append(item)

new_list.sort()
print(new_list)


# enter a number greater than 100
# while (True):
#     inp = int(input("Enter a number\n"))
#     if inp < 100:
#         print("Try again!\n")
#         continue
#     else:
#         print("Congrats you entered a number greater than 100")
#         break
