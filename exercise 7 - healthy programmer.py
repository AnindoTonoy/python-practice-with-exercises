# Healthy programmer

# 9.00 am - 5.00pm
# Water - water.mp3 (3.5 litres)- for stop the music type - Done - then save this as log
# Eyes - eyes.mp3 - play every 30 mins - for stop the music type - Eydone - then save this as log
# Physical activity - physical.mp3 - play every 45 mins - for stop the music type - Exdone - then save this as log

# Rules - use pygame module to play the music

# -------------------------------------------------------------------------------------------------------------------
from pygame import mixer
import threading
import datetime
import time


def get_time():
    return datetime.datetime.now()


def drink_water_log(text):
    """
    This the function for record and append the log
    :param text: as input Drank
    :return: appended text file
    """
    with open("logs/water-drank-log.txt", "a") as f:
        a = f.write(f"{get_time()} - {text}\n")
        return a


def eye_exercise_log(text):
    """
    This the function for record and append the log
    :param text: as input Eydone
    :return: appended text file
    """
    with open("logs/eye-exercise-log.txt", "a") as f:
        a = f.write(f"{get_time()} - {text}\n")
        return a


def physical_exercise_log(text):
    """
    This the function for record and append the log
    :param text: as input Eydone
    :return: appended text file
    """
    with open("logs/physical-exercise-log.txt", "a") as f:
        a = f.write(f"{get_time()} - {text}\n")
        return a


# function for read the drink water log
def read_water_log():
    """
    This the function for record and append the log
    :return: show the text file
    """
    with open("logs/water-drank-log.txt", "r") as f:
        a = f.read()
        return print(a)


# function for read the eye exercise log
def read_eye_log():
    """
    This the function for record and append the log
    :return: read the text file
    """
    with open("logs/eye-exercise-log.txt", "r") as f:
        a = f.read()
        return print(a)


# function for read the physical exercise log
def read_physical_log():
    """
    This the function for record and append the log
    :return: read the text file
    """
    with open("logs/physical-exercise-log.txt", "r") as f:
        a = f.read()
        return print(a)


# function for count time and play music for drinking water
def drink_water():
    while True:
        print('Water drinking counting is running ...')
        time.sleep(1680)

        # Starting the mixer
        mixer.init()

        # Loading the song
        mixer.music.load("music/water.mp3")

        # Setting the volume
        mixer.music.set_volume(0.5)

        # # Start playing the song
        mixer.music.play()

        # Start playing the song
        # mixer.music.play()

        user_input = input("Dear Programmer,\nPlease Drink a glass of water.\n"
                           "Type 'Drank' to stop the music:\n")
        query = user_input.capitalize()

        if query == 'Drank':
            # Stop the mixer
            mixer.music.stop()
            drink_water_log(query)
            print('Thank you. Your water drinking log is updated.\n'
                  '-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n')
        continue


# function for count time and play music for Eye exercising
def eye_exe():
    while True:
        print('Eyes exercising counting is running ...')
        time.sleep(2100)

        # Starting the mixer
        mixer.init()

        # Loading the song
        mixer.music.load("music/eyes.mp3")

        # Setting the volume
        mixer.music.set_volume(0.5)

        # # Start playing the song
        mixer.music.play()

        user_input = input("Dear Programmer,\nPlease Rest yours Eyes.\n"
                           "Type 'Eyedone' to stop the music:\n")
        query = user_input.capitalize()

        if query == 'Eyedone':
            # Stop the mixer
            mixer.music.stop()
            eye_exercise_log(query)
            print('Thank you. Your Eyes resting log is updated.\n'
                  'The next reminder for eye rest after 30 mins.\n'
                  '-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n')
        continue


# function for count time and play music for physical exercising
def physical_exe():
    while True:
        print('Full-body exercising counting is running ...')
        time.sleep(2700)

        # Starting the mixer
        mixer.init()

        # Loading the song
        mixer.music.load("music/physical.mp3")

        # Setting the volume
        mixer.music.set_volume(0.5)

        # # Start playing the song
        mixer.music.play()

        user_input = input("Dear Programmer,\nPlease do some exercise as you are sitting for a long.\n"
                           "Type 'Exdone' to stop the music:\n")
        query = user_input.capitalize()

        if query == 'Exdone':
            # Stop the mixer
            mixer.music.stop()

            physical_exercise_log(query)
            print('Thank you. Your Eyes resting log is updated.\n'
                  'The next reminder for eye rest after 30 mins.\n'
                  '-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n')
        continue


if __name__ == '__main__':
    print("\n\t\t\t\t\t------| Healthy Programmer |------")
    print('\nYou want to read the previous log files or run the "Healthy Programmer" program?\n'
          'if cheak the previous files press "1"\nor Run the program press "2"\n')

    user_choice = input('Press the key: ')
    if user_choice == '1':
        read_choice = input("\nPress 1 for check the water drank logs\nPress 2 for check the eyes exercised logs\n"
                            "Press 3 for check the physical exercised logs\nPress the key: ")

        if read_choice == '1':
            read_water_log()

        elif read_choice == '2':
            read_eye_log()

        elif read_choice == '3':
            read_physical_log()

    elif user_choice == '2':
        # targeting the threads
        t1 = threading.Thread(target=drink_water)
        t2 = threading.Thread(target=eye_exe)
        t3 = threading.Thread(target=physical_exe)

        # starting the threads
        t1.start()
        t2.start()
        t3.start()

        # join the threads
        t1.join()
        t2.join()
        t3.join()
