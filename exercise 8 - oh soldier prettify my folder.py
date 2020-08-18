import os


def soldier(path, file_name, file_extension):
    os.chdir(path)

    with open(file_name) as f:
        text = f.read().split("\n")

    # print(text)
    # print(os.listdir())
    i = 1
    for item in os.listdir():

        if item not in text:
            os.rename(item, item.capitalize())

        if item.endswith(file_extension):
            os.rename(item, f'{i}{file_extension}')
            i += 1


if __name__ == '__main__':
    path = input('Give the path name here:')
    file_name = input('Give the file name here:')
    file_extension = input('Give the file extension here:')
    soldier(path, file_name, file_extension)


