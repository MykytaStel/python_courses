# === TASK 1 === #

create_file = open("my-file.txt", "a+")
create_file.write("Hello world\n")
create_file.close()

open_file = open("my-file.txt", "r")

content = open_file.read()

print(content)

# === TASK 2 === #

