
import random

'''
问题描述：将 n 各皇后放在 n * n大小的棋盘上，要求所有皇后相互之间不能在同一行、列、斜线上；
'''
def confict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False

# 提供参数的默认值
def queens(num = 8, state = ()):
    for pos in range(num):
        if not confict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result
                    
def prettyPrint(solution):
    def line(pos, length = len(solution)):
        return '. '*(pos) + 'X ' + '. '*(length - pos - 1)

    for pos in solution:
        print(line(pos))

# 3 * 3 以下 ，对角线等会冲突
print(list(queens(3)))
print(list(queens(4)))

for solution in queens(8):
    print(solution)


prettyPrint(random.choice(list(queens(8))))