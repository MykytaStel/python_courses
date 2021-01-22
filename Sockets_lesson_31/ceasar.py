def cesar(string):
    alpha = ' abcdefghijklmnopqrstuvwxyz'
    res = []
    print(string)
    for c in string.decode('utf-8'):
        print(c)
        if c == alpha[-1]:
            c = alpha[0]
        r = alpha[alpha.index(c) + 1]
        res.append(r)
    key = ''.join(res)
    return key
