import socket
import threading
from myapp import BaseFrame

BUFFER_SIZE = 1024

# BaseFrameを継承してアプリケーションクラスを作成
class AppFrame(BaseFrame):
    def __init__(self, master=None):
        self.s = None
        BaseFrame.__init__(self, master)
        self.master.title('client')
        self.setIp('192.168.1.13')

    def connect(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.s:
                self.s.connect((self.getIp(), self.getPort())) # 相手のPCに接続
                self.addLog(self.getIp() + 'に接続します。')
                while True: # 以下をずっと処理する
                    # 受信したメッセージを出力
                    self.addLog('相手:' + self.s.recv(BUFFER_SIZE).decode())
        except ConnectionResetError as e:
            self.addLog('相手との繋がりが途切れました。')

    def sendMessage(self):
        message = self.msgTextBox.get() # メッセージ入力欄からメッセージを取得
        self.s.send(message.encode()) # メッセージを送信
        self.addLog('私:' + message)

# メイン処理
if __name__ == "__main__":
    f = AppFrame()
    f.mainloop()
