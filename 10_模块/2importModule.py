import hello_module as hello
import package_runoob.runoob1 as oob1
import package_runoob.runoob2 as oob2

import sys
sys.path.append(r"/Users/liuxiaobing13/Documents/lxb/github/PythonStudy/9_magic")
import test_module as test

'''
python 导入自定义模块：
一 同级目录或子目录
    1 导入同级目录下的模块 直接import导入使用 import hello_module as hello
    2 导入子目录文件 
        a. 可以采用 import 一个包的形式，将子目录封装成包，即可调用
           package_runoob 下面创建__init__.py 文件，文件内容可以为空
二 非同级目录中的模块
    3 导入非同级目录中的模块 test_module

'''

# 1 导入同级目录下的模块
hello.show()

# 2 导入包中的模块
oob1.run()
oob2.run()

# 3 导入非同级模块 sys.path.append(r'path')
test.test_print()

'''
    模块导入
    python 模块导入时，只会执行一次导入，避免相互导入的循环，以及优化
    如果需要重新加载模块，可以使用 importlib 中的函数 reload(moduleName)
    reload函数接受需要重新加载的模块名,返回重新加载的模块
'''
from importlib import reload
# 重新加载导入的模块，模块导入会重新执行一次
# helloNew 是 reload 重新加载后返回的模块，helloNew 和 hello都可以实现调用
helloNew = reload(hello)
helloNew.show()
hello.show()