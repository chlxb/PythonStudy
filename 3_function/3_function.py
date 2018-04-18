# This Python file uses the following encoding: utf-8
# -*- coding: utf-8 -*-
# 1-1 定义函数
# def 引入函数的定义，其后必须跟有函数名和以括号表明的形式参数列表。函数体的语句从下一行开始，且必须缩进。
# 函数第一行可以是一个可选的字符串文本。此字符串是函数的文档字符串
# 没有 return 语句的函数默认返回一个 None 值，可以使用 print 打印该值

def fib(n): # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a , b = 0 , 1
    while a < n:
        print a,
        a , b = b , a + b


def fib2(n): # return Fibonacci series up to n
    """Return a Fibonacci series up to n."""
    result = []
    a , b = 0 , 1
    while a < n:
        result.append(a) # see below
        a , b = b , a+b
    return result         

fib(2000)
print '\n',fib,'\n'
f=fib
print  f(100),'\n'
f100=fib2(100)
print f100,'\n'

# 1-2 默认参数值
# 函数定义的时候，可以给参数设置默认值，此类函数被调用时，可以带有比定义要少的参数。
def ask_ok(prompt, restries = 4, complaint = 'Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        restries = restries - 1
        if restries < 0:
            raise IOError('refusenik user')
        print complaint

ask_ok('DHJGHSSS')


# Python 中的 for 语句按照元素出现的顺序迭代任何序列（列表或字符串）。
#Measure some strings:
print 'for 语句：'
words = ['cat', 'window', 'defensestrate']
for w in words:
    print w, len(w)

# 如果要在循环内修改正在迭代的序列，建议先制作副本，迭代序列不会隐式创建副本。 使用切片就可以很容易的做到：
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
print words



# 4.5 pass 语句：pass 语句什么也不做。它用于预发上必须要有一条语句，
# 但程序什么也不需要做的场合。通常用于创建最小的类：
class MyEmptyClass:
    pass
# 另一个使用 pass 的地方是编写新代码时，作为函数体或控制体的占位符，这让你在更抽象层次上思考
def initlog(*args):
    pass