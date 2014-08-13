import os

#def defineDirectory():
#    directoryList = []
#    directoryNames= input('请输入需要过滤的目录名，目录名之间以|隔开：')
#    directoryList = directoryNames.split('|')
#    return directoryList

def defineFile():
    fileList = []
    fileNames= input('请输入需要过滤的文件，文件名之间以|隔开：')
    fileList = fileNames.split('|')
    return fileList
    
#def filterDirectory(root, hostName, directoryName):
#    if root.startswith(hostName + os.sep + directoryName):
#        return True
    
def suffixName():
    suffixNames = input('请输入需要统计的文件的后缀名，以|隔开：')
    suffixName = suffixNames.split('|')
    return suffixName