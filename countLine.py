def afileline(f_path):
    #初始化行数
    res = 0
    f = open(f_path,'r')
    for lines in f:
        #便利行数，去掉空行（空行，split函数返回假）
        if lines.split():
            res += 1
    return res