import random

data = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    20,
    12,
]


def choice(data):
    index = random.randrange(0, len(data))
    return data[index]


print(choice(data))
