import socket
import time
# AF_INET: ipv4地址  SOCK_DGRAM:UDP协议
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 飞秋服务器地址和端口号

server = ('192.168.46.38', 2425)
# 消息内容
while True:
    content = '1:134871264:斌哥:黑马程序员:32:你好，帅哥！'
    # sendto():发送消息  注意:编码是gbk
    udp_client_socket.sendto(content.encode('gbk'), server)