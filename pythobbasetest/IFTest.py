'''
语法语义
同一语句块中缩进必须一致
三大结构
1,顺序
2.分支，
3.循环
'''

'''
分支 ，
表达式冒号不能少，表达式结果为布尔值，if语句块，必须同一个缩进上，条件表达式为True执行if后面的缩进语句块
if 条件表达式:
     语句1
     语句2
     语句3
     .......
'''

#if语句联系
#如果age小于18，则答应未成年
age = 17
if age < 18:
    print('未成年')
    print('age = ', age)
    print('hello')

age = 20
if age < 18:
    print('未成年')
    print('age = ', age)
    print('hello')
# print(11) 缩进不一致报错
print('age ',age)

# if ... else ... 语句 python没有switch-case语句
'''
if 条件表达式:
    语句1
    语句2
    ...
else:
    语句1
    语句2
    ...
'''

'''
input的作用：
1.在屏幕上输出括号中的字符串
2.接受用户输入的内容并返回到程序
3.input返回的内容一定是字符串类型
'''

'''
多路分支 elif 可以有很多个，else可以没有，多路分支只会选一个执行
if 条件表达式:
    语句1
    语句2
    ...
elif 条件表达式:
    语句1
    语句2
    ...
elif 条件表达式:
    语句1
    语句2
    ...
elif ...
    ...
else:
    语句1
    语句2
    ...
    
例：score 成绩 学生成绩问题
'''