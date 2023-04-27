
a = 'Now I need a drink, alcoholic of course, after the heavy leutures involving quantum mechanics.'

words = [x.strip() for x in a.split(',.')]
print(words)
b = ''

for i in range(0, 14):
    num = str(len(words[i]))
    b += num

print(b)
