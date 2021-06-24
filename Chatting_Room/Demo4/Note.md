# Chatting Room

## Explanation
多人聊天室，可以讓多個clients 互相傳遞訊息，
如 client A B C 連到 server ， client A 傳一封訊息出去給 server ，server 接收後會 broadcast 給 client B C。如果打 「 send [filename]」，就會把這個file 傳出去給 server

## Use
登入 client
```
python3 client.py 192.168.0.128 7851
```

登入 server
```
python3 chat_server.py 192.168.0.128 8080
```

## 流程
Server 登入
![](./Picture/1.png)

兩個 Clients 登入（192.168.0.129 和 192.168.0.103）

Client A (192.168.0.129)
![](./Picture/2.png)

Client B (192.168.0.103)
![](./Picture/3.png)

Server 顯示兩個 Clients 成功連線
![](./Picture/4.png)

Client A (192.168.0.129) 輸入 Hello
![](./Picture/5.png)

Server 有收到，並 broadcast 給 Client B(192.168.0.103)
![](./Picture/7.png)

Client B (192.168.0.103) 成功收到
![](./Picture/6.png)

Client B (192.168.0.103) 傳送 file
![](./Picture/8.png)

Server 成功收到
![](./Picture/9.png)

Client B (192.168.0.103) 輸入 leave 離開連線
![](./Picture/10.png)

Server 也知道Client B (192.168.0.103) 離開連線
![](./Picture/11.png)