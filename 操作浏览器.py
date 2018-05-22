#打开浏览器三种方法

#startfile方法
'''
import os
os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
'''

#system方法(打不开)
'''
import os
os.system(r'C:\"Program Files (x86)"\"Google"\"Chrome"\"Application"\chrome.exe')
'''

#更好的解决方案webbrower
'''
import webbrowser
webbrowser.open("www.baidu.com")
'''
print ('hello python3')

print('we\'ar go to shopping')

print("我们发现这个\"地方\"不一样")

print("Hi"+" Tom")

print("Hi"+ str(5))

print (int('8')+5)

print(float(8.5)+5)

print(5+8)#加

print(9-5)#减

print(3*6)#乘

print(20/6)#除

print(1**4)#指数

var1=5
print(var1)

var2='hello'
print(var2)

var3=5+67
print(var3)

var4=print('hello python3')

condition=1
while  condition<5:
	print(condition)
	condition+=1

#一个列表，遍历列表
List1=[1,2,3,4,5,6,7,8,9]
for eachNumber in List1:
	print(eachNumber)

#用自带的range,打印10到20,range，range(i, j) produces i, i+1, i+2, ..., j-1.
for i in range(10,20):
	print (i)

#1到100的相加
sum=0
i=1
while i<101:
	sum=sum+i
	i=i+1
print(sum)

#if语句
x=5
y=8
z=4
s=5
if x<y:
	print('x小于y')
if x<y>z:
	print('x小于y，但是y大于z')
if x<=s:
	print('x=s')

#if-else
x=5
y=8
if x>y:
	print('x大于y')
else:
	print('x不大于y')

#if-elif-else
x=5
y=8
z=15
if x>y:
	print(
elif
else

