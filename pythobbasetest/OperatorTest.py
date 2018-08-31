'''
运算符
1.算数运算符
2.比较或者关系运算符
3.赋值运算符
4.逻辑运算符
5.位运算
6.成员运算符
7.身份运算符
'''

#1.算数运算符 +，-，*(乘)，/(除)，%(取余)，//(取整),**(幂运算)
#python没有自增自减运算符
a = 10
b = 21
c = 30

print(a + b) # 31
print(a - b) # -11
print(a * b) # 210
print(b / a) # 2.1
print(c / a) # 3.0
print(b % a) # 1
print(b // a) # 2
print(b ** 3) #9261
#print(a++) #报错，python中不能自增自减


#2.比较运算符
#对两个变量或者值，对象进行比较的运算符
#比较的结果是布尔值，True/False

print(True) # True
print(False) # False

#布尔值True 表示整数 1， False 表示整数 0
print(8 + True) # 9
print(8 + False) # 8

# == 等于
a = 3 ** 4
#下面语句的执行顺序
#1. 计算a == 80
#2. 把结果放入b中
b = a == 80
print(b)  # False

# != 不等于 比较的对象，不等于也可表示为 <>
a = 8
b = 8
print(a == b) # True
print(a != b) # False

#注： == 和 is 的区别 需了解
s1 = 'yanxi'
s2 = 'yanyi'
print(s1 == s2) #False
print(s1 != s2) # True
print(s1.__eq__(s2)) # False
print(s1 is s2) #False

# > 大于， <小于，>= ,<=
a = 10
b = 23
print(a > b) #False
print(a < b) # True
print(a >= b) # False
print(a <= b) # True

#3.赋值运算符 = 赋值，+= 缩写，所有数学运算符都有缩写形式（之后写全）
# =, +=, -=, /=， *=， %=， //=，**=
a = 10 # 把数值10赋值a
print(a) # 10
a += 6  # 等价于 a =a + 6
print(a) # 16
a -= 1 # 等价于 a = a - 1
print(a) # 15
a *= 2 # a = a * 2
print(a) # 30
a /= 4 # a = a / 4
print(a) # 7.5

# % 取模 - 返回除法的余数
a %= 4 # a = a % 4
print(a) # 3.5
a  //= 2 # a = a // 2
print(a) #1.0
a  ** 6 # a = a ** 6
print(a) #1.0
b = 7
b %= 4
print(b) #3
#//取整数，向下取整
b //= 2
print(b) # 1
print(9.0//4.0) #2.0
b **= 3
print(b) # 1


#4.逻辑运算符 and 与，or 或，not 非 ,and相当于整数 * ， or 相当于整数 +
#python中没有异或运算
#逻辑运算符的短路问题,如果前面的表达式已经能确定是否为True/False,则不执行后面的表达式
#if a and b：#如果a是false，那么跳过b的判断，结果直接false
#if a or b：#如果a为true，那么跳过b的判断，直接true
#逻辑运算一般返回值为True/False
a = 3
b = 0
print(a and b) # 0
print(a or b) # 3
print(not a) #False
print(not b) #True
c = a != 3
d = b == 0
print(a and b) # 0
print(a or b) # 3
print(not a) #False
print(not b) #True
print(c and d) #False
print(c or d) # True
print(not c) #True
print(not d) #False

#5.成员运算符 in ， not in
#用来检测某一变量是否是另一个变量的成员
#返回值为True/False
a = {1,2,3,4,5}
b = 3
print(b in a) #True
print(b not in a) # False
b = 9
print(b in a) #False
print(b not in a) # True

#6. 身份运算符
#用来检测两个变量是否是同一个变量
#语法 var1 is var2 , var1 is not var2

a = 1
b = 1
print(a is b) # True
print(a is not b)#False

a = 'yanxi'
b = 'yanxi'
print(a is b) #True
print(a is not b) #False

a = b ='yanxi'
print(a is b) # True
print(a is not b) #False

#is 和 == 的区别
#is 是用来判断引用对象是否相同， == 是用来比较对象中的内容是否一样
a = [1,2,3]
b = a
print(a == b) #True
print(a is b) #True
b = a[:]
print(a == b) #True
print(a is b) # False


#7.位运算符： 把数字看成二进制数进行运算
# a = 60, b = 13
a = 0b00111100
b = 0b00001101
print(a) #60
print(b) #13
print(a & b)#12
print(a | b) #61
print(a ^ b) #49
print(not a) #Flase


#数值型 &，| 为二进制位运算
a = 10 # a = 0b1010
b = 3 # b = 0b0011
print(a & b) # 2
# print(a && b) #SyntaxError: invalid syntax 语法错误，python中没有&&
print(a | b) #11
#print(a || b) #SyntaxError: invalid syntax 语法错误，python中没有 ||

#布尔型，& 为and, | 为or
a = True
b = False
print(a & b) #False
print(a | b) #True