from kiteconnect import KiteConnect
import talib
import pandas as pd
import datetime
import subprocess

api_k = ""  # api_key
api_s = ""  # api_secret
access_token = 'KKvJb60E8Do9PPvPOgqJTuf6ib7hag3X'


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
    c=1

    for name in watchlist:

        try:
            spot = name

            spotlist = 'NSE:' + spot
            cd = kite.ltp([spotlist])
            ltp = cd[spotlist]['last_price']
            df = get_candle_data(name, "day", 300)
            close= df["close"].values
            low = df['low'].values
            high = df["high"].values
            open =df['open'].values
            vol = df['volume'].values

            ema50 = talib.EMA(close,50)
            ema200 = talib.EMA(close,200)


            upper,middle, lower= talib.BBANDS(close,timeperiod=20)
            li=[]

            # if close[-1]>close[-2] and close[-1]>close[-3] and vol[-1]>vol[-2] and vol[-1]>vol[-3]:
            #     print(name)
            #
            # else:
            #     print("*****")

            if open[-1]>close[-1] and open[-2]>close[-2] and open[-3]>close[-3]:
                print(name + "   three red candle")

            if close[-1]<lower[-1]:
                print(name + " band cross")

            else:
                print("NULL")















            # print(upper[-1],middle[-1],lower[-1],close[-1])
            # if low[-1]<middle[-1]:
            #     print(name)
            # if low[-1]<dema[-1]:
            #     print(f"{name} dema")
            # if high[-1]<upper[-1]:
            #     print(name + "  going up")












        except Exception as e:
            continue
