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

#转义字符

#格式化字符
#%d 整数
#%s 字符串
s = '%s are my angle.'
print(s)  # %s are my angle. 如果后面没有跟%，%s表示字符串%s
print(s % 'you')  #you are my angle.
print(s%'you')  #you are my angle

#注意以下表达的出错原因
#如果字符串中有占位符，则有几个占位符必须用几个实际内容代替，或者一个也不要
s = 'I am %s,i am %d years old'
print(s) #I am %s,i am %d years old

#print(s%'yanxi')  #TypeError： not enough arguments for format string
#print(s%'yangxi',10) #TypeError： not enough arguments for format string

print(s%('yanxi',10)) #I am yanxi,i am 10 years old

#format 函数格式化字符串
#推荐使用
#在使用上以 {} 和：代替%，后面用format带参数完成
s = 'you are {} angle'.format('my')
print(s) #you are my angle

s = 'Yes,i am {1} years old,I love love {0} and i am {1} years old'.format('yanxi',10)
print(s)#Yes,i am 10 years old,I love love yanxi and i am 10 years old

#None 表示什么都没有
#如果函数没有返回值，可以返回None
#用来占位
#用来解除变量绑定

#内置数据结构（变量类型）list，set，tuple，dict

#3.List 列表，用中括号表示：一组有顺序的数据的组合
#range 生成一个数字序列，具体范围可以设定，注意，python中数字范围一般（range）包含左边不包含右边的数字，前闭后开
#rangeint是特别的，左右都包括

#空列表
l1 = []
print(type(l1)) #<class 'list'>
#创建带值得列表
l2 = [200]
print(type(l2)) #<class 'list'>
print(l2) #[200]
l3 = [1,2,3,4,2,4,6]
print(l3) #[1, 2, 3, 4, 2, 4, 6]
l4 = list()
print(type(l4)) #<class 'list'>
#列表访问，1.使用下标（索引） 2.

l = [1,2,5,3,2,5]
print(l[2])

#分片操作,不写左边默认为0，右边下标值加1，即取到最后一个值
print(l[1:4]) #[2, 5, 3]
print(l[:4]) #[1, 2, 5, 3]
print(l[1:]) #[2, 5, 3, 2, 5]
print(l[:]) #[1, 2, 5, 3, 2, 5]

#分片可以控制增长幅度，默认为1
print(l[1:5:1]) #[2, 5, 3, 2]

#每次增长两个
print(l[1:5:2]) #[2, 3]

#下标可以超出范围，超出后不在考虑多余的下标内容
print(l[2:10]) #[5, 3, 2, 5]
print(l[-7:10]) #[1, 2, 5, 3, 2, 5]

#负数作为下标，从右往左，从 -1 开始，分片默认从左往右
print(l[-2:10]) #[2, 5]
print(l[-4:-2]) #[5, 3]

#注意下面的执行结果
print(l[-4:-2:-1])

#分片是生成一个新的list还是截取原来的list的部分
#可以用内置函数id查看，负责显示一个变量或者数据的唯一确定编号
a = 100
b = 200
print(id(a)) #1503295648
print(id(b)) #1503298848
c = a
print(id(c)) #1503295648
a = 101
print(id(a)) #1503295680
print(id(c)) #1503295648
print(a)
print(c)

l = [1,2,3]
ll =l[:]
lll = [1,2,3]
llll = l
print(id(l)) #921050573576
print(id(ll)) #921050573576
print(id(lll)) # 788906638024
print(id(llll)) #496593890056

l[1]= 6
print(l) #[1, 6, 3]
print(llll) #[1, 6, 3]

#del删除
l = [1,2,3,4,5,6]
print(id(l)) #589957495496
del l[2]
print(l) # [1, 2, 4, 5, 6]
print(id(l)) #589957495496

#del一个变量后不能再继续使用此变量
l = [1,2]
print(l)
del l
#print(l)  #NameError: name 'l' is not defined

#列表相加
l1 = [1,2,3]
l2 = [7,8,10]
print(l1 + l2)  #[1, 2, 3, 7, 8, 10]

#使用乘号操作列表
l3 = [1,2,3]
print(l3 * 3) #[1, 2, 3, 1, 2, 3, 1, 2, 3]

#成员资格运算： 判断一个元素是否在list里面  in 和 not in
l = [1,2,3,4,5]
a = 3
b = 8
print(a in l) #True
print(a not in l) #False
print(b in l) # False
print(b not in l) #True

#遍历list，一般用for，不用while
l = [1,2,3,4]
for i in l:
    print(i)


#双层列表循环
a = [["one",1],["two",2],["three",3]]
for k,v in a:
    print(k, "----", v) #one ---- 1   two ---- 2    three ---- 3

#双层列表变异
a = [["one", 1, 'eins'], ["two", 2], ["three", 3,4,5,6]]
#for k,v in a:
#    print(k, "----", v)  #ValueError: too many values to unpack (expected 2)
a = [["one", 1, 'eins'], ["two", 2, "zwei"], ["three", 3, "drei"]]
for k,v,w in a:
    print(k,"---", v, "---", w)


#列表内涵 list content

a = ['a', 'b', 'c']
#用list a创建一个list b
#下面代码的含义是，对于所有a中的元素，逐个放入新列表b中
b = [i for i in a]
print(b) #['a', 'b', 'c']

#对a列表所有元素乘以10
a = [1,2,3,4,5]
b = [ i * 10 for i in a]
print(b) #[10, 20, 30, 40, 50]

#取a列表中偶数
a = [i for i in range(1,25)]
b = [m for m in a if m % 2 == 0]
print(b) #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]

#列表可以嵌套
a = [i for i in range(1,4)]
print(a) #[1, 2, 3]
b = [i for i in range(100,400) if i % 100 == 0]
print(b)  #[100, 200, 300]

c = [ m + n for m in a for n in b]
print(c) #[101, 201, 301, 102, 202, 302, 103, 203, 303]

#嵌套加判断
d = [ m + n for m in a for n in b if m < 3]
print(d) #[101, 201, 301, 102, 202, 302]

#list 常用函数 len，max，min，list
l = [1,2,3]
print(len(l)) #3
print(min(l)) #1
print(max(l)) #3

#list函数：将其他格式的数据转换成list，转换是可迭代的
s = "you are my angle"
print(list(s))  #['y', 'o', 'u', ' ', 'a', 'r', 'e', ' ', 'm', 'y', ' ', 'a', 'n', 'g', 'l', 'e']  空格也是字符
print(list(range(1,10))) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

#关于列表的函数
#append函数 插入一个内容
a = [i for i in range(1,10)]
print(a)
a.append(100)
print(a) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

#insert 指定位置插入 insert(index,data)
a.insert(2,99)
print(a) #[1, 2, 99, 3, 4, 5, 6, 7, 8, 9, 100]

#删除 del， pop 把最后一个元素取出来
last_ele = a.pop()
print(last_ele) #100
print(a) #[1, 2, 99, 3, 4, 5, 6, 7, 8, 9]

#remove 从列表中删除指定的值的元素:
#注：如果元素不在list内会出现什么状况，怎么解决
print(id(a)) #175305036040
a.remove(99)
print(id(a)) #175305036040
print(a) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

#clear ：清空
print(a)
print(id(a)) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
a.clear() #726842249544
print(a) #[]
print(id(a)) #726842249544

#reverse 翻转
a = [1,2,3,4]
print(id(a))
a.reverse()
print(a)
print(id(a))

#extend 扩展列表，两个列表，把一个直接拼接到后一个上

#count 查找列表中指定值（元素）的个数

#copy 拷贝，浅拷贝
#list变量是传地址操作
#深拷贝 需要特定工具

#4.元组 tuple 不可更改的list
#元组创建 t = ()
#创建一个空元组
t = ()
print(type(t)) #<class 'tuple'>

#创建一个只有一个元素的元组，需要还元素后面加，
t = (1)
print(type(t))  #<class 'int'>
t = (1,)
print(type(t)) #<class 'tuple'>
#创建多个值
t= (1,2,3,4)
print(type(t))
l = [1,2,3,4]
t =tuple(l)
print(t) #(1, 2, 3, 4)
print(type(t)) #<class 'tuple'>

#元组的特性 1.序列表，有序   2.元组数据值可以访问，不能修改  3.元组数据可以是任意类型
# 4.list所有的特性除了修改外，元组都具备，list的操作，索引，分片，序列相加，相乘，成员资格操作元组都有
t = (1,1,2,3)
print(t[2]) #2
#t[2]= 0 #TypeError: 'tuple' object does not support item assignment 元组不能修改，可以访问
#3.元组数据可以是任意类型
t = ('a',1,2)
print(type(t))
print(t) #('a', 1, 2)

#元组可以相加
t1 = (1,2,3)
t2 = (1,2,1.2)
t1 = t1 + t2
print(type(t1))
print(t1) #(1, 2, 3, 1, 2, 1.2)，这里可以赋值给t1是因为指向的不是同一块地址
#元组相乘
t = t1 * 2
print(t) #(1, 2, 3, 1, 2, 1.2, 1, 2, 3, 1, 2, 1.2)

#分片
print(t[4:])
print(t[4:3]) #()
print(t[4:6]) #(2, 1.2)
print(t[0::2]) #下标步长为2  (1, 3, 2, 1, 3, 2)
print(t[1:7:2]) #(2, 1, 1.2)
#元组成员资格运算
a = 3
print(a in t)
print(a not in t)
a = 5
print(a in t)
print(a not in t)

#元组函数 tuple ，list可以转换成tuple

#元组函数min,max，基本和list通用，除了修改函数
#如果需要查找的数字是多个，则返回第一个
#元组变量交换法
a = 1
b = 3
a,b = b,a
print(a) #3
print(b) #1

#set集合
#集合是高中数学中的一个概念
#一堆确定的无序的唯一的数据，集合中每一个数据成为一个元素
#集合的定义
s = set()
print(type(s)) #<class 'set'>
print(s) #set（）

#此时，大括号内一定要有值，否则定义的是一个dict类型
s = {1,2,3}
print(type(s))
print(s)

'''
集合的特征：
集合内数据无序，即无法使用索引和分片
集合内部袁术具有唯一性，可以也拿过来排除重复数据
集合内的数据，str，int，float，tuple，即内部只能放置可hash的数据
'''

#集合序列操作
#集合检测
#in， not in

#集合遍历操作

#集合的内涵
#普通集合内涵： 以下集合在初始化后自动过滤重复元素

#带条件的集合内涵

#多循环的集合函数

#集合函数 len，max，min 跟其他基本函数一致
#set 生成一个集合

#add 向集合内添加元素

#clear 清空数据

#copy 拷贝
#remove 移除指定的值，直接改变原有值，如果要删除的值不存在，报错
#discard 移除集合中指定的值 ，和remove一样，但是如果删除的值不存在，不报错
s = {1,23,4,3,6}
s.remove(4)
print(s)
s.discard(1)
print(s)

print("*" * 20)
s.discard(9)
print(s)
#s.remove(8)
#print(s) #KeyError:

#pop 随机移除一个元素  注：在网上查一下
s = {1,3,4,5,2}
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)

#交集  intersection
#差集 difference
#并集  union
#issubset 检查一个集合是否为另一个子集
#issuperset 检查一个集合是否为另一个超集

#集合的数字操作
#frozen set 冰冻集合 冰冻集合是不可以进行任何修改的集合，是一种特殊的集合

#6.字典 dict 字典是一种数组集合，没有顺序的数组数据，数据以键值对形式出现
#字典的创建
#创建空字典1

#创建空字典2

#用dict创建有内容字典1

#用dict创建有内容字典2，利用关键字参数

#字典的特征
#字典是序列类型，但是是无序序列，没有分片和索引
#字典中的数据每个都有键值对组成，key 可hash，value任何值

#成员检测 in， not in 检测的是key

#字典遍历
d = {"one":1,"two":2, "three":3}
for k in d:
    print(k,d[k])

for k in d.keys():
    print(k,d[k])

for v in d.values():
    print(v)

for k,v in d.items():
    print(k,'---',v)

#字典生成式
d = {"one":1,"two":2, "three":3}
dd = {k:v for k,v in d.items()}
print(dd)

d = {"one":1,"two":2, "three":3}
dd = {k:v for k,v in d.items() if v % 2 == 0}
print(dd)

#字典的相关函数 len，max，min，dict
#str(字典): 返回字典的字符串格式

#clear 清空
#items 返回字典的键值对组成的元组格式
#keys 返回字典的键组成的一个结构
#values 返回字典中值得一个结构，可迭代

#get：根据指定键返回相对应的值，，好处是可以设置默认值

#fromkeys  使用指定的序列作为键，使用一个值作为字典的所有的键的值

l = {"1","2","3"}
d = dict.fromkeys(l,"aaa")
print(d)  #{'3': 'aaa', '2': 'aaa', '1': 'aaa'}
