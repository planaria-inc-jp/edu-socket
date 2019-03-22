import socket
import tkinter as tk
from myapp import BaseFrame

BUFFER_SIZE = 1024

class AppFrame(BaseFrame):
    def __init__(self, master=None):
        self.connection = None
        BaseFrame.__init__(self, master)
        self.master.title('server')

    def connect(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            myip = socket.gethostbyname(socket.gethostname())
            self.setIp(myip)
            s.bind((myip, self.getPort())) # 自分のPCのIPアドレスを書く
            s.listen()
            self.addLog('相手を待ちます。ドキドキ…')
            (self.connection, client) = s.accept()
            ip = client[0]
            self.addLog(ip + 'から会話を申し込まれました。')
            try:
                while True:
                    data = self.connection.recv(BUFFER_SIZE)
                    # print(data.decode())
                    self.addLog('相手:' + data.decode())
                    # message = input("Please input > ")
            finally:
                self.connection.close()

    def sendMessage(self):
        message = self.msgTextBox.get()
        self.connection.send(message.encode())
        self.addLog('私:' + message)

if __name__ == "__main__":
    f = AppFrame()
    f.mainloop()
