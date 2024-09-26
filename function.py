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
    5,
]


def count(data, target):
    n = 0
    for i in data:
        if i == target:
            n += 1
    return n


def contains(data, target):
    for i in data:
        if i == target:
            return target
    return False


def scale(data, factor):
    result = []
    for j in range(len(data)):
        result.append(data[j] * factor)
    return result


number = int(input("Enter a number that you want to search "))
result = count(data, number)
contain = contains(data, number)
skala = scale(data, number)
print(f"Scale {skala}")
print(f"The Data contains {contain}")
print(f"The number {number} appears {result} time(s) in the list.")
