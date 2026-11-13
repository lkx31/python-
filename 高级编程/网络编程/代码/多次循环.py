import socket

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.connect(("127.0.0.1", 8088))

while True:
    msg = input("请输入要发送的消息(输入exit退出): ")
    if msg == 'exit':
        break

    tcp_client.send(msg.encode('utf-8'))
    data = tcp_client.recv(1024).decode('utf-8')
    print("服务器返回:", data)

tcp_client.close()