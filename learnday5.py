# -*- coding:utf-8 -*-
# @Content：
# @Time: 2020/3/31 14:37
# @Author: kuvi
# @Email: kkxxmei1tian@foxmail.com
# @File: learnday5.py
'''
构造程序逻辑
'''
# 寻找水仙花数
# 水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，
# 它是一个3位数，该数字每个位上数字的立方之和正好等于它本身
#思路
# 三位数即100-1000
#拿到个十百位的单个数字
# for x in range(100, 1000):
#     ge = x % 10
#     # print(ge)
#     shi = x // 10 % 10
#     # print(shi)
#     bai = x // 100
#     # print(bai)
#     # print(x)
#     if x == ge ** 3 + shi ** 3 + bai ** 3:
#         print(x)

#正整数反转
# 将12345变成54321
# num = int(input('num = '))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num //= 10
# print(reversed_num)


#百钱百鸡
# 公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
# for x in range(0, 20):
#     for y in range(0, 33):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z / 3 == 100:
#             print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))


# CRAPS赌博游戏。
# 该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
# 简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
# 玩家第一次如果摇出2点、3点或12点，庄家胜；
# 其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
# 如果玩家摇出了第一次摇的点数，玩家胜；
# 其他点数，玩家继续要骰子，直到分出胜负。
# from random import randint
#
# money = 1000
# while money > 0:
#     print('你的总资产为:', money)
#     needs_go_on = False
#     while True:
#         debt = int(input('请下注: '))
#         if 0 < debt <= money:
#             break
#     first = randint(1, 6) + randint(1, 6)
#     print('玩家摇出了%d点' % first)
#     if first == 7 or first == 11:
#         print('玩家胜!')
#         money += debt
#     elif first == 2 or first == 3 or first == 12:
#         print('庄家胜!')
#         money -= debt
#     else:
#         needs_go_on = True
#     while needs_go_on:
#         needs_go_on = False
#         current = randint(1, 6) + randint(1, 6)
#         print('玩家摇出了%d点' % current)
#         if current == 7:
#             print('庄家胜')
#             money -= debt
#         elif current == first:
#             print('玩家胜')
#             money += debt
#         else:
#             needs_go_on = True
# print('你破产了, 游戏结束!')

"""
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...

"""
#
# a = 0
# b = 1
# for x in range(20):
#     a, b = b, a + b
#     print(a, b)


"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14

"""
# import math
#
# for num in range(1, 10000):
#     result = 0
#     for factor in range(1, int(math.sqrt(num)) + 1):
#         if num % factor == 0:
#             result += factor
#             if 1 < factor != num // factor:
#                 result += num // factor
#     if result == num:
#         print(num)


"""
输出100以内所有的素数。
说明：素数指的是只能被1和自身整除的正整数（不包括1）。
输出2~99之间的素数
"""

import math

for num in range(2, 100):
    is_prime = True
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
