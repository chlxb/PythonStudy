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
三 添加相应模块到python默认sys.path路径下：
    1 print(sys.path) 获取sys的所有路径，将模块放入其中，程序引入时，可以找到该模块，不建议用这种方式将自定义模块放入python系统模块路径
    2 配置操作系统环境变量 PTHONPATH，添加用户自定的路径到环境变量中
'''

'''
    包：一种包含其他多个模块的模块，模块集合
    必要条件：包是一个目录，目录中必须包含 __init__.py 文件,将包想要包含的模块全都放在包的目录下，包也可以嵌套其他包
'''

'''
    探索模块：
        dir 函数：显示模块所有的函数、类、变量等
        __all__ 变量：定义模块的公有接口，默认导入时，只导入__all__变量列表中的内容；
                     导入其他内容，需要显式的声明需要导入的内容 import module.xxx / from module import xxx

    使用 help 获取帮助： 
        help(hello) //显示整个模块
        help(hello.show) //显示模块指定变量或者函数
    使用 __doc__ 文档：
        在 模块头部添加模块描述，或在方法或者变量的开始添加描述，作为相关文档，可以使用__doc__开查看相关文档
        文档添加方法：
            模块开头，或方法开头，  ''' desc '''   或者   """ desc """
        hello_module.__doc__
'''

'''
    阅读源代码：
    通过__file__ 属性可以查看相应模块的文件路径，从而可以查看源文件
        hello_module.__file__
        copy.__file__sy
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