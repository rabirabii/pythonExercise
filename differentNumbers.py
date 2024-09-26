data = [
    1,
    2,
    3,
    4,
    5,
    6,
    6,
    2,
    3,
    6,
    10,
    20,
    12,
    2,
    2,
]


def diffNumbers(sequence):
    unique = list(dict.fromkeys(sequence))
    return unique


print(diffNumbers(data))
