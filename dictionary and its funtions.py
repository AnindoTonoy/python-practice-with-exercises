# Dictionary is nothing but key value pair
d1 = {'Anindo': 'Burger',
      'Turjo': 'Rice',
      'Jitu': 'veg',
      'Shawon': {'B': 'meat', 'L': 'Fruit'},
      'Ankit': 'Junk Food',
      45: 'Orange'}

# print(type(d1))
# print(d1)
# # print(d1['Shawon'])

# del d1[45]          # Delete a key and it's value
# print(d1)
# d2 = d1.copy()
# del d1[45]
# d1.update({'Leena': 'Onion'})
print(d1.keys())
print(d1.items())