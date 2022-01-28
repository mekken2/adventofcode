lst = []

with open('data.txt') as file:
    for line in file:
        lst.append(line.rstrip())

res = ''
eps = ''
count1 = 0
count0 = 0

for i in range(len(lst[0])):
    for j in lst:
        if j[i] == '0':
            count0 += 1
        elif j[i] == '1':
            count1 += 1

    if count0 > count1:
        res += '0'
        eps += '1'
    else:
        res += '1'
        eps += '0'

    count0 = 0
    count1 = 0

res = res[::-1]
eps = eps[::-1]
binary_res = int(res)
binary_eps = int(eps)

dec_res = 0
dec_eps = 0

for i in range(len(res)):
    if res[i] == '1':
        dec_res += 2 ** i
    else:
        dec_eps += 2 ** i

print(dec_eps)
print(dec_res)
print(dec_res * dec_eps)