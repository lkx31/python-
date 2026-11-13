def check(fn):  
    def inner():
        print("登录验证")
        fn()  #coment()
    return inner
def comment():
    print("发表评论")

comment = check(comment)   # commentc=inner
comment()  #inner()
