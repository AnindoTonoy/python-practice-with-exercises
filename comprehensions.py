# list comprehension

ls = [i for i in range(1, 10) if i%2 == 0]
print(ls)

# dictionary comprehension

dict1 = {i : f'Item {i}' for i in range(100) if i%10 == 0}
dict2 = {value:key for key, value in dict1.items()}
print(dict2)
print(dict1)

# set comprehension

dresses = {dress for dress in ['dress1', 'dress2', 'dress1',
                               'dress2', 'dress1', 'dress2']}
print(dresses)
print(type(dresses))

# Generator comprehension

evens = (i for i in range(10) if i%2 == 0)
print(type(evens))

for item in evens:
    print(item)

# Exercise
user_input = eval(input('Enter how many items you want: '))
user_choice = eval(input('Press\n'
                         '1 for List Comprehension\n'
                         '2 for Dictionary Comprehension\n'
                         '3 for Set Comprehension\n'))

if user_choice == 1:
    list1 = ['I am a good programmer' for i in range(user_input)]
    print(list1)

if user_choice == 2:
    dict1 = {i: 'I am a awesome programmer' for i in range(user_input)}
    print(dict1)

if user_choice == 3:
    set1 = {"you are the best programmer" for i in range(user_input)}
    print(set1)