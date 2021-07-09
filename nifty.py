from kiteconnect import KiteConnect
import talib
import pandas as pd
import datetime
import subprocess

api_k = ""  # api_key
api_s = ""  # api_secret
access_token = 'K6UFfhq1IwHO3Lhxz6aPUhg27q9Amyaz'


def get_login(api_k, api_s):
    # print("logging into zerodha")
    global kws, kite
    kite = KiteConnect(api_key=api_k)

    # print("[*] Generate Request Token : ", kite.login_url())
    # request_tkn = input("[*] Enter Your Request Token Here : ")
    # data = kite.generate_session(request_tkn, api_secret=api_s)
    # kite.set_access_token(data["access_token"])
    # print(data['access_token'])

    kite.set_access_token(access_token)

    return kite


kite = get_login(api_k, api_s)
index=["NIFTY BANK","NIFTY AUTO","NIFTY FIN SERVICE","NIFTY FMCG","NIFTY IT","NIFTY MEDIA","NIFTY METAL","NIFTY PHARMA","NIFTY PSU BANK","NIFTY PRIVATE BANK","NIFTY REALTY"]
def get_candle_data(name, timeframe, delta):
    zrd_name = 'NFO:' + name
    to_date = datetime.datetime.now().date()
    from_date = to_date - datetime.timedelta(days=int(delta))
    token = kite.ltp(['NSE:' + name])['NSE:' + name]['instrument_token']
    data = kite.historical_data(token, from_date, to_date, timeframe)
    data = pd.DataFrame(data)
    return data

for name in index:

    try:
        spot = name

        spotlist = 'NSE:' + spot
        cd = kite.ltp([spotlist])
        ltp = cd[spotlist]['last_price']
        df = get_candle_data(name, "day", 10)
        volume=df['volume'].values
        open=df['open'].values
        print(df)

    except Exception as e:
        continue
