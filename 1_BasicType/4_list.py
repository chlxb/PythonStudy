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
print(lassmamtes[-1])   # 从尾部开始

# 3 切片
# 正向操作 
sub = classmamtes[:2] 
print("切片 :2{0}".format(sub))
sub = classmamtes[0][2:5]   # 进行二次切片
print("二次 切片结果 {0}".format(sub))

# 反向操作
print("反向切片 :{0}".format(classmamtes[-1: -3]))
print("反向切片 :{0}".format(classmamtes[-2: ]))     # 切片时，前面的索引一定要不大于后面的索引

# 4 反转 
# 注： 此处的反转是生成与列表元素顺序相反的新列表
alst = [1, 2, 3, 4, 5, 6]
rlst = alst[::-1]   # 反转操作，反转不是修改原列表，而是生成新的
print "反转方法1： {0}".format(rlst)
print "反转方法2： {0}".format(list(reversed(alst)))

# 5 更多操作：
#  .1 len() 返回列表长度
#  .2  + 连接连个列表
result = alst + ["apple", "orange", "bike"]
print "拼接操作后： {0}".format(result)
#  .3 * 重复元素 
print "列表的 * 操作： {0}".format(alst*3)
#  .4 in 判断是否在列表中
if "apple" in result:
    print "apple belong to result"
else:
    print "apple not belong to result"

#  .5 max() 和 min() 获取最大或最小值
list1, list2 = [123, 'sxv, sva', 59], [356, 43, 2]
print "max num in alst is：", max(alst)
print "min value element: {0}".format(min(classmamtes))

#  .6 cmp() 比较  cmp(x, y) ---- if x<y, zero if x==y, positive if x>y
print "比较结果{0}".format(cmp(list1, list2))

#  .7 append() 追加 将指定内容追加到末尾 
classmamtes.append("Kate")
classmamtes.append([4, 'ss', '-3'])
print "classmates after append: ", classmamtes
classmamtes[len(classmamtes):] = ["*", "sd@"]   # append 效果跟 a[len(a):] = [x] 相同
print ": ", classmamtes
classmamtes.append('Tom')

#  .8 list.extend(L)  通过将指定 可迭代对象的 的所有元素追加到已知列表来扩充
# 注： extend() 等价于 按 a[len(a):] = L
original = [1, 2, 3]
ext = ["python", "lxb"]
original.extend(ext)
print("original after extend by list: {0}".format(original))
# 注意： 当 通过字符串来扩充时，字符串被当做字符列表来追加
original = [1, 2, 3]
original.extend("lxb")
print("original after extend by string: {0}".format(original))
original[len(original):] = "abc"    # extend 的等效写法
original[len(original):] = ["sd", "434"]
print(original)

#  .9 L.count(value) -> integer -- 统计指定内容在列表中的出现次数
original = [1, '1', 'hello', 1, -1, 1, 'a']
print("{0} times about {1}".format(original.count(1), 1))
print("{0} times about {1}".format(original.count('a'), 'a'))
print("{0} times about {1}".format(original.count(4), 4))   # 不存在的元素，不报错，显示次数为 0

#  .10 L.index(value, [start, [stop]]) -> integer 
# --    return first index of value.
# --    Raises ValueError if the value is not present.
# --    获取指定元素在列表中首次出现的索引，如果元素不存在，则报错
original.index("hello")
# original.index("world") # 报错

#  .11 L.insert(index, object) -- insert object before index
# --    在指定索引前面插入元素
original = []
original.insert(-3, 9)  # 
original.insert(2, 3)   # 如果索引不存在，则插入到当前元素的末尾或列表头部（取决于索引 >0? ）
original.insert(0, "hello")
original.insert(5, ['l', 'x', 'b'])
original.insert(len(original), 6)
print("original : {0} after insert".format(original))

#  .12 L.pop([index]) -> item 
# --    remove and return item at index (default last).
# --    Raises IndexError if list is empty or index is out of range.
# --    从列表中移除并返回指定索引处的元素，如果不指定索引，则默认是末尾。如果列表为空或者 索引越界，报错
# result = original.pop(-10) # 索引不存在，报错
result = original.pop(-1)  # result = 6 
print("type of result is: {0}, result is: {1}".format(type(result), result))
print("original {0} after pop".format(original))
#  .13  L.remove(value) 
# --    remove first occurrence of value.
# --    Raises ValueError if the value is not present.
# --    移除首次出现在列表中的 value 值，如果 value 不存在，报错，无返回值
original = [1, 4, 1, 5, 'hello', 'b', 'hello']
original.remove(1)
# original.remove("world")    # 因为 world 不存在所以会报错
print(original)

#  .14 L.reverse() -- reverse *IN PLACE* 将列表翻转
original.reverse()
print("original {0} after reverse".format(original))

#  .15 L.sort(cmp=None, key=None, reverse=False) 
# -- stable sort *IN PLACE*;
# --    cmp(x, y) -> -1, 0, 1
# --    key 根据什么比较
# --    是否倒序
# -- 排序
original.sort()
print("original %s after sorted" % original)


# 6 list 跟 str 对比总结
# list 跟 str 都属于列表类型，列表的函数大多数在 list 跟 str 中有相应的实现
# 区别： 
#   1. list 是可变类型，str 不可变。及 list 可以进行原地修改内容，str 不能如此做，只能通过生成新 str 达到类似修改的目的
#   2. 多维 list

# 7 list 和 str 转化
# split(), join()
s = "I am, writing\npython\tbook on line"
new = s.split() # split 不带参数时，默认见到任何分割符号，就用其分割
