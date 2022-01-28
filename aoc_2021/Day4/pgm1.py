lst = []

with open('data.txt') as file:
    for line in file:
        lst.append(line.rstrip())

puzzle_input = lst[0]
puzzle_input = puzzle_input.split(',')
boards = []
temp = []

for i in range(2,len(lst)):
    if lst[i] == '':
        boards.append(temp)
        temp = []
    else:
        temp.append(lst[i].split())

#print(boards)
print(puzzle_input)

mark = []
unmark = []
count_r = 0
count_c = 0

for i in puzzle_input:
    for j in boards:
        for k in j:
            if k == i:
                if i not in mark:
                    mark.append(i)
                count_r += 1
                if count_r == 5:
                    res = j
    for j in boards:
        for k in j:
            if k[0] == i:
                if i not in mark:
                    mark.append(i)
                count_c += 1
                if count_c == 5:
                    res = j


print(res)
print(mark)