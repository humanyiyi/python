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

'''
关键字参数
语法：
     def func(p1=v1,p2=v2,...)
        func_body
     使用
     func(p1=value1,p2=value2,...)
     
比较麻烦，但是也有好处
    1.不容易混淆，一般实参和形参只是按照位置一一对应即可，容易出错
    2.使用关键字参数，可以不参考参数位置
'''

def func(name,age,addr):
    print('I am a student')
    print('my name is {0},my age is {1},my adrr is {2}'.format(name,age,addr))

n = 'yanxi'
a = 18
addr = 'beijing'

func(n,a,addr)#my name is yanxi,my age is 18,my adrr is beijing
func(a,n,addr) #my name is 18,my age is yanxi,my adrr is beijing

def stu_key(name = '',age = 0,addr = ''):
    print('I am a student')
    print('my name is {0},my age is {1},my addr is {2}'.format(name,age,addr))

stu_key(name = n, age = a, addr = addr) #my name is yanxi,my age is 18,my addr is beijing
stu_key(age = a, name = n, addr = addr)#my name is yanxi,my age is 18,my addr is beijing

'''
收集参数
把没有位置，不能和定义时的参数位置相对应的参数，放入一个特定的数据结构中
语法
   def func(*args):
      func_body
      按照list使用方式访问args得到传入参数
      
    调用：
    func(p1,p2,p3,p4....)

参数名args不是必须这样写，但是推荐用args
参数名args前需要星号
收集参数可以和其他参数并存
'''

#收集参数写在第一位和最后一位，中间位置的区别，收集参数可以不带参数
#type函数作用是检测变量类型

'''
收集参数值关键字收集参数
把关键字参数按字典格式存入收集参数
语法：
    def func(**kwargs):
        func_body
    调用：
    func(p1 = v1, p2 = v2, p3 =v3...)
kwargs:一般这样用
调用的时候，把多余的关键字参数放入kwargs
访问kwargs需要按字典格式访问
'''

#例子：自我介绍
def stu(**kwargs):
    print('hello ')
    print(type(kwargs))
    #对于字典的访问
    for k in kwargs.keys():
        print(k, "--->", kwargs[k])

stu(name = 'yanxi', age = 18, addr = 'beijing', love = 'wenheng', work = 'huajia')
print('*' * 20)
stu(name = 'jinchen')

'''
收集参数混合调用的顺序问题
收集参数，关键字参数，普通参数可以混合使用
使用规则就是普通参数和关键字参数优先
定义的一般顺序是普通参数，收集参数tuple，关键字参数，收集参数dict
'''
#例：自我介绍问题

'''
收集参数的解包问题
 把参数放入list或者dict中，直接把list/dict中的值放入收集参数中
 语法：
 
 list一个星号，dict两个星号
'''
def func(*args):
    print(type(args))
    for i in args:
        print(i)

func(1,2,'a',"abc")
l = [1,2,3,'a']
func(l)  #[1, 2, 3, 'a'] 直接输入list，会看作一个参数处理
func(*l)  #收集参数如果输出是list可以用 *list解包

def func(**kwargs):
    for k,v in kwargs.items():
        print(k, "--->", v)

func(one=1,two=2,three=3)
dict = {"name":"yanxi","age":18}
#func(dict) #TypeError: func() takes 0 positional arguments but 1 was given 字典集合参数不解包报错
func(**dict)



#函数返回值

def func(name,age):
    '''

    :param name:
    :param age:
    :return:
    '''
    pass

'''
函数的作用域
'''
'''
变量作用域
 变量的作用范围限制
 分类：
      1.全局 global：在函数外部定义
      2.局部 local：在函数内部定义
 变量作用范围
      全局：
      局部：
 LEGB原则：
     L（Local）局部作用域
     E（Enclosing function local) 外部嵌套函数作用域
     G(Global module) 函数定义所在的模块作用域
     B（Buildin）：python内置模块的作用域 
'''

#提升局部变量为全局变量，  使用global https://www.cnblogs.com/summer-cool/p/3884595.html

#globals,locals函数
#通过global和locals显示出局部变量和全局变量

#eval()函数：把一个字符串当成一个表达式执行，返回表达式执行后的结果
x = 100
y = 200
z1 = x + y
#z2 = eval(x + y) #报错TypeError: eval() arg 1 must be a string, bytes or code object
z2 = eval("x + y")
print(z1)
print(z2)

#exec 类似eval，但是没有返回结果

#递归函数
 #函数直接或者间接的调用自己
 #优点：简洁，容易理解
 #缺点：对递归深度有限制，消耗资源大
 #python中对递归深度有限制，超过限制报错
 #在写递归程序的时候，注意结束条件

x = 0
def func():
    global x
    x += 1
    print(x)
    #func()
func()


#递归的例子： 斐波那契数列
def func(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return func(n - 1) + func(n - 2)

print(func(1)) # 1
print(func(2))# 1
print(func(7))  # 13


#汉诺塔问题： 1.每次只能移动一个盘子 2.任何一次移动，三个塔的状态必须是小盘子在上，大盘子在下


def move(n,a,b,c):
    if n == 1:
        print(a, '-->', c)
        return None
    move(n - 1, a, c, b)
    print(a, '-->', c)
    move(n - 1, b, a, c)

a = 'A'
b = 'B'
c = 'C'
#move(1,a,b,c)
#move(2,a,b,c)
move(3,a,b,c)