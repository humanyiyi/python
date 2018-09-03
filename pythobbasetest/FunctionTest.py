#函数： 一般完成一项特殊功能
'''
函数使用：
    函数要先定义
    调用函数
    def func()
    1.def关键字，后面跟一个空格
    2.函数名，自己定义，起名遵循命名规则，大驼峰命名只给类用
    3.后面的括号和冒号不能省，括号内可以有参数
    4.函数内所有代码缩进
'''

def func():
    print('hello world')
    print('wenheng love yanxi')
    print('you are my angle')

#函数调用
#直接函数名后面跟括号
func()


'''
函数的参数和返回值
    1.参数：赋值给函数传递一些必要的数据或者信息
          形参：在函数定义时用到的参数没有具体的值，只是占位符，为形参
          实参：在函数调用时输入的值
    2.返回值：函数的执行结果
          使用return关键字
          如果没有return，默认返回None
          函数一旦执行return语句，无条件返回，函数结束
'''

#参数的定义
def hello(person):
    print('{0},hello'.format(person))
    print('Sir')

hello('yanxi')

def person(name,age):
    print('my name is {0},my age is {1}'.format(name,age))

person('yanxi',18)

#返回值 return

# 写个九九乘法表

#参数详解


'''普通参数
    定义的时候直接定义变量名
    调用的是直接把变量或者值放入指定位置
    def 函数名(参数1，参数2,...)
         函数体
    调用
    函数名(value1，value2，...)
    调用的时候，具体值参考的是位置，按位置赋值
'''


'''
默认参数
    形参带有默认值
    调用的时候，如果没有对相应形参赋值，使用默认值
        def func(p1=v1,p2=v2,p3=v3,...)
            代码块
        调用1
        func()
        调用2
        value1=100
        value2=200
        func(value1,value2)
'''

#关键字参数
#收集参数