def afileline(f_path):
    res = 0
    f = open(f_path,'r')
    for lines in f:
        if lines.split():
            res += 1
    return res