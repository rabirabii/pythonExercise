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


def OddNumbers(n):
    if n <= 0:
        return []
    else:
        if (n % 2) == 0:
            return OddNumbers(n - 1)
        else:
            return OddNumbers(n - 1) + [n]


def has_odd_number(n):
    odd_numbers = [x for x in n if x % 2 != 0]
    return len(odd_numbers) >= 2


print(OddNumbers(100))
print(has_odd_number(data))
