#filename:functions.py
#author:chenxi
#modified:20140831
#function:自定义函数库

import os

def defineHost():
    """
    function:定义需要统计的项目根目录
    args:无
    returns:返回项目根目录的绝对地址
    """
    str_input = input("请输入你需要计算的项目绝对路径：")   #需要一个正则表达式来确定目录的形式
    str_input = str_input.split('\\')   #将定义的目录名解析成列表，'\'
    host = ''
    for x in str_input:
        host += (os.sep + x)
    host = host[1:]     #从第二个开始取，以去掉盘符钱的os.seq
    return host

def filterFile():
    """
    functions:过滤不需要统计的文件
    args:无
    returns:返回不需要统计的文件的列表
    """
    fileNames= input('请输入需要过滤的文件，文件名之间以|隔开：')
    fileList = fileNames.split('|')
    return fileList

def filterDirectory():
    """
    functions:过滤不需要统计的目录
    args:无
    returns:返回不需要统计的目录的列表
    """
    directoryNames= input('请输入需要过滤的目录名，目录名之间以|隔开：')
    directoryList = directoryNames.split('|')
    return directoryList

def suffixName():
    """
    function:确定需要被统计的代码文件的后缀名
    args:无
    returns:返回一个由后缀名组成的列表
    """
    suffixNames = input('请输入需要统计的文件的后缀名，以|隔开：')
    suffixName = suffixNames.split('|')
    return suffixName

def aFileLine(f_path):
    """
    function:计算一个文件的行数
    args:文件的句柄
    returns:该文件中代码的行数
    """
    res = 0     #初始化行数为0
    f = open(f_path,'r')
    #遍历文件，去掉空行（空行，split函数返回假）
    for lines in f:     
        if lines.split():
            res += 1
    return res