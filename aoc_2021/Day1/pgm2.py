lst = []

with open('data.txt') as file:
    for line in file:
        lst.append(int(line.rstrip()))

print(lst)
print(len(lst))

count = 0
sum_t = []

for i in range(0,len(lst)-2):
    sum_t.append(lst[i]+lst[i+1]+lst[i+2])

for i in range(1,len(sum_t)):
    if sum_t[i-1] < sum_t[i]:
        count += 1

print(count)
