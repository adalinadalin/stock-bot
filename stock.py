import twstock
import requests
#twstock.realtime.mock = False  # 使用正常資料
stock_code_dict = {"2330": "600", "2303": "51", "4743":"-", "2881":"-"}
line_message = ''
stock_price = []
for i in stock_code_dict.items():

    stock = twstock.Stock(i[0])
    recommended_price = i[1]
    stock_price = stock.price
    stock_id = stock.sid
    stock_price_len = len(stock_price)
    lastClose_price = stock_price[stock_price_len-2] # 昨收
    close_price = stock_price[stock_price_len-1] # 收盤
    stoc_info = twstock.realtime.get(i[0])    # 擷取當前股票資訊
    #print(stock)
    name = stoc_info.get('info').get('name')
    message = ''
    rise = round(close_price - lastClose_price, 2)
    amplitude = round((rise/lastClose_price) * 100, 3)
    message = '\n' + '股票名稱： ' + name  + '\n' + '股票代號： ' + str(stock_id) + '\n'+ '建議： ' + recommended_price + '\n'  + '昨收： ' + str(lastClose_price) + '\n' + '成交價格： ' + str(close_price) + '\n' + '漲跌： ' + str(rise) + '\n' + '幅度： ' + str(amplitude) + '\n'

    line_message = line_message + message
    
print(line_message)

url = 'https://maker.ifttt.com/trigger/line/with/key/金鑰'
myobj = {'value1':line_message}

x = requests.post(url, data = myobj)
print(x.text)

