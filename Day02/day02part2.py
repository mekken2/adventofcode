with open('input.txt') as f:
    content = f.read()

res = content.split('\n')

count1 = 0
count2 = 0

for i in res:
    lower_limit = i[0:i.find('-')]
    lower_limit = int(lower_limit)
    upper_limit = i[i.find('-')+1:i.find(' ')]
    upper_limit = int(upper_limit)
    letter = i[i.find(' ')+1]
    word = i[i.find(': ')+2:]
    print(word)
    
    if word[lower_limit-1] == letter or word[upper_limit-1] == letter:
        count1 += 1
    if word[lower_limit-1] == letter and word[upper_limit-1] == letter:
        count2 += 1
print(count1-count2)