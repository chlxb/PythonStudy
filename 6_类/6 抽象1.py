
fibs = [0, 1]
for i in range(10):
    # 列表 下标从零开始 是倒着取
    fibs.append(fibs[-2] + fibs[-1])
print(fibs)