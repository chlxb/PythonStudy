# -*- coding: utf-8 -*-
# dict：
print '====================dict===================='
scores = {'Michael': 97, 'Bob': 76, 'Tracy': 98}
newDict = dict([('space', 4139), ('guodi', 4127), ('jack', 9436)]) # 字典构造函数创建字典
dic2 = dict(sape=4752, gsh=3652, jack=23767) # 通过关键字参数指定 键 - 值 
dic = {x: x**2 for x in (2, 4, 6)} # 字典推导式创建字典 
print scores

scores['Adam'] = 78
print scores

del scores['Bob'] # 用 del 删除 键值对