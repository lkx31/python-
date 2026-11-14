#引入socket
import socket
#创建服务器对象
tcp_server_socker=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#设置绑定ip和端口(ip和端口）IP绑定的是一个网段，该的网段下哪些用户可以访问
#127.1.1.0：只有我自己本机可以访问
#192.168.46.72:同网段都可以访问
#0.0.0.0 "":任何人都哦可以
tcp_server_socker.bind(("0.0.0.0",8088))
#开启监听:同时监听多少个程序
tcp_server_socker.listen(128)
#等待访问(有两个返回值）
# 参数1表示当前与某个客户对象链接soceket对象，参数2端口号
print(f"服务器已经启动了，等待客户端访问")
connect_socket,clent_port=tcp_server_socker.accept()
print(f"连接的客户端对象{connect_socket},",f"端口号{clent_port}")
#接收客户端数据
recvDate=connect_socket.recv(1024).decode("utf-8")
print(f"客户端发给服务器的数据是{recvDate}")
#服务器给客户端发送数据
senddata="我是服务器，欢迎你访问我".encode("utf-8")
connect_socket.send(senddata)
connect_socket.close()
tcp_server_socker.close()

