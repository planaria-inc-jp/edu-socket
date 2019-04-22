import socket
from myapp import BaseFrame

BUFFER_SIZE = 1024

# BaseFrameを継承してアプリケーションクラスを作成
class AppFrame(BaseFrame):
    def __init__(self, master=None):
        self.connection = None
        BaseFrame.__init__(self, master)
        self.master.title('server')

    def connect(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            myip = socket.gethostbyname(socket.gethostname()) # 自分のPCのIPアドレスを取得
            self.setIp(myip)
            s.bind((myip, self.getPort())) # 自分のPCのIPアドレスを書く
            s.listen()
            self.addLog('相手を待ちます。ドキドキ…')
            (self.connection, client) = s.accept() # 受信できるまで待つ
            ip = client[0] # 接続してきた相手からIPアドレスを取得
            self.addLog(ip + 'から会話を申し込まれました。')
            try:
                while True: # 以下をずっと処理する
                    data = self.connection.recv(BUFFER_SIZE) # メッセージを受信
                    self.addLog('相手:' + data.decode())
            except ConnectionResetError as e:
                self.addLog('相手との繋がりが途切れました。')
            finally:
                self.connection.close() # 接続を閉じる

    def sendMessage(self):
        message = self.msgTextBox.get() # メッセージ入力欄からメッセージを取得
        self.connection.send(message.encode()) # メッセージを送信
        self.addLog('私:' + message)

# メイン処理
if __name__ == "__main__":
    f = AppFrame()
    f.mainloop()
