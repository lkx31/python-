def fn1(*args, **kwargs):
    print(args)
    print(kwargs)


# 第一种方式别直接把数据发成打包好的形式
fn1(1, 2, 3, 4, name='lkt', age='18')
#第二种方式直接指（解包）
fn1(*(1,2,3,4),**{'name':'lkt'})
