import os
def defineHost():
    str_input = input("请输入你需要计算的项目绝对目录：") 
    #需要一个正则表达式来确定目录的形式
    str_input = str_input.split('\\')
    host = ''
    for x in str_input:
        host += (os.sep + x)
    host = host[1:]
    return host