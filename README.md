# 利用IFTTT 發送 LINE 訊息通知

[TOC]
>Read more about here:
>https://blog.xuite.net/plcduino/blog/588955471
>https://twstock.readthedocs.io/zh_TW/latest/

## 註冊IFTTT 
進入IFTTT網站 https://ifttt.com/
輸入帳號(email)和自訂密碼。

## 建立Line與「IFTTT」的連動

點擊右上角【Explore】後，在Explore的搜尋欄位中，搜尋”line”
選擇【line】後，按下【Connect】，此時會要求輸入所要連接的Line帳號與密碼。
按下【同意並連動】，LINE 好友裡會自動多出一個名為 LINE Notify 的好友
![](https://i.imgur.com/Wmx7Ndn.png)

## 創建IFTTT服務 

![](https://i.imgur.com/INaeyCo.png)

## 複製金鑰與網址

進入清單中的[My services]，選擇【WebHooks】，按下右上角的[Documentation]，即可查到金鑰與post服務的網址

執行
```cmd
python3 stock.py
```
![](https://i.imgur.com/uTBcknh.png)
