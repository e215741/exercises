a = 'パトカー'
b = 'タクシー'
c = ""

for i in range(0,4):
    str = (a + b)[i::4]
    c += str
    
print(c)
