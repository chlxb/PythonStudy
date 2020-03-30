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
