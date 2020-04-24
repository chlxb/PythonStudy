# -*- coding: utf-8
# 中文注释或者文档报错的时候，在python 顶部添加上面一行  -*- coding: utf-8，编码
"""
    this is a module
    show is method 
    testWhileMain and test is test case method
"""

# this is module name
''' this is module name '''
moduleName = 'show hello'

def show():
    '''show module info'''
    print("hello world, I am a custom module")

def test():
    '''hello_module excuted as module'''
    show()
    print("hello_module excuted as module")

def testWhileMain():
    '''hello_module excuted as main'''
    show()
    print("hello_module excuted as main")


if __name__ == '__main__':
    testWhileMain()
else:
    test()
