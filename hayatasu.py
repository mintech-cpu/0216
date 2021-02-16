# -*- coding: utf-8 -*-
"""hayatasu.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1coSyP3uG1YnQKZl5WreQ3dzpl26qHD05
"""

#数字の5をスキップする
for i in range(10):
  if i == 5:
    continue
  print(i)

#3の倍数をスキップする
i = 0
for i in range(10):
    if i % 3 == 0:
      continue
    print(i)

i = 0

while i < 100:
  i += 1
  print(i)

l = ['sato', 'tanaka', 'uno']

# for i in range(len(l)):
#   print(i, l[i])

# インデックス番号, 中身

for i, v in enumerate(l):
  print(i, v)

# メソッド
num = [1, 2, 3]
print(num)

num.append(4)
print(num)

l = []

for i in range(5):
  l.append(i)
  
print(l)

# 要素の追加
num = [1, 2, 3]
num.insert(1, 10)

print(num)

# リストの拡張

num1 = [1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)

print(num1)

# 要素の削除
num = [1, 2, 3, 10, 11]

num.remove(10)
print(num)

num.remove(11)
print(num)

# num = []

# for i in range(5):
#   num.append(i)

# print(num)

# リスト内包表記
num = [i for i in range(5)]
print(num)

num = [i for i in range(5) if i % 2 ==0] #for文の中にifぶんを書くことができる
print(num)

t = (1, 2)

one, two = t
print("1", one)
print("2", two)

t1 = (1, 2)
t2 = (3, 4)

t1 = t1 + t2
print(t1)

# 辞書
d = {'apple':100, 'banana':200}
print(d)

# appleに対応する値を取り出す
print(d['apple'])

# bananaの値を12０にする
d['banana'] = 120
print(d)

# peach:150を追加
d['peach'] = 150
print(d)

d = {'apple': 100, 'banana': 120, 'peach': 150}

print(d)

#辞書に入っているkeyを全て取得
d.keys()

# 辞書に入っているkeyをfor分で取り出す
for key in d.keys():
  print(key)

#辞書に入っているvalueを全て取得
d.values()

for value in d.values():
  print(value)

# keyとvalueを全て取得
d.items()

for key, value in d.items():
  print(key, value)

# valueの取り出し
d = {'apple': 100, 'banana': 120, 'peach': 150}

print(d['apple'])

print(d.get('apple'))

# 要素を取得するだけでなく、削除する
print(d.pop('apple'))



