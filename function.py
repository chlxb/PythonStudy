# def 引入函数的定义，其后必须跟有函数名和以括号表明的形式参数列表。
# 函数第一行可以是一个可选的字符串文本。此字符串是函数的文档字符串


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
