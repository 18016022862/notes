#!/usr/bin/env python27
#-*- coding:utf-8 -*-

#print 'hello,%s!welcome my house'%'jack' 

#r=72
#print '%d' % r

# arr=['zhangsanfeng','lisinan']
# arr.append('jiangyuan') #末尾追加
# print arr
# arr.insert(1,'zhaowu')  #指定位置追加
# print arr
# arr.pop(1)	#删除指定位置
# print len(arr)#长度
# str="1111111111"
# print len(str)

# tuple=([1,2],)
# tuple[0][1]=3
# print tuple

#test
# L = [
    # ['Apple', 'Google', 'Microsoft'],
    # ['Java', 'Python', 'Ruby', 'PHP'],
    # ['Adam', 'Bart', 'Lisa']
# ]
# print 'Apple=%s' % L[0][0]
# print 'Python=%s' % L[1][1]
# print 'Lisa=%s' % L[2][2]

# a=-100
# print abs(a) #绝对值

# arr=[5,5,2,6,5]
# print max(arr)

# n1=255
# n2=1000
# print hex(n1)
# print hex(n2)

#定义一个函数
# def my_abs(x):
    # if x>=0:
	    # return x
    # else:
        # return -x

# a=my_abs(-1)
# print a

# def my_abs(x):
	# #isinstance(a,type) 检测输入的字符是否合法
    # if not isinstance(x,int):
        # raise TypeError(u'请输入数字')
    # if x>0:
        # return x
    # else:
        # return -x

# a=input()
# print my_abs(a)

#导入模块
# import math
# #横坐标、纵、步、角度
# def move(x,y,step,angle=0):
    # nx=x+step*math.cos(angle)
    # ny=y-step*math.sin(angle)
    # return nx,ny

# x,y=move(1000,500,60,math.pi/6)
# print (x,y) #返回值为 tuple 类型

# t=(1,2,3)
# for i in t:
    # print i
	
# import math
# a*x^2+b*x+c=0
# def quadratic(a,b,c):
    # r=b*b-4*a*c
    # x1=0
    # x2=0
    # if r<0:
        # print 'no result'
        # pass
    # elif r==0:
        # x1=-(b+math.sqrt(b*b-4*a*c))/2*a
    # else:
        # x1=-(b+math.sqrt(b*b-4*a*c))/2*a
        # x2=-(b-math.sqrt(b*b-4*a*c))/2*a
    # return x1,x2
# a=quadratic(1,-5,6)
# print a

# def calc(*numbers):
    # sum=0
    # for n in numbers:
        # sum+=n*n
    # return sum
# t=(1,5,6)
# a=calc(*t)
# print a

#关键字参数
# def person(name,age,**kw):
    # print 'name:',name,'age:',age,'other:',kw

# person('zhangsanfeng',20,sex='man')

#递归函数
# def fn(n=1):
    # if n<=1:
        # return 1
    # else:
        # return fn(n-1)*(n)
# print fn(1000) #栈溢出
# print fn(0)

# def fn(n,p):
    # if n<=1:
        # return p
    # else:
        # return fn(n-1,n*p)
# def fn_iter(m):
    # return fn(m,1)
	
# print fn_iter(1000)

#汉诺塔实现
# def move_to(fromm,to):
    # print (fromm,'->',to)

# def move(n,a,b,c):
    # if n==1:
        # move_to(a,c)
    # else:
        # move(n-1,a,b,c)
        # move_to(a,c)
        # move(n-1,c,a,b)

# move(3,'A','B','C')




