def describe(*args, **kwargs):
    print(f"位置参数有{len(args)}")
    print(f"位置参数有{len(kwargs)}")
    print(f" / ".join(kwargs.keys()))

describe(1,'hello',3.14,name='Alice',age=25,city='Beijing')
