import sys


def count_lines(f):
    return len(f.readlines())


def count_chars(f):
    return len(f.read())


def wc():
    file_name = sys.argv[1]
    with open(file_name) as f:
        total_lines = count_lines(f)
        f.seek(0)
        total_chars = count_chars(f)
        print(total_lines, total_chars)


wc()
