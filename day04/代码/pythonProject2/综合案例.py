# 案例：用for循环实现用户登录
# ① 输入用户名和密码
# ② 判断用户名和密码是否正确（username='admin'，password='admin888'）
# ③ 登录仅有三次机会，超过3次会报错
# 分析：用户登陆情况有3种:
# ① 用户名错误(此时便无需判断密码是否正确)  -- 登陆失败
# ② 用户名正确 密码错误 --登陆失败
# ③ 用户名正确 密码正确 --登陆成功 break
for i in range(1,4):
    username=input("请输入用户名：")
    password=input("请输入密码：")
    if username=='admin'and password=='admin888':
        print("密码正确")
        break
    if username=='admin' and password!='admin888':
        print(f"用户名正确 密码错误 --登陆失败,还剩下{3-i}次机会")
    if username!='admin' and password=='admin888':
        print(f"用户名不正确 密码正确 --登陆失败,还剩下{3 - i}次机会")
        continue
    if username!='admin':
        print(f"密码错误 --登陆失败,还剩下{3 - i}次机会")

