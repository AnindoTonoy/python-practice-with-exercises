# open file with block
with open("anindo.txt") as f:
    a = f.readlines()
    print(a)

# open file without with block
f = open("anindo.txt")
a = f.read(10)
print(a)
f.close()