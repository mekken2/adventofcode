from os import sep


val1 = ''
lst = []
table = []
temp = []

with open('data_ex.txt') as file:
    i = -1
    for line in file:
        i += 1
        temp = []
        #print(line.rstrip())
        lst.append(str(line.rstrip()))
        val1 = lst[i]
        val1 = val1[0:val1.index('-')-1]
        val1 = val1.split(sep=',')
        #print(val1)
        val2 = lst[i]
        val2 = val2[val2.index('>')+1:]
        val2 = val2.split(sep=',')
        #print(val2)
        temp.append(val1)
        temp.append(val2)
        table.append(temp)

print(table)

temp = []
res_table = []

max_x2 = 0
max_y2 = 0
for i in table:
    x1 = int(i[0][0].rstrip())
    y1 = int(i[0][1].rstrip())
    x2 = int(i[1][0].rstrip())
    y2 = int(i[1][1].rstrip())

    if max_x2 < x2:
        max_x2 = x2

    if max_y2 < y2:
        max_y2 = y2

    if x1 == x2 or y1 == y2:
        if x1 == x2:
            if y1 > y2:
                for i in range(y1-y2):
                    temp.append(x1)
                    temp.append(y2+i)
                    res_table.append(temp)
                    temp = []
            else:
                for i in range(y2-y1):
                    temp.append(x1)
                    temp.append(y1+i)
                    res_table.append(temp)
                    temp = []
    
print(res_table)
temp = []

dict_val = {}
for i in range(max_x2):
    for j in range(max_y2):
        # temp.append(i)
        # temp.append(j)
        # print(temp)
        # temp = []
        if not str(i)+str(j) in dict_val:
            dict_val[str(i)+str(j)] = 1
        else:
            dict_val[str(i)+str(j)] += 1

print(dict_val)
count = 0

for i,j in dict_val.items():
    if j >= 2:
        count += 1

print(len(dict_val))
print(count)