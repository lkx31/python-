textd=open("./adadad/b.txt,","r",encoding='utf-8')
while True:
    new_textd = textd.readline()
    print(new_textd,end='')
    if new_textd=='':
        break
textd.close()

textd1=open("./adadad/b.txt,","r",encoding='utf-8')

new_textd2=textd1.readlines()
print(new_textd2)
textd1.close()