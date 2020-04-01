# -*- coding:utf-8 -*-
# @Content：字符串和常用数据结构_使用字符串
# @Time: 2020/3/31 15:27
# @Author: kuvi
# @Email: kkxxmei1tian@foxmail.com
# @File: learnday7_1.py
'''
1.使用字符串
字符串类型是一种结构化的、非标量类型
'''
s1 = 'hello, world!'
s2 = "hello, world!"
# 以三个双引号或单引号开头的字符串可以折行
s3 = """
hello, 
world!
"""
print(s1, s2, s3, end='')

'''
可以在字符串中使用\（反斜杠）来表示转义，也就是说\后面的字符不再是它原来的意义，
例如：\n不是代表反斜杠和字符n，而是表示换行；
而\t也不是代表反斜杠和字符t，而是表示制表符。
所以如果想在字符串中表示'要写成\'，同理想表示\要写成\\
'''

s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2, end='')

'''
在\后面还可以跟一个八进制或者十六进制数来表示字符，例如\141和\x61都代表小写字母a，
前者是八进制的表示法，后者是十六进制的表示法。
也可以在\后面跟Unicode字符编码来表示字符
例如\u9a86\u660a代表的是中文“骆昊”
'''
s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)

'''
不希望字符串中的\表示转义，我们可以通过在字符串的最前面加上字母r来加以说明
'''

s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')

'''
对字符串进行处理
'''

s1 = 'hello ' * 3
print(s1) # hello hello hello
s2 = 'world'
s1 += s2
print(s1) # hello hello hello world
print('ll' in s1) # True
print('good' in s1) # False
str2 = 'abc123456'
# 从字符串中取出指定位置的字符(下标运算)
print(str2[2]) # c
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5]) # c12
print(str2[2:]) # c123456
print(str2[2::2]) # c246
print(str2[::2]) # ac246
print(str2[::-1]) # 654321cba
print(str2[-3:-1]) # 45


str1 = 'hello, world!'
# 通过内置函数len计算字符串的长度
print(len(str1)) # 13
# 获得字符串首字母大写的拷贝
print(str1.capitalize()) # Hello, world!
# 获得字符串每个单词首字母大写的拷贝
print(str1.title()) # Hello, World!
# 获得字符串变大写后的拷贝
print(str1.upper()) # HELLO, WORLD!
# 从字符串中查找子串所在位置
print(str1.find('or')) # 8
print(str1.find('shit')) # -1
# 与find类似但找不到子串时会引发异常
# print(str1.index('or'))
# print(str1.index('shit'))
# 检查字符串是否以指定的字符串开头
print(str1.startswith('He')) # False
print(str1.startswith('hel')) # True
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!')) # True
# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))
str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit())  # False
# 检查字符串是否以字母构成
print(str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True
str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())