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
    
比如：性别，非男即女
'''

'''
input的作用：
1.在屏幕上输出括号中的字符串
2.接受用户输入的内容并返回到程序
3.input返回的内容一定是字符串类型
'''
#sex = input('请输入性别：') #input 在屏幕上输入字符串
sex = 'nan'
if sex == 'nan':
    print('此人性别为：',sex)
else:
    print('性别为女')



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
    
例：score 成绩 学生成绩（0-100）问题 90以上 A，80-90 B，70-80 C，60-70 D，60以下 E
'''

score = input('学生成绩：')

score = int(score)  #如果不把输入的字符串转换成数值型，则会报错 TypeError: '<=' not supported between instances of 'int' and 'str'

if 90 <= score < 100:
    print('该学生成绩为：A')
elif 80 <= score < 90:
    print('该学生成绩为：B')
elif 70 <= score < 80:
    print('该学生成绩为：C')
elif 60 <= score < 70:
    print('该学生成绩为：D')
elif 0 <= score < 60:
    print('该学生成绩为：E')
else:
    print('输入的分数错误')