# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [ a , b , c , ..., z ], but without having to type all 26 such
# characters literally.


def AlphabetList():
    return [chr(i) for i in range(ord("a"), ord("z") + 1)]


print(AlphabetList())
