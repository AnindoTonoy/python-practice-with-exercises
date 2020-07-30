list1 = ["Rice", "Potato", "Garlik", "Onion", "Apple", "Noodles"]

# printing odd number of index and item
for index, item in enumerate(list1):
    if index % 2 == 1:
        print(index, item)


obj1 = enumerate(list1)
print("Type of obj:", type(obj1))

# printing index and item of list1 in a list
print(list(enumerate(list1)))
