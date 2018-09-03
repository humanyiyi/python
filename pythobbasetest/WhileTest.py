'''
语法语义
同一语句块中缩进必须一致
三大结构
1,顺序
2.分支，
3.循环
'''

#循环： while :一般不能确定长度的循环

i = 0
while i < 10:
    print('打印:',i)
    i += 1

#如：存钱 存10000 ，年利率为6.7%，第二年连本带息一起存，依此类推，多少年可以翻倍

benqian = 100000
year = 0
while benqian < 200000:
    benqian = benqian * (1 + 0.067)
    year += 1
    print('第{0}年拿了{1}前'.format(year,benqian))

print('第{}年翻倍'.format(year))