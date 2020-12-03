with open('output.txt') as f:
    content = f.read()

# 31 chars in each line
# 323 lines

res = content.split('\n')

#line_length = len(res[1])
check = 0
count = 0
j = 0

try:
    for i in range(len(res)-1):#range(int((len(res)/2)-1)):
        print(res[i])
        check += 1
        if res[j+1][check] == '#':
            count += 1
            print(count)
        j += 2
except IndexError:
    print(count)
#    if check >= line_length-1:
#        check = 0

print(count)