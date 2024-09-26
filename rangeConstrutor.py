def rangeConstrutor(start, end, step):
    return [i for i in range(start, end, step)]


def rangeConstrutorList(start, end, step):
    return list(range(start, end, step))


def rangeConstrutorListPow(start):
    return list(map(lambda x: 2**x, range(start)))


print(rangeConstrutor(8, -10, -2))
print(rangeConstrutorList(8, -10, -2))
print(rangeConstrutorListPow(9))
