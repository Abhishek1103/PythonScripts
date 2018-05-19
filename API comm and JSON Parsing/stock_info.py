import requests
import pandas as pd
import json

apikey = "BIF6YELBOTUM7BAK"
stock_symbol = "INFY.NS"
stock_symbol = input("Enter The stock Symbol: ").strip()
url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol="+stock_symbol+"&interval=5min&apikey="+apikey
res = requests.get(url)
data = res.json()
df = pd.DataFrame.from_dict(data['Time Series (5min)'], orient='columns')
print(df)