
def func(arg=[]):
    if arg:
        arg.append(arg[0] * 2)
        
    return arg

res1 = func([10])                        
print res1                              # [10, 20]

res2 = func()
print res2                              # []

res2.append(1)

res3 = func()
print res3                              # why is it [1, 2]??
