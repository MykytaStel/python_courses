def caesar(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        print(char)
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result
