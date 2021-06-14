###### tags: `TCP/IP Protocol Suite`

# Socket Programming

## 程式說明


### 程式流程圖
![](https://i.imgur.com/p61UNPO.png)


Client: 連接到 server 後，輸入一字串後，傳送到 server 後，在接受 server 相同的字串，最後輸出字串。

Server：接受到 client 的訊號後，輸出 client 所傳入的字串，再回傳一個相同的字串給 server 。



## 執行結果與說明
1. 執行 Server.py 。
![](https://i.imgur.com/mKuE7c1.png)

2. 執行 Client.py 。
![](https://i.imgur.com/Aidmvf7.png)

3. Client 成功連接 Server 。
![](https://i.imgur.com/LRwvJrl.png)

4. Client 傳入 字串 "hello" 給 server ，並成功收到 server 相同的字串。
![](https://i.imgur.com/SMqQ4qE.png)

5. Server 成功收到 Client 的字串。
![](https://i.imgur.com/1ncykOr.png)

6. Client 傳入 字串 "exit" 給 server ，Client 離開。
![](https://i.imgur.com/aeSocIC.png)

7. Server 顯示 Client 已離線。
![](https://i.imgur.com/OOmpaS8.png)


## 遭遇的困難與解決方法

1. 我在執行時遇到： accept() fails with Operation not supported
    * solution:
        * 原本寫法：server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

        * 更改寫法：server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        * 說明：
            * socket.SOCK_DGRAM is for UDP
            * socket.SOCKSTREAM is for TCP

2. 我在執行時遇到: "ConnectionRefusedError: [Errno 111] Connection refused."
    * Solution:
        * 原本寫法：server.bind(('', port)) #Bind to the port
        * 更改寫法：server.bind(('server.bind((HOST, PORT))')
        * 說明：更改後的寫法，會讓 socket 不會這限制。如果只連接到127.0.0.1，這會讓 server 無法連接到其他不一樣的 host 。

3. 我在執行時遇到: "Network is unreachable"
```python=
SERVER_HOST = '192.168.3.139'
```

* solution: 因為我的server host 是192開頭，是私人網路，無法讓外部的 client 連接到，要用NAT轉換成公共網路，才可以成功連接。



