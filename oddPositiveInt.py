def oddPositiveInt(n):
    if n <= 0:
        return 0

    elif (n % 2) == 0:
        return "The Number is Even"
    else:
        return n + oddPositiveInt(n - 2)


def oddPositiveIntSum(n):
    return sum([i for i in range(2, n)])


print(oddPositiveInt(5))
print(oddPositiveIntSum(5))
