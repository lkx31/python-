1.概念 : 本质上 装饰器目的, 在不修改源代码的情况下 对方法进行增强.不入侵代码

2.通用语法: 

```
def 外部函数名称(外部传入的函数):
	def 内部函数名称(*args , **kwargs):
		在执行原函数之前 书写增强代码 
		result = 外部传入的函数(*args , **kwargs)  # 本质调用原函数
		在执行原函数之后 书写增强代码
		return result
	return 内部函数名称
	
```









# 1. 计算机网络概述

## 学习目标

1、了解计算机网络相关信息

2、掌握Python3编码转换的方法

3、掌握TCP客户端及服务器端开发流程及应用实践

4、socket套接字之send和recv原理剖析

5、掌握网络综合案例：多任务版TCP服务端程序应用实践

## 1.1 网络的概念

HTTP : 协议  超文本传输协议 , 规范数据传输格式

​	请求协议: 客户端给服务器 request

​		请求行: 请求方式 请求路径 (get/post)

​			get 查询 post 新增 put 修改 delete 删除

​		请求头: 浏览器传输服务器的本地信息

​		==请求体 : 请求的数据(客户端真实需要传输的数据)==

​	响应协议: 服务器给客户端 response

​		响应行: 状态码

​			1xx 2xx 3xx 4xx 5xx  

​			200 : 表示响应成功 

​			304 : 表示本地有缓存 加快查询效率

​			404 : 表示服务器资源找不到

​			500 : 服务器代码报错了

​		响应头: 服务器传给浏览器一些特殊信息

​		响应体: 响应正文 网页上真正需要展示的内容 就是代码





网络三要素: 协议 ip 端口

ip: 任何一个机器 都有唯一的ip地址  找电脑 相当于找ip

端口: 用来区分 电脑中的软件程序

协议: 规范 客户端和服务器之间 应该如何进行数据传输



协议 ip 端口   www.baidu.com -> 域名  端口在互联网默认可以省略的

http://www.baidu.com:80

https://www.baidu.com:443  

http://127.0.0.1:端口

http://localhost:端口

https:// 加密协议 443   http:// 不加密协议  80



扩展:  通过代码访问服务器资源

```
# 安装: requests模块  pip install requests
# 导包
import requests
# 访问百度服务器
# 1.准备有效,俗称网址
# url:统一资源定位符   域名: 可以认为就是ip地址的别名
url = "https://www.baidu.com/"
# 2.发送请求
responses = requests.get(url)
print(responses)
print(responses.content)
print(responses.content.decode())
```

网络就是将具有独立功能的多台计算机通过通信线路和通信设备连接起来，在网络管理软件及网络通信协议下，实现资源共享和信息传递的虚拟平台。

![1781337612404](assets/1781337612404.png)

## 1.2 为什么要学习网络

学习网络的目的就是能够编写基于网络通信的软件或程序，通常来说就是网络编程。

![1781337618689](assets/1781337618689.png)

## 1.3 IP地址概述

思考一个问题，当我们在计算机中使用微信和你心中那个“她”聊天时，信息是如何精准的传递到她的计算机中的呢？

![1781337623751](assets/1781337623751.png)

### 1.3.1 IP地址的作用

通过IP地址找到网络中唯一一台设备，然后可以跟这个设备进行数据通信。

![1781337630820](assets/1781337630820.png)

答：是通过计算机的IP地址来实现的，IP地址是分配给网络设备上网使用的数字标签，它能够标识网络中唯一的一台设备，好比现实中每个人都有一个手机号。

![1781337637233](assets/1781337637233.png)

### 1.3.2 IP地址的表现形式

![1781337645203](assets/1781337645203.png)

IP地址一共有4位，第1位，1~223，第234位，0~255

注意事项： 192.168.46.72

① IP地址分为两类 : IPv4和IPv6

② IPv4是目前使用的IP地址

③ IPv6是未来使用的IP地址

## 1.4 端口和端口号的概念

### ☆ 计算机通信原理

问题：如果在一台电脑上使用飞秋给另外一台电脑上的飞秋发送数据并且另外的这台电脑还运行着多个软件，它是如何区分这多个软件把数据给飞秋的呢?

![1781337665595](assets/1781337665595.png)

答：其实，每运行一个程序都会有一个端口，想要给对应的程序发送数据，找到对应的端口即可。端口就是传输数据的通道，好比教室的门，是数据传输必经之路。

![1781337672935](assets/1781337672935.png)

而且每一个端口都会有一个对应的端口号（操作系统为了统一管理这么多端口，就对端口进行了编号，这就是端口号，端口号其实就是一个数字，好比我们现实生活中的门牌号），想要找到端口通过端口号即可，如：飞秋软件的默认端口号就是2425。

![1781337679198](assets/1781337679198.png)

最终通信结果：通过ip地址找到对应的设备，通过端口号找到对应的端口，然后通过端口把数据给应用程序。

![1781337684294](assets/1781337684294.png)

### ☆ 扩展：端口号扩展

① 知名端口号

知名端口号是指众所周知的端口号，范围从0到1023，这些端口号一般固定分配给一些服务，比如21端口分配给FTP（文件传输协议）服务，22端口分配给SSH（安全外壳协议，主要用于远程连接与文件传输），25端口分配给SMTP（简单邮件传输协议）服务，80端口分配给HTTP服务，443端口分配给HTTPS服务等等。





② 动态端口号

一般程序员开发应用程序使用端口号称为动态端口号。

动态端口号的范围是从1024到65535，如果程序员开发的程序没有设置端口号，操作系统会在动态端口号这个范围内随机生成一个给开发的应用程序使用。

> 注意：当运行一个程序默认会有一个端口号，当程序退出时，所占用的这个端口号就会被释放。

```markdown


注册端口（1024 - 49151）特点：需要向IANA（互联网数字分配机构）申请注册才能正式使用，但实际开发中很多软件不注册就直接用了。
- **3306**：MySQL数据库
- **6379**：Redis缓存
- **11434**：ollama的端口

动态/私有端口（49152 - 65535）—— “临时访客证”级别
特点：不需要申请，系统自动分配，用完就回收。
```









设置端口建议8000以后

## 1.5 TCP协议概述

### ☆ 为什么需要TCP协议

之前我们学习了IP地址和端口号，通过IP地址能够找到对应的设备，然后再通过端口号找到对应的端口，再通过端口把数据传输给应用程序，这里要注意，数据不能随便发送，在发送之前还要选择网络传输方式（传输协议），保证程序之间按照指定的传输规则进行数据的通信。

![1781337691082](assets/1781337691082.png)

### ☆ TCP概述

TCP的英文全拼(Transmission Control Protocol)简称传输控制协议，它是一种面向连接的、可靠的、基于字节流的传输层通信协议。==核心目的: 传输数据==

![1781337696431](assets/1781337696431.png)

TCP通信步骤：① 创建连接 ② 传输数据 ③ 关闭连接

TCP通信模型相当于生活中的’打电话‘，在通信开始之前，一定要先建立好连接，才能发送数据，通信结束要关闭连接。

### ☆ TCP的特点

#### ① 面向连接

通信双方必须先建立好连接才能进行数据的传输，并且双方都会为此连接分配必要资源用来记录连接的状态和信息。当数据传输完成后，双方必须断开此连接，以释放系统资源。

![1781337705212](assets/1781337705212.png)

#### ② 可靠传输

(基于三次握手 四次挥手)

##### **☆ TCP采用发送应答机制**

通过TCP这种方式发送的每个报文段都必须得到接收方的应答才认为这个TCP报文段传送成功

##### **☆ 超时重传**

发送端发送一个报文之后就会启动定时器，如果指定时间内没有得到应答就会重新发送这个报文段

##### **☆ 错误校验**

TCP用一个校验和函数来校验数据是否有错误，在发送和接收时都要计算校验和

##### **☆ 流量控制和阻塞管理**

流量控制用来避免发送端发送过快而使得接收方来不及接收

### 扩展：UDP协议（不可靠传输协议）

TCP可靠协议（数据可以100%传输）

日常通信、数据传输一定要保证可靠性，使用TCP。

UDP不可靠协议（只能保证速度，但是没办法保证数据传输质量，发送5M => 接收3.75M）

有些情况下，我们对数据的质量没有要求，可以考虑使用UDP，如视频通话。

**SMTP负责“发邮件”**  



# 2. Python3编码转换

## 学习目标

掌握Python3编码转换的方法

## 2.1 为什么要学习编码转换

在计算机网络中，数据都是以二进制的形式进行传输的。所以在网络传输数据的时候，数据需要先编码转化为二进制（bytes）数据类型

I Love Python => 字符串 => 转换为二进制数据 => 网络中传输

## 2.2 数据的编码转换

![1781337716731](assets/1781337716731.png)

数据转换方法说明：

| 函数名 | 说明                      |
| :----- | :------------------------ |
| encode | 编码 将字符串转化为字节码 |
| decode | 解码 将字节码转化为字符串 |

提示：encoed()和decode()函数可以接受参数，encoding是指在编解码过程中使用的编码方案。

字符串编码：

```
str.encode(encoding=”utf-8”)
```

二进制解码：

```
bytes.decode(encoding=“utf-8”)
```



```python
# 编码
data = "我喜欢你好久了".encode("utf-8")
print(data)

# 解码
data = data.decode("utf-8")
print(data)

```



# 3. socket网络编程

## 学习目标

1、了解计算机网络相关信息

2、掌握Python3编码转换的方法

3、掌握TCP客户端及服务器端开发流程及应用实践

4、socket套接字之send和recv原理剖析

5、掌握网络综合案例：多任务版TCP服务端程序应用实践

## 3.1 socket套接字

### 3.1.1 目前存在的问题

到目前为止我们学习了IP地址和端口号，使用这些我们就可以在茫茫的网络海洋中进行畅游了么？

答案是否定的！

![1781337727772](assets/1781337727772.png)

### 3.1.2 socket套接字

那我们需要什么工具呢？答：socket套接字工具，它是计算机之间进行**通信**的**一种约定**或一种方式。通过 socket 这种约定，一台计算机可以接收其他计算机的数据，也可以向其他计算机发送数据。

这就好比现实中的电话，当知道了对方的电话号码后需要使用电话才能进行通讯，程序之间想要进行网络通信需要基于这个socket套接字，socket套接字就是正在运行中的程序间进行网络通讯的工具。

![1781337732770](assets/1781337732770.png)

### 3.1.3 socket使用场景

不夸张的说，只要跟网络相关的应用程序或者软件都使用到了socket。

![1781337742478](assets/1781337742478.png)

## 3.2 TCP客户端及服务器端开发实践

### 3.2.1 TCP网络应用程序开发分类

① TCP客户端应用程序开发

② TCP服务器端应用程序开发

客户端程序是指运行在用户设备上的程序，服务端程序是指运行在服务器设备上的程序，专门为客户端提供数据服务。那如何记忆呢？

> 主动发起建立连接请求的是客户端程序，等待接受连接请求的是服务端程序。

### 3.2.2 TCP客户端程序开发流程及应用实践（五步走）

#### ☆ 开发流程介绍

![1781337762596](assets/1781337762596.png)

#### ☆ socket类的介绍

```
① 导入socket模块
import socket

② 创建客户端socket对象使用socket类
socket.socket(AddressFamily, Type)
```

客户端socket类的参数和方法说明：

| 参数名        | 说明                       |
| :------------ | :------------------------- |
| AddressFamily | IP地址类型, 分为IPv4和IPv6 |
| Type          | 传输协议类型               |

开发客户端需要使用的函数：

![1781337778211](assets/1781337778211.png)

#### ☆ TCP客户端程序开发实践

>1、创建客户端套接字对象
>
>2、和服务器端套接字建立连接(参数必须是一个元祖)
>
>3、发送数据
>
>4、接收数据
>
>5、关闭客户端套接字

socket(socket.AF_INET, socket.SOCK_STREAM)

参数1:  `AF_INET`：IPv4；`AF_INET6`：IPv6  

参数2:

​            `SOCK_STREAM`：TCP，可靠、有序、有连接

​          ` SOCK_DGRAM`：UDP，不可靠、无连接



connect((参数1, 参数2)) : 

参数1: host  设置连接主机地址 

参数2: port 设置连接端口





send(参数1):  

参数1:  发送的数据

recv:`buffer_size` 单次最大读取字节数（如 1024、4096） 

阻塞特性：默认**阻塞 IO**，无数据时卡住等待

```
import socket

if __name__ == '__main__':
    # 1、创建客户端套接字对象
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2、和服务器端套接字建立连接(参数必须是一个元祖)
    tcp_client_socket.connect(("192.168.31.181", 8080))
    # 3、发送数据
    tcp_client_socket.send('hell, itheima'.encode(encoding='utf-8'))
    # 4、接收数据
    recv_data = tcp_client_socket.recv(1024).decode('utf-8')
    print(recv_data)
    # 5、关闭客户端套接字
    tcp_client_socket.close()
```

使用网络调试查看，效果如下图所示：

![1782987082746](assets/1782987082746.png)

### 3.2.3 TCP服务器端开发流程及应用实践(七步走)

#### ☆ 服务器端

![1781337796260](assets/1781337796260.png)

#### ☆ 开发流程介绍

![1781337813864](assets/1781337813864.png)

#### ☆ socket类的介绍

```
① 导入socket模块
import socket

② 创建客户端socket对象使用socket类
socket.socket(AddressFamily, Type)
```

客户端socket类的参数和方法说明：

| 参数名        | 说明                            |
| :------------ | :------------------------------ |
| AddressFamily | IP地址类型, 分为TPv4和IPv6      |
| Type          | 传输协议类型 可以设置TCP或者UPD |

开发客户端需要使用的函数：

```
① 导入socket模块
import socket

② 创建服务器端socket对象使用socket类
socket.socket(AddressFamily, Type)
```

客户端socket类的参数和方法说明：

| 参数名        | 说明                       |
| :------------ | :------------------------- |
| AddressFamily | IP地址类型, 分为TPv4和IPv6 |
| Type          | 传输协议类型               |

开发服务器端需要使用的函数：

| 方法名 | 说明                                                         |
| :----- | :----------------------------------------------------------- |
| bind   | 绑定IP地址和端口号                                           |
| listen | 设置监听                                                     |
| accept | 等待接受客户端的连接请求(阻塞函数，直到三次握手完成的客户端到来) |
| send   | 发送数据                                                     |
| recv   | 接收数据                                                     |

#### ☆ TCP服务器端程序开发实践

>1、创建服务器端套接字对象
>
>2、绑定IP地址与端口号
>
>3、开启监听
>
>4、等待接收客户端连接请求
>
>5、接收数据
>
>6、发送数据
>
> 7、关闭套接字

tcp_sock.bind((参数1 , 参数2))

参数1: "0.0.0.0" 绑定地址

参数2: 8080  绑定端口

accept() 返回值 :     返回值1  与客户端通信的新套接字     返回值2    客户端(IP,端口)

listen (backlog) 开启监听   参数:全连接队列最大容量（等待 accept 的连接数）

```
import socket

if __name__ == '__main__':
    # 1、创建服务器端套接字对象
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2、绑定IP地址与端口号 127.0.0.1  0.0.0.0   192.168.34.101
    tcp_server_socket.bind(("", 8888))
    # 3、开启监听
    tcp_server_socket.listen(128)
    # 4、等待接收客户端连接请求
    conn_socket, ip_port = tcp_server_socket.accept()
    print('客户端IP+端口：', ip_port)
    # 5、接收数据
    recv_data = conn_socket.recv(1024)
    print('接收到的数据：', recv_data.decode())
    # 6、发送数据
    conn_socket.send("客户端的数据已经收到了".encode())
    # 7、关闭套接字
    conn_socket.close()
    tcp_server_socket.close()
```

### 3.2.4 扩展：TCP服务器端开发之多轮对话

服务端开发

>1.创建服务器
>
>2.绑定地址与端口
>
>3.开启监听 参数是最大监听数
>
>4.等待客户端连接
>
>5.接受客户端数据
>
>6.发送数据

```python
# 引入套接字
import socket
# 1.创建socket 套接字对象
tcp_server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
# 2.绑定主机的ip和端口
tcp_server_socket.bind(("127.0.0.1" , 8888))
# 3.开启监听
tcp_server_socket.listen(128)
# 4.等待连接 返回值 (socket object, address info)
print("服务器准备完成!! 开始等待客户端连接")
while True: # 为了接收多个客户端连接  挨个对话  无法做到 同时对话
    connect_socket , ip_port = tcp_server_socket.accept()


    print(f"连接的对象:{connect_socket} 端口号是: {ip_port}")
    try:
        while True: # 为某一个客户端实现多轮对话的窗口
            # 5.接收客户端数据 接收1024个字节
            recvData = connect_socket.recv(1024).decode("utf-8")
            print(f"服务器接收的数据为:{recvData}")

            # 如果接收到发送的最后 一条消息为空 表示客户端已经要关闭了
            if recvData =='' : # or len(recvData)==0  or recvData is None
                print("客户端关闭,服务器当前关闭")
                connect_socket.close()  # 关闭当前与某个客户端的对话
                break

            # 6.发送数据
            s = input("请输入要发送给客户端的消息:")
            sendData = s.encode("utf-8")
            connect_socket.send(sendData)
    except:
        print("程序出现异常情况")
        connect_socket.close() #异常之后需要释放资源

# 7.关闭 释放资源
tcp_server_socket.close() # 释放服务器资源 关闭整个服务器
```

客户端开发

```python
# 引入套接字
import socket

# 1.创建套接字对象  设置协议使用的ipv4地址  使用的是tcp协议 也可以不传 有默认值
tcp_client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)


# 2.连接服务器 连接服务器: 需要知道服务器的ip和端口  ip地址是字符串 端口是整型
tcp_client_socket.connect( ('127.0.0.1' , 8888) )


print("连接成功后 输入exit退出对话")
while True:
    # 3.发送数据 此处发送数据有编码的问题
    s = input("请输入您要发送给服务器的消息:")

    if s=='exit':# 表示客户端需要退出
        break


    sendData = s.encode('utf-8')
    tcp_client_socket.send( sendData )

    # 4.接收服务器响应的结果
    recvData  = tcp_client_socket.recv(1024)
    # 解码
    recvData = recvData.decode("utf-8")
    print(f"服务器响应的数据为:{recvData}")





# 5.关闭
tcp_client_socket.close()
```







### 3.2.5 TCP网络应用程序开发注意点

![1781337830645](assets/1781337830645.png)

端口复用：

```
import socket

if __name__ == '__main__':
    # 1、创建服务器端套接字对象
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 2、绑定IP地址与端口号
    tcp_server_socket.bind(("", 8888))
    # 3、开启监听
    tcp_server_socket.listen(128)
    # 4、等待接收客户端连接请求
    conn_socket, ip_port = tcp_server_socket.accept()
    print('客户端IP+端口：', ip_port)
    # 5、接收数据
    recv_data = conn_socket.recv(1024)
    print('接收到的数据：', recv_data.decode())
    # 6、发送数据
    conn_socket.send("客户端的数据已经收到了".encode())
    # 7、关闭套接字
    conn_socket.close()
    tcp_server_socket.close()
```

### 3.2.6 扩展：飞秋消息

```
content = '1:134871264:斌哥:黑马程序员:32:你好，帅哥！'


[0] 消息类型：'1'
[1] 发送者ID：'134871264'
[2] 发送者昵称：'斌哥'
[3] 群组或组织名称：'黑马程序员'
[4] 接收者ID：'32'
[5] 消息正文：'你好，帅哥！'

0.消息类型 (1)
    表示消息的类别。例如：1 可能表示文本消息；
    其他值可能代表文件传输、表情包等不同消息类型。
1. 发送者ID (134871264)
    标识发送者的唯一用户ID，在局域网内用于识别不同的用户。
2.发送者昵称 (斌哥)
    发送者的显示昵称，接收方可以直观地看到是谁发送的消息。
3.群组或组织名称 (黑马程序员)
    表示发送者所属的群组或者组织，用于标识团队或单位。
4.接收者ID (32)
    标识目标接收者的唯一用户ID，用于点对点通信时指定接收方。
5.消息正文 (你好，帅哥！)
    实际要发送的文本内容，可以是聊天信息或其他数据
```

点对点消息：

```
import socket
# AF_INET: ipv4地址  SOCK_DGRAM:UDP协议
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 飞秋服务器地址和端口号
server = ('192.168.109.58', 2425)
# 消息内容
content = '1:134871264:斌哥:黑马程序员:32:你好，帅哥！'
# sendto():发送消息  注意:编码是gbk
udp_client_socket.sendto(content.encode('gbk'), server)
```

群发消息：

```
import socket
# AF_INET: ipv4地址  SOCK_DGRAM:UDP协议
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# TODO 设置广播SO_BROADCAST
udp_client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# 飞秋服务器地址和端口号
server = ('192.168.109.255', 2425)
# 消息内容
content = '1:134871264:斌哥:黑马程序员:32:你好，帅哥！'
# sendto():发送消息  注意:编码是gbk
udp_client_socket.sendto(content.encode('gbk'), server)
```