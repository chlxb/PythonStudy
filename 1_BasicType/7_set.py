# -*- coding: utf-8 -*-
# 集合 set : 集合的元素没有顺序，且不会重复，基本用途有 成员测试和消除重复的条目
# 集合支持交集、并集、差和对称差等运算
# 创建集合使用： 花括号 或者 set() 函数，
# 注意： 若要创建一个空集合必须使用 set()函数， {}将创建一个空字典
print '====================set===================='
basket = {'apple', 'orange', 'apple', 'pear', 'banana'}
print basket
fruit = set(basket) # create a set without duplicates
print 'orange' in fruit # 验证是否存在指定元素 
fruit.add('watermelon') # add 添加集合元素
fruit.remove('apple')   # remove 删除集合元素 
a = set('aujbcxgfdensa')
b = set('sdjcbheriy')
c = a - b
print a
print c
a = {x for x in 'asdhcnhjgue' if x not in 'abc'} # 集合支持列表推导式