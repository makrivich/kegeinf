def f(x):
    if x>92:return 0
    if x==92:return 1
    r=f(x+1)
    if '1' in str(x):
        r+=f(int(str(x).replace('1','2')))
    return r
print(f(11))
