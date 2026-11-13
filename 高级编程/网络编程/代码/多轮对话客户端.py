import  socket
#两个参数，socket.AF_INET表示ipv4,socket.SOCK_STREAM叫TCP协议
tcp_client=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
#链接服务器,参数是一个元组（ip地址和端口号
tcp_client.connect(("192.168.46.72",8088))
#发送消息编码
while True:
    msg=input("请输入内容(输入exit推出)")
    if msg=="exit":
        tcp_client.close()
        break
    senMsg=msg.encode('utf-8')
    tcp_client.send(senMsg)
    #接收服务器返回的消息recv(1024)每次获取1024字节
    recvMsg=tcp_client.recv(1024)
    #解码
    result=recvMsg.decode("utf-8")
    print(f"服务器放回的数据是："+result)
#释放资源
print("已经退出对话")