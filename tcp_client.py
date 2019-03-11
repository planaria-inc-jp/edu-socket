import socket

PORT = 50000
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('192.168.1.13', PORT)) # 相手のIPアドレスを書く
    while True:
        # 入力したメッセージを送信
        data = input('Please input > ')
        s.send(data.encode())

        # 受信したメッセージを出力
        print(s.recv(BUFFER_SIZE).decode())
