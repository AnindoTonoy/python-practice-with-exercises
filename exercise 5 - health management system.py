# 3 clients - Anindo, Harry, Rohan
# Health Management System

import datetime


def get_time():
    """This function return current date and time"""
    return datetime.datetime.now()


def diet_lock(file_name, text):
    """This function return diet lock of the clients"""
    with open(file_name, "a") as f:
        a = f.write(f"{get_time()} - {text} \n")
    return a


def exercise_lock(file_name, text):
    """This function return exercise lock of the clients"""
    with open(file_name, "a") as f:
        a = f.write(f"{get_time()} - {text} \n")
    return a


def diet_retrieve(file_name):
    """This function return retrieve diet of the clients"""
    with open(file_name, "r") as f:
        content = f.read()
    return print(content)


def exercise_retrieve(file_name):
    """This function return retrieve exercise of the clients"""
    with open(file_name, "r") as f:
        content = f.read()
    return print(content)


def lock_take(client_name):
    if client_name == 1:
        print("What you want to Lock?\n"
              "1. Diet\n"
              "2. Exercise\n"
              "(Press 1 for Diet, 2 for Exercise.")
        client_choice = int(input("press: "))

        if client_choice == 1:
            # anindo's diet lock
            f_name = "anindo_diet.txt"
            txt = input("Enter Diet:")
            diet_lock(f_name, txt)
            print("You successfully lock this diet!")

        elif client_choice == 2:
            # anindo's exercise lock
            file_name = "anindo_exercise.txt"
            text = input("Enter Exercise:")
            exercise_lock(file_name, text)
            print("You successfully lock this exercise!")

    elif client_name == 2:
        print("What you want to Lock?\n"
              "1. Diet\n"
              "2. Exercise\n"
              "(Press 1 for Diet, 2 for Exercise.")
        client_choice = int(input("press: "))

        if client_choice == 1:
            # harry's diet lock
            f_name = "harry_diet.txt"
            txt = input("Enter Diet:")
            diet_lock(f_name, txt)
            print("You successfully lock this diet!")

        elif client_choice == 2:
            # harry's exercise lock
            file_name = "harry_exercise.txt"
            text = input("Enter Exercise:")
            exercise_lock(file_name, text)
            print("You successfully lock this exercise!")

    elif client_name == 3:
        print("What you want to Lock?\n"
              "1. Diet\n"
              "2. Exercise\n"
              "(Press 1 for Diet, 2 for Exercise.")
        client_choice = int(input("press: "))

        if client_choice == 1:
            # rohan's diet lock
            f_name = "rohan_diet.txt"
            txt = input("Enter Diet:")
            diet_lock(f_name, txt)
            print("You successfully lock this diet!")

        elif client_choice == 2:
            # rohan's exercise lock
            file_name = "rohan_exercise.txt"
            text = input("Enter Exercise:")
            exercise_lock(file_name, text)
            print("You successfully lock this exercise!")


def retrieve_take(client_name):
    if client_name == 1:
        print("What you want to Retrieve?\n"
              "1. Diet\n"
              "2. Exercise\n"
              "(Press 1 for Diet, 2 for Exercise.")
        client_choice = int(input("press: "))

        if client_choice == 1:
            # anindo's diet Retrieve
            f_name = "anindo_diet.txt"
            diet_retrieve(f_name)

        elif client_choice == 2:
            # anindo's exercise Retrieve
            file_name = "anindo_exercise.txt"
            exercise_retrieve(file_name)

    elif client_name == 2:
        print("What you want to Lock?\n"
              "1. Diet\n"
              "2. Exercise\n"
              "(Press 1 for Diet, 2 for Exercise.")
        client_choice = int(input("press: "))

        if client_choice == 1:
            # harry's diet Retrieve
            f_name = "harry_diet.txt"
            diet_retrieve(f_name)

        elif client_choice == 2:
            # harry's exercise Retrieve
            file_name = "harry_exercise.txt"
            exercise_retrieve(file_name)

    elif client_name == 3:
        print("What you want to Lock?\n"
              "1. Diet\n"
              "2. Exercise\n"
              "(Press 1 for Diet, 2 for Exercise.")
        client_choice = int(input("press: "))

        if client_choice == 1:
            # rohan's diet Retrieve
            f_name = "rohan_diet.txt"
            diet_retrieve(f_name)

        elif client_choice == 2:
            # rohan's exercise Retrieve
            file_name = "rohan_exercise.txt"
            exercise_retrieve(file_name)


print("=============| Health Management System |=============")
print("What you want to do? \n"
      "1. Lock\n"
      "2. Retrieve\n"
      "(Press 1 for Lock, 2 for Retrieve)")

activity_input = int(input("Press: "))

if activity_input == 1:
    print("\n=============| Clients Lists |=============")
    print("Select the Client for Lock.\n"
          "1. Anindo\n"
          "2. Harry\n"
          "3. Rohan\n"
          "(Press 1 for Anindo, 2 for Harry, 3 for Rohan)")

    client_name = int(input("Press: "))

    lock_take(client_name)


elif activity_input == 2:
    print("\n=============| Clients Lists |=============")
    print("Select the Client for Retrieve.\n"
          "1. Anindo\n"
          "2. Harry\n"
          "3. Rohan\n"
          "(Press 1 for Anindo, 2 for Harry, 3 for Rohan)")

    client_name = int(input("Press: "))

    retrieve_take(client_name)
