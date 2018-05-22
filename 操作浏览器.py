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
