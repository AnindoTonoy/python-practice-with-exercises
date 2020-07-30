import time


initial = time.time()
# print(initial)

n = 0
while n < 10:
    print("This is Anindo!")
    time.sleep(1.5)
    # program sleeps here for 1.5 sec
    n += 1

print("while loop ran in", (time.time() - initial), "seconds\n")


initial2 = time.time()
# print(initial2)

for i in range(10):
    print("This is Anindo!")
    time.sleep(1.5)
    # program sleeps here for 1.5 sec

print("for loop ran in", (time.time() - initial2), "seconds\n")


local_time = time.asctime(time.localtime(time.time()))      # Getting formatted time
print("Locl Time and is: ", local_time)
