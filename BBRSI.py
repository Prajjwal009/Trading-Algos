import datetime

import pandas as pd
import talib
from kiteconnect import KiteConnect

api_k = ""  # api_key
api_s = ""  # api_secret
access_token = 'Zw85Om3UmP0qlIfQ3sWCmGzmnN8Tvuew'


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

# try:
# 	kite.profile()['user_id']  
# 	print("Login Sucessfull")
# except Exception as e:
# 	print("login error, Please login again")


watchlist = ["WIPRO", "MFSL", "RELIANCE", "PCJEWELLER", "BHEL", "TATACOMM", "IOC", "RPOWER", "AJANTPHARM", "MARUTI",
             "TATAMTRDVR", "EXIDEIND", "ICICIBANK", "MOTHERSUMI", "INDIGO", "AXISBANK", "BOSCHLTD", "BHARATFORG",
             "HEXAWARE", "TCS", "IDEA", "DHFL", "AMARAJABAT", "GAIL", "IFCI", "TECHM", "CONCOR", "SUZLON", "MINDTREE",
             "ASHOKLEY", "PFC", "REPCOHOME", "HDFC", "RECLTD", "TVSMOTOR", "TATAMOTORS", "JINDALSTEL", "SRTRANSFIN",
             "DCBBANK", "ZEEL", "ULTRACEMCO", "CHENNPETRO", "SOUTHBANK", "RBLBANK", "HINDALCO", "GSFC", "TV18BRDCST",
             "RELCAPITAL", "IRB", "TITAN", "SUNTV", "CADILAHC", "EICHERMOT", "MCDOWELL-N", "SAIL", "BEML", "MRPL",
             "GLENMARK", "CIPLA", "IDFCFIRSTB", "RAMCOCEM", "CASTROLIND", "GRASIM", "INDIANB", "IDFC", "TATAPOWER",
             "JUBLFOOD", "LT", "INFIBEAM", "ORIENTBANK", "MANAPPURAM", "TATAELXSI", "COLPAL", "HDFCBANK", "ITC",
             "ASIANPAINT", "AUROPHARMA", "PEL", "BRITANNIA", "OIL", "M&MFIN", "APOLLOTYRE", "SUNPHARMA", "ENGINERSIN",
             "CEATLTD", "DLF", "NESTLEIND", "CANBK", "NATIONALUM", "ESCORTS", "POWERGRID", "GODFRYPHLP", "GODREJCP",
             "ONGC", "MRF", "BIOCON", "M&M", "DABUR", "BHARTIARTL", "UNIONBANK", "NHPC", "VOLTAS", "BAJFINANCE",
             "RELINFRA", "BAJAJFINSV", "VEDL", "PVR", "ACC", "MGL", "BPCL", "NCC", "STAR", "HINDPETRO", "HEROMOTOCO",
             "UPL", "IDBI", "DRREDDY", "BANKINDIA", "NMDC", "HCLTECH", "DIVISLAB", "L&TFH", "CHOLAFIN", "MCX",
             "IBULHSGFIN", "ARVIND", "COALINDIA", "TATASTEEL", "INDUSINDBK", "ADANIENT", "SBIN", "VGUARD", "BAJAJ-AUTO",
             "MUTHOOTFIN", "KSCL", "GODREJIND", "LUPIN", "RAYMOND", "SHREECEM", "BATAINDIA", "KTKBANK", "JSWSTEEL",
             "GMRINFRA", "TATAGLOBAL", "HINDUNILVR", "TORNTPOWER", "TATACHEM", "BERGEPAINT", "SYNDIBANK", "LICHSGFIN",
             "CENTURYTEX", "DISHTV", "KOTAKBANK", "JISLJALEQS", "INFRATEL", "UJJIVAN", "TORNTPHARM", "AMBUJACEM", "BEL",
             "YESBANK", "BANKBARODA", "NTPC", "SRF", "WOCKPHARMA", "BALKRISIND", "NBCC", "INDIACEM", "APOLLOHOSP",
             "HINDZINC", "CESC", "FEDERALBNK", "ADANIPORTS", "IGL", "ICICIPRULI", "INFY", "CUMMINSIND", "CGPOWER",
             "PNB", "JUSTDIAL", "OFSS", "EQUITAS", "SIEMENS", "MARICO", "UBL", "PAGEIND", "PIDILITIND", "BSOFT",
             "CANFINHOME", "PETRONET", "ADANIPOWER", "HAVELLS", "KAJARIACER"]
trd_list1 = []
ltpl1 = []
trd_list2 = []
ltpl2 = []
time1 = []
time2 = []


def get_candle_data(name, timeframe, delta):
    zrd_name = 'NFO:' + name
    to_date = datetime.datetime.now().date()
    from_date = to_date - datetime.timedelta(days=int(delta))
    token = kite.ltp(['NSE:' + name])['NSE:' + name]['instrument_token']
    data = kite.historical_data(token, from_date, to_date, timeframe)
    data = pd.DataFrame(data)
    return data


while True:


    for name in watchlist:

        try:
            spot = name

            spotlist = 'NSE:' + spot
            cd = kite.ltp([spotlist])
            ltp = cd[spotlist]['last_price']
            df = get_candle_data(name, "15minute", 7)

            close = df['close'].values

            c = close[-1]
            upper, middle, lower = talib.BBANDS(close, timeperiod=20)
            mom= talib.MOM(close,)

            ri = talib.RSI(close, 14)
            rsi = round(ri[-1], 2)
            b1 = round(upper[-1], 2)
            b2 = round(middle[-1], 2)
            b3 = round(lower[-1], 2)


            # if upper[-1]>upper[-2] and lower[-1]<lower[-2] and rsi<26:
            #     print(f"{name}  bands opening and selling position appearing")




            if ltp > b1 and rsi > 75 and rsi < 80 and name not in trd_list1 and name not in trd_list2:
                print(f'sell   {name}      {ltp}       {rsi}      {datetime.datetime.now()}')
                trd_list1.append(name)
                ltpl1.append(ltp)
                time1.append(datetime.datetime.now())


            if ltp>b1 and rsi>80:
                print(f"{name}     overbought")


            if ltp < b3 and rsi < 25 and name not in trd_list1 and name not in trd_list2:
                print(f"buy   {name}    {ltp}          {rsi}   {datetime.datetime.now()}")
                trd_list2.append(name)
                ltpl2.append(ltp)
                time2.append(datetime.datetime.now())




            # # if  (ri[-1]-ri[-2])>15:
            # #
            # #     print(f"  {name}   rsi difference ")
            #
            # # if ri[-1]<ri[-2] and ri[-2]<ri[-3]:
            # #     print(f"{name} rsi dropping")
            #






        except Exception as e:
            continue
