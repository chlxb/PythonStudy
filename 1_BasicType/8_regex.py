'''
? 匹配0次或1次前面的分组
* 匹配0次或多次前面的分组
+ 匹配1次或多次
{n} 匹配n次
{n,} 匹配n次以上（包括n）
{,m} 匹配m次以下 (包括m)
{n,m} 匹配 n 到 m 次 (包括n和m)
{n,m}? 或 *？对前面的内容进行非贪心匹配
^spam 字符串以spam开头
spam$ 字符串以spam结尾
. 匹配除换行符的所有字符
\d \w \s 分别为 数字 单词 空格
\D \W \S 分别为 数字 单词 空格除外的字符
[abc] 匹配方括号中的任意字符 （a、b或c）
[^abc] 匹配不在方括号中的任意字符

re.IGNORECASE 或 re.I 不区分大小写
re.complie()
'''

import re

def hiddenAllAgentName():
    # 将Agent 后面的内容变星号
    agentNamesRegex = re.compile(r'Agent (\w)\w*')
    result = agentNamesRegex.sub(r'\1****', 'Agent T.x Alice told Agent t.c Carol that Agent T.d Eve knew Agent T.r Bob was a double agent')
    print(result)

hiddenAllAgentName()

# 匹配复杂的正则表达式
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)?       # separator
    \d{3}       # firsst 3 digits
    (\s|-|\.)   # separator
    \d{4}       # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})? # extension
)''', re.VERBOSE)

# 组合使用多个命令
re.compile('foo', re.VERBOSE | re.DOTALL | re.IGNORECASE)

phoneRegex1 = re.compile(r'''(
    (((^0)\d{6,7}))$
)''', re.VERBOSE)
print(phoneRegex.match('010-1234567'))