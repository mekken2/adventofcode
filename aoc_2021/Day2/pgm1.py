lst = []

with open('data.txt') as file:
    for line in file:
        lst.append(line.rstrip())

print(lst)
print(len(lst))

horizontal = 0
depth = 0

for i in lst:
    if 'forward' in i:
        horizontal += int(i[8:])

    if 'up' in i:
        depth -= int(i[3:])

    if 'down' in i:
        depth += int(i[5:])

print(horizontal)
print(depth)
print(horizontal * depth)