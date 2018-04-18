# -*- coding: utf-8 -*-
# Python 内置的一种数据类型时列表： list。list是一种有序的集合，
# 可以随时添加和删除其中的元素

'''====================list===================='''
classmamtes = ['Michael', 'Bob', 'Tracy']
print classmamtes
print len(classmamtes)
# 索引超出范围时，报 IndexError错误，最后一个元素的索引时 length-1
# 取得最后一个元素，除了计算索引位置外，还可以使用 -1 做索引。
# 依次类推，可以 -2 可以获得倒数第二；-3 ……
print classmamtes[-1]
# 末尾追加 
classmamtes.append('Tom')
# 插入到指定位置 
classmamtes.insert(2, 'Jack')
print classmamtes
# 末尾删除 
classmamtes.pop()
# 删除指定位置
classmamtes.pop(1)
print classmamtes
# 替换指定位置 
classmamtes[2] = 'Lucy' 
print classmamtes

# list 中元素数据类型可以不同 
# 另一种有序列表叫元组， tuple。tuple 和 list 类似，
# 但是 tuple 一旦初始化就不能修改。
# 定义 tuple, t = (1, 2, 3), 定义一个空 tuple, t = ()
# 但是定义一个只有 1 个元素的 tuple，不能写成 t = (1) // 会默认为 1 这个数组
print '====================tuple===================='
t = (1, )
print t



# 注意 set 跟 dict 都不可放入可变对象，因为无法判断两个可变对象是否相等，
# 也就无法保证 set 内部 ‘不会’ 有重复元素
scores['list'] = list
print scores

# 遍历 使用 enumerate()函数可以同时得到索引和对应的值 
for i, v in enumerate(scores):
    print i, v
    pass

# 使用 zip()函数可以成对读取元素。
question = ['name', 'quest', 'favorite color']
answer = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(question, answer):
    print 'What is your {0}? It is {1}.'.format(q, a)
    pass

# 调用 reversed()函数反向遍历一个序列
print "反向遍历序列"
for i in reversed(xrange(1, 10, 2)):
    print i

for f in sorted(fruit):
    print f

# 遍历字典时，使用 iteritems()方法可以同时得到 键 和 对应的值
for k, v in scores.iteritems():
    print "Key is {0}, value is {1}".format(k, v)