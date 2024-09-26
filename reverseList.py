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


def reserve_list(n):
    if n == 0:
        return []
    else:
        return [n] + reserve_list(n - 1)


def reverse_list_recursive(n):
    if len(n) == 0:
        return []
    else:
        return reverse_list_recursive(n[1:]) + [n[0]]


print(reserve_list(5))
print(reverse_list_recursive(data))
