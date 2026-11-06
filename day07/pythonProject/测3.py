zh='admin'
mn='admin888'
count=0
while count<3:
    zhanghao=input("请输入你的账号")
    mima=input("请输入你的密码")
    if zhanghao==zh:
        if mima==mn:
            print("登录成功")
        else:
            count+=1
            print(f"密码错误,您还剩下{3-count}次机会")
    else:
        count+=1
        print(f"账号错误，您还剩下{3-count}次机会")