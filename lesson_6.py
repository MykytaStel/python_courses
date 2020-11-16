# Task - 1 #
user_sentence = input('Enter your sentence ')

words = dict()

for word in user_sentence.split():
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

print(words)

# Task - 2 #

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}


def get_total_price(stocks: dict, price: dict):
    total = 0
    for key, value in stocks.items():
        total += price.get(key, 0) * value

    return total


print(get_total_price(stock, prices))
stock['milk'] = 200
print(get_total_price(stock, prices))

# Task - 3 #

print([(x, x*x) for x in range(10)])
print({str(x): x*x for x in range(10)})
