with open('input.txt') as f:
    content = f.read()

res = content.split('\n')

for i in range(len(res)):
    res[i] *= 1000

for i in range(len(res)):
    with open('output.txt','a+') as f:
        f.write(res[i]+'\n')
