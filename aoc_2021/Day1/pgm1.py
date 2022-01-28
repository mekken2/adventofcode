lst = []

with open('data.txt') as file:
    for line in file:
        lst.append(int(line.rstrip()))

print(lst)
print(len(lst))

count = 0

for i in range(1,len(lst)):
    if lst[i-1] < lst[i]:
        count += 1

print(count)