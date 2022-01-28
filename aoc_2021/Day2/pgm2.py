lst = []

with open('data.txt') as file:
    for line in file:
        lst.append(line.rstrip())

print(lst)

horizontal = 0
depth = 0
aim = 0
val = []

for i in lst:
    if 'forward' in i:
        val = i.split()
        horizontal += int(val[1])
        depth += int(val[1])*aim

    if 'down' in i:
        val = i.split()
        aim += int(val[1])

    if 'up' in i:
        val = i.split()
        aim -= int(val[1])

final = horizontal * depth

print(final)