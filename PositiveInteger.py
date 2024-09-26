def sumPositiveInt(n):
    if n == 0:
        return 0
    else:
        return n + sumPositiveInt(n - 1)


def sumPositiveIntFast(n):
    return sum([i for i in range(1, n + 1)])


print(sumPositiveInt(5))
print(sumPositiveIntFast(5))
