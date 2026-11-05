def fn1(name,age,gender):
    print(f"我的名字是{name},我的年龄是{age},我的性别是{gender}")
fn1('lkt',18,'男')


def fn2(name,age,gender):
    print(f"我的名字是{name},我的年龄是{age},我的性别是{gender}")
fn2(name='lkt',age=18,gender="男")
def fn3(*args):
    print(f"我的名字是{args[0]},我的年龄是{args[1]},我的性别是{args[2]}")

fn3('lkt',18,'男')

def fn4(**kwargs):
    print(f"我的名字是{kwargs['name']},我的年龄是{kwargs['age']},我的性别是{kwargs['gender']}")
fn4(name="lkt",age=18,gender="男")