from urllib.request import urlopen,urlretrieve
import re

url = 'http://www.baidu.com'
# 打开远程文件 urlopen
webpage = urlopen(url)
text = webpage.read()

# 获取远程文件 urlretrieve 获取并保存到指定路径
urlretrieve(url, './14_net/urllib/baidu_temp.html')


'''
    1. quote(string[,safe]): 返回一个字符串
    2. quote_plus(string[, safe]): 类似 quote(string[,safe]),但将空格替换成加号
    3. unquote(string): 与quote相反
    4. unquote_plus(string):  quote_plus 相反
    5. urlencode(query[,doseq]): url编码，将映射（如字典）或由包含两个元素的元组组成的序列转换成url编码的字符串
'''

