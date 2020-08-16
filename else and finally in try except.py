try:
    f = open("anindo.txt")

except Exception as e:
    print(e)

else:
    print('If except is not running then this will print.')

finally:
    # f.close()
    print('Anyway! Executing this.')

print('This is an important task.')