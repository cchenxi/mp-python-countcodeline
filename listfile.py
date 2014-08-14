import os
#导入指定项目所在目录的模块
import defineHost
#导入过滤模块
import filterDF
#导入计算单个文件代码行数的模块
import countLine

if __name__ == '__main__':
    #指定目录
    host = defineHost.defineHost()
    
    #定义行数
    allline = 0
    
    #定义需要统计的文件数
    allfiles = 0
    
    #定义过滤目录
    #directoryList = filterDF.defineDirectory()
    
    #定义过滤文件
    fileList = filterDF.defineFile()
    
    #定义后缀
    suffixList = filterDF.suffixName()
    
    for root, dirs, files in os.walk(host):
        #过滤目录    
        if root.startswith(host + os.sep + 'GUI'):
            continue
        if root.startswith(host + os.sep + 'M'):
            continue
        if root.startswith(host + os.sep + 'OOP'):
            continue
        
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
                allline += countLine.afileline(itpath)
    print('Total lines:', allline)
    print('Total files:', allfiles)