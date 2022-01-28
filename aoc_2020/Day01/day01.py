with open('input.txt') as f:
    content = f.read()
#array = content.split()
res = [int(i) for i in content.split()]

for i in range(len(res)):
    for j in range(len(res)):
        for k in range(len(res)):
            if res[i] + res[j] + res[k] == 2020:
                print(res[i]*res[j]*res[k])
                break