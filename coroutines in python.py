# Coroutines in python


def searcher():
    import time
    details = "Hello! I am Anindo. I am a python programmer. I love coding."
    # Some task that will take some times
    time.sleep(4)

    while True:
        text = (yield)
        if text in details:
            print(f'Yes, "{text}" is in the Details.')

        else:
            print(f'Sorry, "{text}" is not in the Details.')


search = searcher()
print('Database is Loading... ')
next(search)
user_input = input('Enter your keywords:')
search.send(user_input)
user_input = input('Enter your keywords:')
search.send(user_input)
search.close()
# Searcher function will stop working here. if you start the function again then it will takes the delay time again.

search = searcher()
print('\nDatabase is Loading for second time...')
next(search)
user_input = input('Enter your keywords:')
search.send(user_input)
user_input = input('Enter your keywords:')
search.send(user_input)
user_input = input('Enter your keywords:')
search.send(user_input)
search.close()