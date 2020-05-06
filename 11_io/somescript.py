# somescript.py
# 统计当前文件的单词数量

import sys

text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print('Wordcount: ', wordcount);