# -*- coding: utf-8 -*-
# Python 内置的一种数据类型时列表： list。list是一种有序的集合，
# 可以随时添加和删除其中的元素

'''====================list===================='''
# list python中的基本数据结构。列表中的数据项不需要具有相同的类型
# 注： 索引是可变数据类型，字符串是不可变的
# 1. 创建 
empty = list()  # 空列表
empty = []  # 空列表

classmamtes = ['Michael', 'Bob', 'Tracy']
len(classmamtes) # 获取列表长度
# 2 索引  通过索引可以访问列表中的所有数据， 索引从0开始, 最后一个
# 元素的索引是 length-1, 取得最后一个元素，除了计算索引位置外，还
# 可以使用 -1 做索引，依次类推，可以 -2 可以获得倒数第二；-3 ……
print classmamtes[-1]   # 从尾部开始

# 3 切片
# 正向操作 
sub = classmamtes[:2] 
print "切片 :2{0}".format(sub)
sub = classmamtes[0][2:5]   # 进行二次切片
print "二次 切片结果 {0}".format(sub)

# 反向操作
print "反向切片 :{0}".format(classmamtes[-1: -3])   
print "反向切片 :{0}".format(classmamtes[-2: ])     # 切片时，前面的索引一定要不大于后面的索引

# 4 反转
alst = [1, 2, 3, 4, 5, 6]
rlst = alst[::-1]   # 反转操作，反转不是修改原列表，而是生成新的
print "反转方法1： {0}".format(rlst)
print "反转方法2： {0}".format(list(reversed(alst)))

# 5 更多操作：
# 5.1 len() 返回列表长度
# 5.2  + 连接连个列表
result = alst + ["apple", "orange", "bike"]
print "拼接操作后： {0}".format(result)
# 5.3 * 重复元素 
print "列表的 * 操作： {0}".format(alst*3)
# 5.4 in 判断是否在列表中
if "apple" in result:
    print "apple belong to result"
else:
    print "apple not belong to result"

# 5.5 max() 和 min() 获取最大或最小值
list1, list2 = [123, 'sxv, sva', 59], [356, 43, 2]
print "max num in alst is：", max(alst)
print "min value element: {0}".format(min(classmamtes))

# 5.6 cmp() 比较  cmp(x, y) ---- if x<y, zero if x==y, positive if x>y
print "比较结果{0}".format(cmp(list1, list2))

# 5.7 append() 追加 将指定内容追加到末尾 
classmamtes.append("Kate")
classmamtes.append([4, 'ss', '-3'])
print "classmates after append: ", classmamtes
classmamtes[len(classmamtes):] = ["*", "sd@"]   # append 效果跟 a[len(a):] = [x] 相同
print ": ", classmamtes

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