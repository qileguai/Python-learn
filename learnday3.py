# -*- coding:utf-8 -*-
# @Content：
# @Time: 2020/3/31 9:58
# @Author: kuvi
# @Email: kkxxmei1tian@foxmail.com
# @File: learnday3.py
'''
分支结构
如果if条件成立的情况下需要执行多条语句，
只要保持多条语句具有相同的缩进就可以了，
换句话说连续的代码如果又保持了相同的缩进那么它们属于同一个代码块，
相当于是一个执行的整体。
'''


'''
if语句的使用
使用if、elif和else关键字
'''
# username = input('请输入用户名：')
# password = input('请输入密码：')
#
# if username == 'admin' and password == '123456':
#     print('验证成功')
# else:
#     print('验证失败')

"""
分段函数求值

        3x - 5  (x > 1)5
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""

# x = float(input('x= '))
# if x > 1:
#     y = 3 * x - 5
# elif x >= -1:
#     y = x + 2
# else:
#     y = 5 * x + 3
#
# print('f(%d) = %d' % (x, y))

#练习1
"""
英制单位英寸和公制单位厘米互换
1英寸(in)=2.54厘米(cm)
"""

# value = float(input('请输入长度: '))
# unit = input('请输入单位: ')
# if unit == 'in' or unit == '英寸':
#     print('%f英寸 = %f厘米' % (value, value * 2.54))
# elif unit == 'cm' or unit == '厘米':
#     print('%f厘米 = %f英寸' % (value, value / 2.54))
# else:
#     print('请输入有效的单位')
#练习2
'''
百分制成绩转换为等级制成绩。
要求：
如果输入的成绩在90分以上（含90分）输出A；
80分-90分（不含90分）输出B；
70分-80分（不含80分）输出C；
60分-70分（不含70分）输出D；
60分以下输出E。
'''
# score = float(input('请输入成绩: '))
# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >= 70:
#     grade = 'C'
# elif score >= 60:
#     grade = 'D'
# else:
#     grade = 'E'
# print('对应的等级是:', grade)
#练习3
'''
输入的边长能否构成三角形，如果能则计算出三角形的周长和面积
1.三角形任意两边之和大于第三边
2.三角形任意两边之差小于第三边

'''
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a\
        and a - b < c and a - c < b and b - c < a:
    print('周长: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积: %f' % (area))
else:
    print('不能构成三角形')





