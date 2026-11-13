test1=open('./adadad/a.txt','r',encoding='utf-8')

while True:

    content=test1.read(10)
    print(content,end=" ")
    if content == "":
        break
test1.close()