f = open("anindo.txt")

# print(f.readline(), end="")
# print(f.tell())
# print(f.readline())
# print(f.tell())

f.seek(58)
print(f.tell())
print(f.readline(), end="\n")

f.seek(0)
print(f.tell())
print(f.readline(), end="")
print(f.readline(), end="")
print(f.readline(), end="")
print(f.tell())

f.close()