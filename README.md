# 利用IFTTT 整合 LINE 股票訊息通知

## twstock - 台灣股市股票價格擷取
https://twstock.readthedocs.io/zh_TW/latest/

```cmd
$ pip install -r requirements.txt
```

## 註冊IFTTT帳號
進入IFTTT網站 
https://ifttt.com/
輸入帳號(email)和自訂密碼。

## 建立Line與「IFTTT」的連動

點擊右上角【Explore】後，在Explore的搜尋欄位中，搜尋”line”
選擇【line】後，按下【Connect】，此時會要求輸入所要連接的Line帳號與密碼。
按下【同意並連動】，LINE 好友裡會自動多出一個名為 LINE Notify 的好友
![](https://i.imgur.com/Wmx7Ndn.png)

![](https://i.imgur.com/gnD8Baf.png)


## 創建IFTTT服務 

從下拉功能表中選擇”Create”，建立IFTTT的連動功能：設定”觸發條件”與”傳遞訊息”。

選擇【Add】
![](https://i.imgur.com/xg1lA85.png)

在搜尋欄位鍵入”webhooks”，下方即出現Webhooks服務圖案。按下【Webhooks】圖案，準備與Webhooks服務連接。
![](https://i.imgur.com/lMIZlVz.png)

選擇【Receive a web request】
![](https://i.imgur.com/nJvNk0T.png)


滑鼠點擊[+That]，即可事件觸發後的選擇服務方式。
![](https://i.imgur.com/QJVcNZx.png)

按下[Send Message]方塊。
![](https://i.imgur.com/8F2caWv.png)

按下【Create action】，進入以下畫面。表示已完成所有服務設定。
![](https://i.imgur.com/INaeyCo.png)

## 複製金鑰與網址

進入清單中的[My services]，選擇【WebHooks】，按下右上角的[Documentation]，即可查到金鑰與post服務的網址，將金鑰複製到 stock_bot.py 程式 url 裡
![](https://i.imgur.com/iZeGO7M.png)

執行
```cmd
python3 stock_bot.py
```
![](https://i.imgur.com/uTBcknh.png)
