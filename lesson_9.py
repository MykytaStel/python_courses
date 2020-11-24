import os


# === TASK 1 === #
def create(
        file_name: str,
        method: str,
        file_text: any,
        new_file_name: str = '',
        remove: bool = False,
        rename: bool = False,
):
    create_file = open(file_name, method)
    if method == 'w' or method == 'w+':
        create_file.write(file_text)
    elif method == 'a' or method == 'a+':
        create_file.write(f'{file_text}\n')
    elif remove:
        os.remove(file_name)
    elif rename:
        os.rename(file_name, new_file_name)

    create_file.close()


def open_files(file_name):
    open_file = open(file_name, "r")
    content = open_file.read()
    return content


print(create('my-file.txt', 'a+', 'Hell yeah'))
print(open_files('my-file.txt'))
# === TASK 2 === #
