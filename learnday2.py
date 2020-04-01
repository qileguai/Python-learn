# -*- coding:utf-8 -*-
# @Content：
# @Time: 2020/3/31 9:58
# @Author: kuvi
# @Email: kkxxmei1tian@foxmail.com
# @File: learnday2.py
'''
硬性规则：
变量名由字母（广义的Unicode字符，不包括特殊字符）、数字和下划线构成，数字不能开头。
大小写敏感（大写的a和小写的A是两个不同的变量）。
不要跟关键字（有特殊含义的单词，后面会讲到）和系统保留字（如函数、模块等的名字）冲突。
PEP 8要求：
用小写字母拼写，多个单词用下划线连接。
受保护的实例属性用单个下划线开头（后面会讲到）。
私有的实例属性用两个下划线开头（后面会讲到）
'''

'''
使用变量保存数据进行算数运算
'''
# a = 123
# b = 321
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)

'''
检查变量类型
'''
# a = 100
# b = 12.345
# c = 1 + 5j
# d = 'hello, world'
# e = True
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

'''
内置函数进行变量类型转换
int()：将一个数值或字符串转换成整数，可以指定进制。
float()：将一个字符串转换成浮点数。
str()：将指定的对象转换成字符串形式，可以指定编码。
chr()：将整数转换成该编码对应的字符串（一个字符）。
ord()：将字符串（一个字符）转换成对应的编码（整数）。
'''
# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %f' % (a, b, a / b))
# print('%d // %d = %d' % (a, b, a // b))
# print('%d %% %d = %d' % (a, b, a % b))
# print('%d ** %d = %d' % (a, b, a ** b))

#其中%d是整数的占位符，
# %f是小数的占位符，
# %%表示百分号（因为百分号代表了占位符，所以带占位符的字符串中要表示百分号必须写成%%），
# 字符串之后的%后面跟的变量值会替换掉占位符然后输出到终端中

'''
运算符
[] [:]	下标，切片
**	指数
~ + -	按位取反, 正负号
* / % //	乘，除，模，整除
+ -	加，减
>> <<	右移，左移
&	按位与
^ |	按位异或，按位或
<= < > >=	小于等于，小于，大于，大于等于
== !=	等于，不等于
is is not	身份运算符
in not in	成员运算符
not or and	逻辑运算符
= += -= *= /= %= //= **= &= `	   = ^= >>= <<=`

'''
#搞不清楚运算符的优先级，可以使用括号来确保运算的执行顺序
# a = 10
# b = 3
# a += b # 相当于：a = a + b
# a *= a + 2 # 相当于：a = a * (a + 2)
# print(a) #195
#
# #比较，逻辑，身份运算符
# flag0 = 1 == 1
# flag1 = 3 > 2
# flag2 = 2 < 1
# flag3 = flag1 and flag2
# flag4 = flag1 or flag2
# flag5 = not (1 != 2)
# print('flag0 =', flag0) # flag0 = True
# print('flag1 =', flag1) # flag1 = True
# print('flag2 =', flag2) # flag2 = False
# print('flag3 =', flag3) # flag3 = False
# print('flag4 =', flag4) # flag4 = True
# print('flag5 =', flag5) # flag5 = False
# print(flag1 is True) # True
# print(flag2 is not False) # False

#练习1：华氏温度转换为摄氏温度
#华氏温度＝摄氏温度×1.8+32
# f = float(input('请输入华氏温度：'))
# c = (f - 32) / 1.8
# print('摄氏温度为：%d' % c)

#练习2： 计算圆的周长和面积

# import math
#
# r = float(input('输入圆的半径：'))
# C = 2 * math.pi * r
# S = math.pi * r * r
#
# print('周长为：%d' % C)
# print('面积为: %d' % S)

#练习3 判断输入的年份是不是闰年

'''
是闰年True
不是为False
普通闰年:公历年份是4的倍数的，且不是100的倍数，为普通闰年。（如2004年就是闰年）；
世纪闰年:公历年份是整百数的，必须是400的倍数才是世纪闰年（如1900年不是世纪闰年，2000年是世纪闰年）；
'''
year = int(input('输入年份：'))
is_leap_year = (year % 4 ==0 and year % 100 != 0) or year % 400 == 0
print(is_leap_year)

