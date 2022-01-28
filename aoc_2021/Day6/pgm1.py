lst = []

with open('data_ex.txt') as file:
    for line in file:
        line = str(line.rstrip())
        lst = line.split(sep=',')

for i in range(len(lst)):
    lst[i] = int(lst[i])

#print(lst)
temp = []
count = 0

for i in range(256):
    for k in range(len(lst)):
        if lst[k] == 0:
            lst[k] = 7
            lst.append(9)
    for j in range(len(lst)):
        lst[j] -= 1
    #print(lst)             

print(len(lst))