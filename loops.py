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
j = 0
while j < len(data) and data[j]:
    j += 1

total = 0
for val in data:
    total += val

biggest = data[0]
for val in data:
    if val > biggest:
        biggest = val

target = int(input("Enter the Data you want to search: "))
found = False
for i in data:
    if i == target:
        found = True
        break
if found:
    print(f"Target {target} found in data!")
else:
    print(f"Target {target} not found in data.")

print(j)
print(total)
print(biggest)
