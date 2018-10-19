import socket

host = ''
port = 3000

log = print

# 创建一个 socket 对象
s = socket.socket()
# 绑定ip和端口
s.bind((host, port))


# 用无线循环处理请求
while True:
    # 开始监听
    s.listen(5)
    # 当有客户端过来连接的时候, s.accept 函数就会返回 2 个值
    # 分别是 连接 和 客户端 ip 地址
    connection, address = s.accept()

    # 设置一次接收的数据大小 buffer_size
    # recv 可以接收客户端发送过来的数据
    # 返回值是一个 bytes 类型
    buffer_size = 1000
    r = b''
    while True:
        request = connection.recv(buffer_size)
        r += request
        if len(request) < buffer_size:
            break

    # bytes 类型调用 decode('utf-8') 来转成一个字符串(str)
    log('ip and request, {}\n{}'.format(address, request.decode('utf-8')))

    # b'' 表示一个 bytes 对象
    response = b'<h1>Hello World!<h1>'
    # 发送响应内容给客户端
    connection.sendall(response)
    # 关闭本次连接
    connection.close()