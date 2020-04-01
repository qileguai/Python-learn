# -*- coding:utf-8 -*-
# @Content：
# @Time: 2020/3/31 9:58
# @Author: kuvi
# @Email: kkxxmei1tian@foxmail.com
# @File: learnday1.py
import sys
#查看版本
print(sys.version)
print(sys.version_info)
'''
单行注释 - 以#和空格开头的部分
多行注释 - 三个引号开头，三个引号结尾
'''
#绘图
import turtle

turtle.pensize(4)
turtle.pencolor('red')

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.mainloop()
