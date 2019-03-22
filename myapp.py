import tkinter as tk
from tkinter import scrolledtext as S
import threading
from abc import ABCMeta, abstractmethod

class BaseFrame(tk.Frame, metaclass=ABCMeta):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        # 接続
        rownum = 0
        ipLabel = tk.Label(text='IPアドレス').grid(row=rownum, column=0)
        self.ipTextBox = tk.Entry()
        self.ipTextBox.grid(row=rownum, column=1, sticky=tk.W, pady=10)
        portLabel = tk.Label(text='ポート番号').grid(row=rownum, column=2)
        self.portTextBox = tk.Entry()
        self.portTextBox.insert(tk.END, '9001')
        self.portTextBox.grid(row=rownum, column=3, sticky=tk.W, pady=10)
        sendButton = tk.Button(text='接続', command=self.startConncting).grid(row=rownum, column=4)

        # ログ
        rownum = rownum + 1
        tk.Label(text='ログ').grid(row=rownum, column=0)
        rownum = rownum + 1
        self.logText = S.ScrolledText(width=50)
        self.logText.grid(row=rownum, column=0, columnspan=4, padx=5, pady=10)

        # メッセージ
        rownum = rownum + 1
        msgLabel = tk.Label(text='メッセージ').grid(row=rownum, column=0)
        self.msgTextBox = tk.Entry(width=40)
        self.msgTextBox.grid(row=rownum, column=1, sticky=tk.W, columnspan=2)
        sendButton = tk.Button(text='送信', command=self.send).grid(row=rownum, column=3)

        self.master.bind('<Return>', self.eventEnter)

    def setIp(self, ip):
        self.ipTextBox.insert(tk.END,ip)
    def getIp(self):
        return self.ipTextBox.get()
    def getPort(self):
        return int(self.portTextBox.get())

    def addLog(self, log):
        self.logText.insert(1.0, log + '\r\n')

    def startConncting(self):
        thread = threading.Thread(target = self.connect, daemon= True)
        thread.start()

    def send(self):
        self.sendMessage()
        # self.msgTextBox.delete(0, tk.END)

    def eventEnter(self, event):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def sendMessage(self):
        pass
