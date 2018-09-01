'''
语法语义
同一语句块中缩进必须一致
三大结构
1,顺序
2.分支，
3.循环
'''

#循环： for循环， while循环
'''
for 变量 in 序列:
    语句1
    语句2
    ...
'''

a = [1,23,12,14,5]
for i in a:
    print('输出内容为：' ,i )
#   print(True + i) #输出是 1 + i
#   print('输出：'+ i)  #TypeError: must be str, not int

print('abc' + 'de') # abcde

'''
for-else 语句：当for循环结束的时候，会执行else语句，else可选，几乎不用
'''

'''
循环中的break，contin，pass
break：无条件结束整个循环
continue：无条件结束本次循环，重新进入下个循环
pass: 空语句，占位符，保持程序结构完整性
python中可以用下划线表示不重要的变量名称
'''

for i in range(0,10): #前闭后开
    print('ouput:', i)

for _ in range(0,5):
    print('wenheng love yanyi')
    print('wenheng love yanyi', _) #wenheng love yanyi i

for i in range(0,10,2):
    if(i == 6):
        break
    print('打印;', i) # 0,2,4

#打印奇数
for i in range(0,10):
    if(i % 2 == 0):
        continue
    print('打印：', i)#1，3，5，7，9

for i in range(0,3):
    pass #占位符，不做任何操作
print(0)