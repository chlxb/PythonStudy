'''
练习 - 跑马灯 在屏幕上显示跑马灯文字
'''
import os
import time

def lamp():
    content = '北京欢迎你为开天辟地……'
    roundCount = 0
    while roundCount < 10:
        # 清理屏幕上的输出
        os.system('clear')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]
        roundCount += 1


'''
2 -- 设计一个生成指定长度的验证码，验证码由大小写字母和数字构成
'''
import random

def gennrator_code(length = 4):
    """ 
    生成指定长度的验证码，默认为4
    :param length: 验证码长度（默认4个字符长度）
    :return: 由大小写字母和数字构成的随机验证码
    """
    all_chars = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(length):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code

'''
3 -- 查询给定文件名的后缀
'''
def file_suffix(filename, need_dot = False):
    """ 
    查询指定文件名的后缀
    :param filename: 文件名
    :param need_dot: 是否需要返回 .
    :return: 文件后缀
    """
    dotPos = filename.rfind('.')
    if 0 < dotPos < len(filename) - 1:
        index = dotPos if need_dot else dotPos + 1
        return filename[index:]
    else:
        return ''

'''
4 -- 返回列表中 最大 和 第二大的元素的值
'''
def find_max2(list):
    maxum, bigger = (list[0], list[1]) if list[0] > list[1] else (list[1], list[0])
    for index in range(2, len(list)):
        if maxum < list[index]: 
            bigger = maxum
            maxum = list[index]
        elif bigger < list[index]:
            bigger = list[index]
    return maxum, bigger


if __name__ == '__main__':
    lamp()
    print('5位验证码: ', gennrator_code(5))
    print('file_suffix: {0}'.format(file_suffix('hello.txt', True)))
    print('前两位大的数：max = {0}, bigger: {1}'.format(find_max2([-1, 6, 3, 2, 0, 2, 4])[0], find_max2([-1, 6, 3, 2, 0, 2, 4])[1]))