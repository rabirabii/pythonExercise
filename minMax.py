data = [
    9,
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
    5,
]


def minMax(data):
    maxMin = [data[0], data[0]]
    for i in data:
        if i > maxMin[0]:
            maxMin[0] = i
        if i < maxMin[1]:
            maxMin[1] = i
    return maxMin


print(minMax(data))
