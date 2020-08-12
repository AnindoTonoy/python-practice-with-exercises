# Decorators In Python


def dec1(func1):
    def now_exec():
        print('Executing now...')
        func1()
        print('Executed.')
    return now_exec


@dec1
def who_is_anindo():
    print('Anindo is a good boy.')


@dec1
def who_is_Arpon():
    print('Arpon is a good boy.')


# who_is_anindo = dec1(who_is_anindo) # we can use decorators like this way also
# who_is_Arpon()
who_is_anindo()


def server(func):
    def conce_server():
        print('Server is connecting...')
        func()
        print('Connected.')
    return conce_server


@server
def facebook():
    print('Facebook is running...')


@server
def youtube():
    print('Youtube is running...')


facebook()
youtube()
