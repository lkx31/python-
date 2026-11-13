import socket

# 1. 设置被控端的IP和端口
TARGET_IP = '192.168.46.38'  # 替换为被控端的真实IP！
PORT = 8888

# 2. 连接被控端
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((TARGET_IP, PORT))
    print(f"成功连接到被控端 {TARGET_IP}！")
except Exception as e:
    print(f"连接失败：{e}")
    exit()

while True:
    # 3. 输入命令
    cmd = input("\n请输入要在对方电脑执行的命令 (输入 exit 退出): ")

    if cmd.lower() == 'exit':
        client.send(cmd.encode('utf-8'))
        break

    # 发送命令
    client.send(cmd.encode('utf-8'))

    # 接收执行结果
    result = client.recv(4096).decode('utf-8')
    print("-" * 30)
    print(result)
    print("-" * 30)

client.close()