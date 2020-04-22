
'''
yield：生成器的标志
       每次使用yield生成一个值后，函数都将冻结，即在此停止执行。直到被重新唤醒后,函数从环形的地方继续执行
生成器 由两个部分组成：生成器函数 生成器的迭代器
生成器的函数是由 def 语句定义的，其中包含yield，
yield 代表生成一个值，return 表示生成器停止执行，不再生成值
'''
# 展开二维数组
def flatten(nested):
    for sublist in nested:
        print("out")
        for ele in sublist:
            print("yield 执行前", ele)
            yield ele
            print("yield 执行后", ele)

nested = [[1, 2], [3, 4], [5]]
for num in flatten(nested):
    print("{0}".format(num))

flattenList = list(flatten(nested))
print(flattenList)

# 2. 简单生成器 生成器推导
g = ((i + 2) ** 2 for i in range(2, 27))
print(next(g)) # i = 2
print(next(g)) # i = 3

print("sum result in range(10): ", sum(i ** 2 for i in range(10)))

# 迭代多维数组，但是当数组元素有字符串的时候，会有问题
# 原因1：字符串迭代的时候，会被视为序列而展开
# 原因2：字符串字符串的第一个元素是一个长度为 1 的字符串，而长度为 1 的字符串的第一个元素是字符串本身，此处会引发死循环
def flatten2(nested):
    try:
        # 如果 nested 是字符串， 会引发内外层死循环
        for sublist in nested:
            for element in flatten2(sublist):
                yield element
    except TypeError:
        # nested 是一个数的时候， 发生异常
        yield nested

nested2 = [1, [4, 5]]
print(list(flatten2(nested2)))

def flatten3(nested):
    try:
        # 异常捕获， 没有捕获异常就会进入else分支
        # 此处 nested + '' 没有异常说明是字符串，进入 else,跑出类型异常，被外层try捕获
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten3(sublist):
                yield element
    except TypeError:
        # nested 是一个数的时候， 发生异常
        yield nested

nested3 = [1, [4, 5], [[11, 12, [-1, 2], -5]], [99, 0], ["bar", "baz"], "foo"]
print(list(flatten3(nested3)))


'''
生成器方法：
    . send
    . throw 用于在yield表达式处引发异常，调用时可以提供一个异常类型、一个可选值和一个traceback对象
    . close 用于停止生成器，调用无需任何参数，由python垃圾收集器在需要时调用，
             也是基于异常的，在yield处引发GeneratorExit异常。因此如果要在生成器中提供一些清理代码，
             可将yield放在try/finally语句中；或者也可以捕获GeneratorExit异常，但随后必须重新引发它，
             调用close后，再试图从生成器获取值，将导致RuntimeError异常
'''
def repeater(value):
    while True:
        new = (yield value)
        if new is not None: value = new

r = repeater(42)
print(next(r))
print(r.send("Hello, world"))

# 4 模拟生成器(老版本python无法使用生成器)

