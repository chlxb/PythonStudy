# -*- coding: utf-8 -*-
#!/usr/bin/python

print '====================tuple===================='
# 另一种有序列表叫元组， tuple。tuple 和 list 类似，元素可以是任意类型。
# 但是 tuple 是不可变数据，通常元组包含不同类型的元素并通过拆分或索引访问甚至通过属性
# 列表是可变，通常元素具有相同的数据类型，并通过迭代访问
# 1. 定义 tuple
empty = () # 定义一个空 tuple
v = ([1,2,3], ["a", "b", "c"])  # 元组1
t = (1, 2, 3)    # 元组2
other = 1234, "hello", t # 元组3
# 注意定义一个只有一个元素的元组，不能写成 t = (1) 
thisIsNum = (1)   #  会被认为是一个数字
thisIsString = ('2') # 字符串
singleton = (1, ) # 元组
print("thisIsNum's type is: {0}, t's type is: {1}".format(type(thisIsNum), type(t)))

fisrt, second, third = other
print("element of other is : {0}, {1}, {2}".format(fisrt, second, third))

# 2 索引 切片
print("索引1: %s" % other[1])
print("索引0: {0}".format(v[0]))
print("索引： {0}".format(v[1][2]))
print("切片: {0}".format(other[1:]))

# 3 list tuple 转化
lst = [1, "哈哈", "hello"]
print("list to tuple {0}".format(tuple(lst)))
tpl = (1, "你好", [1, 3, 5])
print("tuple to list {0}".format(list(tpl)))

# 4 使用场景
# 4.1 tuple 比 list 操作速度快，定义一个仅仅用来遍历的常量集，tuple 替代 list
# 4.2 借助不可变性，可以对不想被修改的数据进行写保护
# 4.3 元组的不可变性使它可以作为字典的 key(前提元组的元素没有 list 等可变类型)
# 4.4 字符串的格式化
