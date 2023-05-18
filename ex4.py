a = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
a = a.replace(".","")
print(a)

words = a.split()   #空白で区切ってリスト化
print(words)

list1 = [1, 5, 6, 7, 8, 9, 15, 16, 19]  #先頭1文字を取り出す単語の番号
b = {}

for i, word in enumerate(words):
    if i+1 in list1:
        b[word[:1]] = i+1
    else:
        b[word[:2]] = i+1
        
print(b)