#!/usr/bin/python3

'''
python3中有6种标准数据类型
1.Number 数字
2.String 字符串
3.List 列表
4.Tuple 元组
5.Set 集合
6.Dictionary 字典
'''

#Number
#整数
int_num = 18
print(int_num)  #18

#定义变量
num1,num2,num3 = 11,31,22
print(num1) #11
print(num2); #31
print(num3) #22

#数值计算
print(num1+num3) #33
print(num3-num2)   # -9
print(num1*num2)  #341
print(num2/num1) #2.8181818181818183
print(num2%num1) #9
print(num3/num1)  #2.0

#浮点型
float_num1 = 1.2
float_num2 = .5
float_num3 = 4.
print(float_num1) #1.2
print(float_num2) #0.5
print(float_num3) #4.0

#复数 整数+虚数 ： 1 + 2j
complex_num = 1 + 2j
print(complex_num)  #(1+2j)

#2.String 字符串
#字符串表达形式，
# 单引号，双引号： 表示一行 ，
#三单引号，三双引号： 可以表示多行，允许换行

str1 = 'hello world'
print(str1)  #hello world
str2 = "hello World"
print(str2) #hello World
#str3 = 'hello world"  #单引号和双引号要成对出现，否则报错

#单引号和双引号在字符串表示上没有什么区别，不过当字符串中有引号时可以区分
str4 = 'you are my "angle"'
print(str4) #you are my "angle"

#单引号和双引号并不能表示换行，如果有换行操作，可是使用 ''' ''' 或者 """ """

'''
str5的输出：
you 
and
me
'''
str5 = '''
you 
and
me
'''
print(str5)

''' str6的输出：
you are my 
 angel;
H LOVE Y
'''
str6 = """
you are my \n angel;
H LOVE Y
"""
print(str6)


#3.List 列表