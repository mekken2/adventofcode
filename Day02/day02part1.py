with open('input.txt') as f:
    content = f.read()

res = content.split('\n')
count_word = 0

for i in res:
    lower_limit = i[0:i.find('-')]
    lower_limit = int(lower_limit)
    upper_limit = i[i.find('-')+1:i.find(' ')]
    upper_limit = int(upper_limit)
    letter = i[i.find(' ')+1]
    word = i[i.find(': ')+1:]
    count = 0
    for j in range(len(word)):
        if letter == word[j]:
            count += 1
    if count >= lower_limit and count <= upper_limit:
        count_word += 1

print(count_word)