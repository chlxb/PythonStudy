
'''
    1. 打开文件
        a 使用函数open, open 函数位于自动导入的模块 io 中。如果文件位于其他地方，可以指定完整路径，如果文件不粗那组，将出现异常 'No such file or directory: 'somefile1.txt''
        b 如果要通过写入文本来创建文件，此时直接使用open函数不能满足需求，需要使用open的第二个参数
            open 函数，只写入文件名，获得一个可读取的文件对象，要写入文件需要传入相应的参数
            value   |   descripe                           |  作用
            'r'     |   读取模式 默认值                      | 可读不可写
            'w'     |   写入模式                            | 可写不可读
            'x'     |   独占写入模式                         | 可写不可读
            'a'     |   附加模式                            | 总是将写入内容插入文件头
            'b'     |   二进制模式（与其他模式结合使用）         
            't'     |   文本模式（默认值，与其他模式结合使用）   | 
            '+'     |   读写模式（与其他模式结合使用）
            写入模式可以在文件不存在的时候创建它。独占写入模式在文件存在时引发 FileExistsError 异常。在写入模式打开文件，既有内容将被删除，并从头开始写入，可以使用附加模式
            + 可以与其他模式结合起来使用，表示可读可写。 'r+' 可读写，
            r+ 跟 w+ 的差别： w+ 会截断文件，r+ 不会
            默认模式为 rt, 意味着文件被视为 经过编码的 Unicode.
'''

'''
    文件的基本方法：
        打开 open
        写入 write
        读取 read  read(4)读取4字符， read 每次会从上次读取的位置开始继续读取。

'''

'''
    使用管道重定向输出:
'''
def io_test():
    # 尝试打开一个不存在或路径错误的文件，报异常
    f = open('../somefile1.txt')

    # 写入模式打开  完整路径文件
    f = open('/Users/liuxiaobing13/Documents/lxb/github/PythonStudy/somefile1.txt', 'w')
    f.write('写入文件开始：\n')
    f.write('第2行内容')
    # 关闭文件
    f.close()

    # 写入模式打开 w 模式在打开时就会截断文件内容。此时读取的话，已经没有内容了
    f = open('../somefile1.txt', 'w+')
    # 读取数据 read(length) 读取的字节数
    last = f.read()
    f.write('重新开始写入，会覆盖原来写入的内容')
    print("上次输入的内容  {0}".format(last))
    f.close()

    # r+ 模式不截断
    f = open('../somefile1.txt', 'r+')
    fourByte = f.read(4)
    last = f.read()
    print("上次输入的内容 读取前四字节 {0} 剩余内容不限制读取长度 {1}".format(fourByte, last))

if __name__ == "__main__":
    io_test()


import sys

text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print('word count: ', wordcount)

# 终端执行管道操作 
# cat somefile.txt | python3 1_file.py 统计somefile.txt的单词数量


