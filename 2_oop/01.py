'''
定义一个学生类，用来形容学生
'''

#定义一个空的表
class Student():
    #定义空类，pass代表直接跳过
    #pass必须有
    pass

#定义一个对象
ming = Student()


#定义一个有描述的类，下面的类用来描述Python的学生
class PythonStudent():
    #用None给不确定的值赋值
    name = None
    age = 10
    course = "Python"

    #注意：
    #1.def doHomework 的缩进
    #2.系统默认有一个self参数
    def doHomework(self):
        print("do work")
        #推荐在函数末尾使用return语句
       # return None

print(PythonStudent.__dict__)

#实例化一个叫yueyue的学生，是一个具体的人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
#注意成员函数的调用没有传递参数
yueyue.doHomework()

