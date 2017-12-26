print("hello FARL")


import datetime
import pandas as pd
import quandl
import matplotlib.pyplot as plt
import bs4 as bs
import pickle
import requests

import matplotlib
matplotlib.use('TkAgg')

import os
#f = open(os.path.expanduser("~/PycharmProjects/gitFARL/quandlapikey.txt"))

#api_key = open(os.path.expanduser("~/PycharmProjects/gitFARL/quandlapikey.txt"), "r").seek(-1,2).read()
#quandl.ApiConfig.api_key = your quandl api key



def save_sp500_tickers():
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'}
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies',
                        headers=headers)
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)
    with open("sp500tickers.pickle","wb") as f:
        pickle.dump(tickers,f)

    return tickers


#irgendwas

oTime = datetime.datetime.now()
print(oTime.isoformat())

#quandl functions

mydata = quandl.get("FRED/GDP")
#normieren
mydata_pct_change = mydata.pct_change()
mydata_ind = (mydata["Value"] - mydata["Value"][1]) / mydata["Value"][1]*100.0 + 100.00


plt.interactive(False)
plt.plot(mydata_ind)


crudedata = quandl.get("EIA/PET_RWTC_D")

plt.plot(crudedata)

plt.show()


#Apple financials
AAPLdata = quandl.get_table('ZACKS/FC', ticker='AAPL')
AAPLdata = pd.DataFrame(AAPLdata)
list(AAPLdata.columns.values)

AAPLdata.tot_revnu
AAPLdata.per_end_date
AAPLdata.sic_code

AAPLdata.cash_flow_oper_activity.plot()
AAPLdata.cash_flow_invst_activity

FCF = AAPLdata.cash_flow_oper_activity - AAPLdata.cash_flow_invst_activity
FCF.plot()
FCFmargin = FCF / AAPLdata.tot_revnu /10
FCFmargin.plot()

FCFtoTA = FCF / AAPLdata.tot_asset
FCFtoTA.plot()


sp500_tickers = save_sp500_tickers()
sp500_tickers[9]

sp500_tickers[3]