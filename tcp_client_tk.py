import socket
import threading
import tkinter as tk
from myapp import BaseFrame

BUFFER_SIZE = 1024

class AppFrame(BaseFrame):
    def __init__(self, master=None):
        self.s = None
        BaseFrame.__init__(self, master)
        self.master.title('client')
        self.setIp('192.168.1.13')

    def connect(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.s:
                self.s.connect((self.getIp(), self.getPort())) # 相手のIPアドレスを書く
                self.addLog(self.getIp() + 'に接続します。')
                while True:
                    # 受信したメッセージを出力
                    self.addLog('相手:' + self.s.recv(BUFFER_SIZE).decode())
        except ConnectionResetError as e:
            self.addLog('切断しました。')

    def sendMessage(self):
        message = self.msgTextBox.get()
        self.s.send(message.encode())
        self.addLog('私:' + message)

if __name__ == "__main__":
    f = AppFrame()
    f.mainloop()
