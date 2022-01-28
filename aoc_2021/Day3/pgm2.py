lst = []

with open('data.txt') as file:
    for line in file:
        lst.append(line.rstrip())

res = ''
eps = ''
count1 = 0
count0 = 0
keep_lst = []
temp = lst

for i in range(len(lst[0])):
    for j in lst:
        if j[i] == '0':
            count0 += 1
        elif j[i] == '1':
            count1 += 1

    if count0 > count1:
        for k in lst:
            if k[i] == '0':
                keep_lst.append(k)
        #print(keep_lst)
    else:
        for k in lst:
            if k[i] == '1':
                keep_lst.append(k)
        #print(keep_lst)

    count0 = 0
    count1 = 0
    lst = keep_lst
    keep_lst = []

val1 = lst[0][::-1]
keep_lst = []
count0 = 0
count1 = 0

for i in range(len(temp[0])):
    for j in temp:
        if j[i] == '0':
            count0 += 1
        elif j[i] == '1':
            count1 += 1

    if count1 < count0:
        for k in temp:
            if k[i] == '1':
                keep_lst.append(k)
        #print(keep_lst)
    else:
        for k in temp:
            if k[i] == '0':
                keep_lst.append(k)
        #print(keep_lst)

    if len(temp) == 1:
        break

    count0 = 0
    count1 = 0
    temp = keep_lst
    keep_lst = []

val2 = temp[0][::-1]

val1_int = int(val1)
val2_int = int(val2)

val1_dec = 0
val2_dec = 0

for i in range(len(val1)):
    if val1[i] == '1':
        val1_dec += 2 ** i
    # else:
    #     val1_dec += 2 ** i

for i in range(len(val2)):
    if val2[i] == '1':
        val2_dec += 2 ** i
    # else:
    #     val2_dec += 2 ** i

print(val1_dec * val2_dec)