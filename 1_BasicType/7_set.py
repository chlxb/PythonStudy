#!/usr/bin/python 
#coding=utf-8
# 集合 set : 集合的元素没有顺序，且不会重复，基本用途有 成员测试和消除重复的条目
# 集合支持交集、并集、差和对称差等运算
# 创建集合使用： 花括号 或者 set() 函数，
# 注意： 若要创建一个空集合必须使用 set()函数， {}将创建一个空字典
print '====================set===================='
# 1. set 创建
basket = {'apple', 'orange', 'apple', 'pear', 'banana'} 
fruit = set(basket) # 从已有 迭代器创建集合， 创建空集合必须使用这种方式
# 集合中不能有重复元素，一下方式，字符串的字符被当成集合元素存储时，会去除重复字符
s1 = set("Boom") 
print("set s1: {0}".format(s1))
# s3 = {"facebook", [1, 2, 'a'], {"a": "a1", "b": "b1"}, 123} # 该语句报错，不能准确确定实字典还是集合
# s3 = {"facebook", [1,2], 123} # 该句报错
# s3 = set(["facebook", [1, 2, 'a'], {"a": "a1", "b": "b1"}])
s3 = set([1, 2, "a"])

print 'orange' in fruit # 验证是否存在指定元素 
fruit.add('watermelon') # add 添加集合元素
fruit.remove('apple')   # remove 删除集合元素 
a = set('aujbcxgfdensa')
b = set('sdjcbheriy')
c = a - b
print a
print c
a = {x for x in 'asdhcnhjgue' if x not in 'abc'} # 集合支持列表推导式