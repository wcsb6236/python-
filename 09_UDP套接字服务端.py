"""
UDP数据报套接字服务端
"""
from socket import *
# 1. 创建数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 2. 绑定地址
sockfd.bind(('127.0.0.1', 8888))

# 3. 消息收发
# recvfrom()功能： 接收UDP消息
# 参数： 每次最多接收多少字节
# 返回值： data 接收到的内容
# addr 消息发送方地址
while True:
    data,addr = sockfd.recvfrom(5)
    # 这里的数字是多少，就只能接受相应字节的数据，超过的部分就丢失了
    print("收到的消息:",data.decode())
    sockfd.sendto(b'Thanks',addr)
# sendto()功能： 发送UDP消息
# 参数： data 发送的内容 bytes格式
# addr 目标地址
# 返回值：发送的字节数

# 4. 关闭套接字
sockfd.close()