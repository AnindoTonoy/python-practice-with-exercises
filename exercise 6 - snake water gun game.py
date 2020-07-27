# Exercise - 6
# Snake | Water | Gun - Game


import random

print("\n------ Snake | Water | Gun ------\n")
print("Total chances are: 10\n")

lst = ["S", "W", "G"]

n = 1
com_score = 0               # Computer's score for count
user_score = 0              # User's score for count
both_same = 0               # Both's score for count

while n <= 10:
    inp = input("S - for Snake, W - for Water, G - for Gun\nEnter you input: ")
    user_input = inp.capitalize()
    com_choice = random.choice(lst)

    c = 0
    u = 0
    b = 0

    # 1
    if com_choice == "S" and user_input == "W":
        print(">> Computer Win!")
        c = 1

    elif com_choice == "S" and user_input == "G":
        print(">> You win!")
        u = 1

    elif com_choice == "S" and user_input == "S":
        print("Both are same choice!")
        b = 1

    # 2
    elif com_choice == "W" and user_input == "S":
        print(">> You win!")
        u = 1

    elif com_choice == "W" and user_input == "W":
        print("Both are same choice!")
        b = 1

    elif com_choice == "W" and user_input == "G":
        print(">> Computer win!")
        c = 1

    # 3
    elif com_choice == "G" and user_input == "S":
        print(">> Computer win!")
        c = 1

    elif com_choice == "G" and user_input == "W":
        print(">> You win!")
        u = 1

    elif com_choice == "G" and user_input == "G":
        print("Both are same choice!")
        b = 1

    else:
        print(f"Invalid input! your input is - '{inp}'. Please Enter input as S or W or G to continue.")

    print(f"Chances left {10 - n}.\n")

    if c == 1:
        com_score += 1

    elif u == 1:
        user_score += 1

    elif b == 1:
        both_same += 1

    n += 1

print("=================================================================================")
print("\t\t\t\t\tGame Over!")

if com_score < user_score:
    print("\t\t\t\t\tYou are the winner!")

elif com_score > user_score:
    print("\t\t\t\t\tComputer is the Winner!")

elif com_score == user_score:
    print("\t\t\t\t\tMatch Draw!")

else:
    print(f"\t\t\t\t\tChoices are same {both_same} times")

print(f"\t\t\t\t\t- Your total score: {user_score}/10")
print(f"\t\t\t\t\t- Computer's total score {com_score}/10")
print(f"\t\t\t\t\t- Your and Computer's choices are same {both_same}/10 times.")
print("=================================================================================")
