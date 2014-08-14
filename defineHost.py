import os
def defineHost():
    str_input = input("请输入你需要计算的项目绝对目录：") 
    #需要一个正则表达式来确定目录的形式
    
    #将定义的目录名解析成列表，'\'
    str_input = str_input.split('\\')
    host = ''
    for x in str_input:
        host += (os.sep + x)
    #从第二个开始取，以去掉盘符钱的os.seq
    host = host[1:]
    return host