def is_multiple(n, m):
    while n > 0:
        n = n - m
    if n == 0:
        return True
    else:
        return False


# def is_multiple(n, m):
#     if m == 0:
#         raise ValueError("m cannot be 0")

#     n = abs(n)
#     m = abs(m)
#     while n > 0:
#         n -= m
#     return n == 0


# print(is_multiple(9, 3))

print(is_multiple(9, 3))
