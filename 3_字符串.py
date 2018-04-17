#!/usr/bin python
# coding: utf-8

# 1 转义字符 \
str1 = "What's your name?"  # 引号 
print str1
str1 = "What\'s your name?"
# 1.2 原始字符串：就是指字符串里面的每个字符都是原始含义，比如反斜杠，不会被看做转义符。
path = "C:\new\name.txt"    # 此处作为文件路径，输出不正确，应为 \n 为换行
print path
path = r"C:\new\name.txt"   # 由r开头引起的字符串，就是原始字符串，在里面放任何字符都表示该字符的原始含义。
print path



# 2 变量和字符串：变量无类型，对象有类型。swift语言变量有类型
print type(str1)    # 字符串
str1 = 1990
print type(str1)    # int 

str2 = "year"
# 3 转字符串的三种方式
print str(str1)+str2
print repr(str1)+str2
print `str1`+str2   # 2.7 可用 3.x不可用

# 4 raw_input 从标准输入接收一个字符串输入结果
# 注意：接受的结果都是字符串类型
# name = raw_input("What's your name?\n")
# age = raw_input("How old are you?\n")
# print "Hello {0}".format(name)
# print "Your will be {0} after ten years".format(int(age)+10)

# 5 索引
# 注： 通过索引获取元素的时候，不能超出列表的长度
print "{0} at str2's {1} index".format(str2[0], 0) # 获取指定索引的值 
# 注： 获取指定元素在列表中的索引时，要确保元素在列表中存在，否则会报错
subStr = "s"
if subStr in str2:
    print "{0} at str2's {1} index".format(subStr, str2.index(subStr))
else:
    print "{0} isn't in str2".format(subStr)

# 6 切片: 获取原有列表的子串
# 注： 此种方法获得指定字符串的所有字符的子串是，不会生成新串
sub1 = str2[:]  # 获得 str2 得到所有字符
sub2 = str2[1:] # 得到 从指定索引开始到结束的字符
sub3 = str2[:5] # 得到 开头到指定索引前一个位置的字符
sub4 = str2[:100] # 当终止的索引超出列表长度时，不会出错，效果相当于不写终止索引,但此种方法不推荐获取真个子串
if sub4 == sub1:
    print "sub4 equal sub1"
    print "str2's id is {2}, sub1's id is {0}, sub4's id is {1}".format(id(sub1), id(sub4), id(str2))
    sub1 = "ss"
    print str2
    print sub1

sub1 = sub1 + "sss"
print "{0} id is {1}".format(sub1, id(sub1))
print "{0} id is {1}".format(str2, id(str2))

# 7 格式化输出
print "I like %s" % "Apple"
print "I am %s and %d years old" % ("Tom", 12)
    





