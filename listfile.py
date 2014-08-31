#filename:listfile.py(main)
#author:chenxi
#modified:20140831
#function:

import os
import functions

if __name__ == '__main__':
    allline = 0     #初始化代码行数为0
    allfiles = 0    #初始化文件数为0
    host = functions.defineHost()   #指定目录
    directoryList = functions.filterDirectory()     #定义过滤目录
    fileList = functions.filterFile()   #定义过滤文件
    suffixList = functions.suffixName()     #定义需要统计的文件后缀
    for root, dirs, files in os.walk(host):
        #过滤目录    
        #if root.startswith(host + os.sep + 'GUI'):
        #    continue       
        #过滤文件
        for afile in files:
            if afile in fileList:
                continue
            ext = afile.split('.')
            ext = ext[-1]
            if ext in suffixList:
                print(root + os.sep +afile)
                itpath = root + os.sep + afile
                allfiles += 1
                allline += functions.aFileLine(itpath)
    print('Total lines:', allline)
    print('Total files:', allfiles)