# _*_ coding: utf-8 _*_
# 条件 
# if xxx: ... elif xxx: ... else: ....
height = 1.75
weight = 80.5
bmi = weight / (height * height)
if bmi < 18.6:
    print("过轻")
elif bmi < 25:
    print('过重')
elif bmi < 28:
    print('肥胖')
elif bmi < 32:
    print('严重肥胖')
    pass

# 循环
# for ... in 
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
x = 1
list = [x for x in range(11)]
print(list)
for x in range(101):
    sum += x
print(sum)

# while 循环 
sum = 0
n = 1
while n < 100:
    sum += n
    n += 2
print(sum)

print("use for ... in")
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello,' + name + '!')
    pass

print("use while ...")
n = 0
while n < len(L):
    print('Hello,' + L[n] + '!')
    n += 1
    pass

strings = ['Hsjhs', 'sdhjngf', 'ssdXXXd', 'sss']
index = 0
for string in strings:
    if 'XXX' in string:
        strings[index] = '[censored]'
    index += 1
else:
    print(strings)

for index, string in enumerate(strings):
    if 'ss' in string:
        strings[index] = 'xxxx{}'.format(index)
else:
    print(strings)

# break 可以使循环提前 退出 
# continue 跳过当前循环

name = ''
while not name:
    name = input('Please enter your name: ')
print('Hello, {}!'.format(name))

# 迭代字典
iterateDic = {'x': 1, 'y': 2, 'z': 3}
for key in iterateDic:
    print(key, 'corresponds to', iterateDic[key])


# while True/break 
# 不够优雅的方式
# word = 'dummy'
# while word:
#     word = input('please enter a  word: ')
#     print('The word was', word)

while True:
    word = input('please enter a  word: ')
    if not word: break
    print('The word was', word)

from math import sqrt

# 可以在循环中添加 else 字句，该else仅在没有调用break时才执行；
for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else:
    # 仅仅没有调用break退出时才会执行
    print("Didn't find it")

# 列表推导 列表退到是一种从其他列表创建列表的方式，类似于-数学中的集合推导
# 例：10以内的平方值：
newList = [x * x for x in range(10)]
print(newList)
# 例：10以内可以被3整除的平方值
newList = [x * x for x in range(10) if x % 3 == 0]
print(newList)

newList = [(x, y) for x in range(3) for y in range(2, 5)]
print(newList)

# 例：将名字首字母相同的男孩跟女孩配对 
# 注：这种方式遍历并检查所有情况是否满足要求，效率不高
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnol', 'bob', 'kris']
print([b+'+'+g for b in boys for g in girls if b[0] == g[0]])

letterGirls = {}
for g in girls:
    letterGirls.setdefault(g[0], []).append(g)
# print([b+'+'+g for b in boys for g in letterGirls[b[0]] if b[0] in letterGirls])  # 此种写法会奔溃，因为 'k' 在letterGirls 中不存在
print([b+'+'+g for b in boys if b[0] in letterGirls for g in letterGirls[b[0]]])  # 应该把 if 放在 for 前面

