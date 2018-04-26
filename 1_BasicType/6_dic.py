# -*- coding: utf-8 -*-

print '====================dict===================='
# dict：无序的键值对，与序列不同，序列由数字做索引，字典由 key 做索引，key是
# 唯一的，不可重复；key 可以是任意不可变类型。
# 注1：当元组只包含不可变类型的元素时，元组也可以做 key。
# 注2: 字典没有切片

# 1. 创建
empty = {} # 创建空字典
# 1.1 字典构造函数创建字典
newDict = dict([('space', 4139), ('guodi', 4127), ('jack', 9436)]) 
# 1.2 通过关键字参数指定 键 - 值 
dic2 = dict(sape=4752, gsh=3652, jack=23767) 
# 1.3 字典推导式创建字典
dic = {x: x**2 for x in (2, 4, 6)}  
# 1.4 直接赋值
scores = {'Michael': 97, 'Bob': 76, 'Tracy': 98}
# 1.5 利用元组创建字典
tpl = (["first", "Google"], ["second", "Yahoo"])
website = dict(tpl)
print(website)
# 1.6 fromkeys创建字典
numDic = {}.fromkeys([1, 2, 3, 4], "hello")
people = {}.fromkeys(("lily", "lucy"), "girl")
print(people)

# 2 基本操作
#   .1 len(d) -- 返回字典 d 中键值对的数量
#   .2 d[key] -- 返回字典 d 中键 key 对应的值
#   .3 d[key] = value -- 将 value 赋值给字典 d 中 key 对应的值
#   .4 del d[key] -- 删除字典 d 中 key 项，移除键值对
#   .5 key in d -- 检查 key 是否存在于字典 d 中 


scores['Adam'] = 78
print scores

del scores['Bob'] # 用 del 删除 键值对

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

# 遍历字典时，使用 iteritems()方法可以同时得到 键 和 对应的值
for k, v in scores.iteritems():
    print "Key is {0}, value is {1}".format(k, v)