# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]


def Arit(n):
    return [i * (n * 1) for i in range(n)]


print(Arit(10))

# Menggunakan list comprehension untuk menghasilkan list huruf dari a hingga z
alphabet_list = [chr(i) for i in range(ord("a"), ord("z") + 1)]

print(alphabet_list)
