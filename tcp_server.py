import socket

PORT = 50000
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('192.168.1.13', PORT))
    s.listen() #相手を待ちます ドキドキ
    (connection, client) = s.accept()
    print(client, 'から会話を申し込まれました。')
    try:
        while True:
            data = connection.recv(BUFFER_SIZE)
            print(data.decode())
            message = input("Please input > ")
            connection.send(message.encode())
    finally:
        connection.close()
