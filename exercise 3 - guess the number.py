# Exercise 3 - Guess The Number

my_num = 18
no_of_guess = 1

print("You can guess 5 times total")

while no_of_guess <= 5:
    num = int(input("Guess a number:\n"))
    if num > my_num:
        print(f"Guess a lesser number than {num}.")

    elif num < my_num:
        print(f"Guess a greater number than {num}.")

    else:
        print("You Won!")
        print("You enter the correct number")
        break

    print(5 - no_of_guess, "no. of guesses left in 5 \n")
    no_of_guess = no_of_guess + 1

if no_of_guess > 5:
    print("you lose! Game Over.")

