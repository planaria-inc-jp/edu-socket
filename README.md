# edu-socket

## TCP CUI版

* tcp_server.py (サーバ)
* tcp_client.py (クライアント)

serverを先に起動してclientを起動する。
接続できると一方ずつ交互にメッセージを送ることができる。

### tcp_server.py

```
python tcp_server.py
```

### tcp_client.py

```
python tcp_client.py
```

---

## TCP GUI版

* tcp_server_tk.py (サーバ)
* tcp_client_tk.py (クライアント)

clientとserverは同時に起動可能。
ただし、接続はserverが先。

### tcp_server_tk.py

```
python tcp_server_tk.py
```

IPアドレスは自動的に取得するので、IPアドレス欄を空欄のまま[接続]ボタンを押す。

### tcp_client_tk.py

```
python tcp_client_tk.py
```

接続する相手のIPアドレスを入力し[接続]ボタンを押す。

### myapp.py

tcp_server_tk.pyとtcp_client_tk.pyの共通処理で、tkinterのフレーム(画面)とスレッド処理を行っている。
抽象メソッドによって子クラス固有の処理を書くことができる。
子クラスではtkinterをimportする必要がない。

* send()のコメントアウトを外すことでメッセージ送信時メッセージ欄がクリアされる。
* eventEnter()のコメントを外すことによってEnterキーでメッセージ送信できる。

---

## UDP CUI版

* udp_server.py (サーバ)
* udp_client.py (クライアント)

おまけで作成したUDP通信版。
