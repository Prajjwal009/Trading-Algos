from kiteconnect import KiteConnect
from kiteconnect import KiteTicker
from pprint import pprint
from datetime import datetime,timedelta
import pandas as pd
import talib


api_key=''
api_secret=''
request_token =''
#access_token='NiXixfhVBxjDDN5iv3KRdZwR7r0e7phA'
kite= KiteConnect(api_key=api_key)
data=kite.generate_session(request_token,api_secret=api_secret)
#kite.set_access_token("etmB2LOkOaNINPQal3Z8auZdqVjG2MMd")
print(data)

# token=3038209
# to_date=datetime.now()
# from_date=to_date-timedelta(days=10)
# interval="5minute"
#
#
#
#
# records=kite.historical_data(token,from_date,to_date,interval)
# df=pd.DataFrame(records)
# open=df['open'].values
# high=df['high'].values
# close=df['close'].values
# low=df['low'].values
# volume=df['volume'].values

# sma5= talib.SMA(close,5)
# sma20= talib.SMA(close,20)
#
# if sma5[-2]<sma20[-20] and sma5[-1]>sma20[-1]:
#     print("buy")
# #
# ltp=19.0

#kite.place_order(tradingsymbol="PFS",
                                   #price=ltp,
                                   #trigger_price=ltp,
                                   #variety=kite.VARIETY_REGULAR,
                                   #exchange=kite.EXCHANGE_NSE,
                                   #transaction_type=kite.TRANSACTION_TYPE_BUY,
                                   #uantity=1,
                                   #squareoff=5,
                                   #stoploss=2,
                                   #trailing_stoploss=1,
                                   #order_type=kite.ORDER_TYPE_LIMIT,
                                   #product=kite.PRODUCT_CNC)





#rint('\n')
