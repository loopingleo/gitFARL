print("hello FARL")


import datetime
import pandas as pd
import quandl
import matplotlib.pyplot as plt
import bs4 as bs
import pickle
import requests

#import matplotlib
#matplotlib.use('TkAgg')

import os
f = open(os.path.expanduser("~/PycharmProjects/gitFARL/quandlapikey.txt"), "r")
f.read()

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


plt.interactive(True)
plt.plot(mydata_ind)


crudedata = quandl.get("EIA/PET_RWTC_D")

plt.plot(crudedata)


#Apple financials
AAPLdata = quandl.get_table('ZACKS/FC', ticker='AAPL', api_key="")
AAPLdata = pd.DataFrame(AAPLdata)
list(AAPLdata.columns.values)
AAPLdata

AAPLdata.tot_revnu[1:6].plot()
AAPLdata.per_end_date
AAPLdata.sic_code

AAPLdata.cash_flow_oper_activity.plot()
AAPLdata.cash_flow_invst_activity

FCF = AAPLdata.cash_flow_oper_activity[7:] - AAPLdata.cash_flow_invst_activity[7:]
FCF.plot()
FCFmargin = FCF / AAPLdata.tot_revnu[7:] /10
FCFmargin.plot()

FCFtoTA = FCF / AAPLdata.tot_asset[7:]
FCFtoTA.plot()


sp500_tickers = save_sp500_tickers()
sp500_tickers[9]

sp500_tickers[3]



## ------------------------- Quandl Data --------------------------------------------



output = pd.DataFrame()

for i in range(0,505):
    ticker = sp500_tickers[i]
    try:
        data = quandl.get_table('ZACKS/FC', ticker=ticker, api_key="")
        data = pd.DataFrame(data)


        #data.per_end_date
        #data.sic_code


        FCF = data.cash_flow_oper_activity[7:8] - data.cash_flow_invst_activity[7:8]
        FCFmargin = FCF / data.tot_revnu[7:8] /10
        FCFtoTA = FCF / data.tot_asset[7:8]


        df = pd.DataFrame([[ticker, FCF[7], round(100*FCFmargin[7],2), round(100*FCFtoTA[7],2)]],
                              columns=["ticker", "FCF", "FCFmargin", "FCFtoTA"])

        output = output.append(df, ignore_index=True)
    except:
        pass


output.to_csv("quandl_sp500.csv")






## ------------------------- PyFinData --------------------------------------------


financials_download(ticker,report,frequency)
financials_download("AAPL","cf","A").loc["Free cash flow"]["2017-09"]
pd.DataFrame(financials_download("vow3", "cf", "A").loc["Free cash flow"]).iloc[0][0]

free_cash_flow("AAPL", "2017-12-31")


output = pd.DataFrame()

for i in range(0,50):
    ticker = sp500_tickers[i]
    #print(ticker)
    #fcf = pd.DataFrame(financials_download(ticker,"cf","A").loc["Free cash flow"]).iloc[0][0]
    try:
        fcf_0 = pd.DataFrame(financials_download(ticker, "cf", "A").loc["Free cash flow"]).iloc[0][0]
        #fcf_1 = pd.DataFrame(financials_download(ticker, "cf", "A").loc["Free cash flow"]).iloc[1][0]
        #fcf_2 = pd.DataFrame(financials_download(ticker, "cf", "A").loc["Free cash flow"]).iloc[2][0]
        #fcf_3 = pd.DataFrame(financials_download(ticker, "cf", "A").loc["Free cash flow"]).iloc[3][0]
        rev_0 = pd.DataFrame(financials_download(ticker, "is", "A").loc["Revenue"]).iloc[0][0]
        #rev_1 = pd.DataFrame(financials_download(ticker, "is", "A").loc["Revenue"]).iloc[1][0]
        #rev_2 = pd.DataFrame(financials_download(ticker, "is", "A").loc["Revenue"]).iloc[2][0]
        #rev_3 = pd.DataFrame(financials_download(ticker, "is", "A").loc["Revenue"]).iloc[3][0]
        #netincome = pd.DataFrame(financials_download(ticker, "is", "A").loc["Net income"]).iloc[0][0]
        #print(ticker, ": ", fcf, " Rev: ", rev, fcf/rev)
        #print(ticker, "fcf margin: ", round(100*fcf / rev, 2))
        df = pd.DataFrame([[ticker,
                            fcf_0,#fcf_1,fcf_2,#fcf_3,
                            rev_0,#rev_1,rev_2,#rev_3,
                            round(100*fcf_0 / rev_0, 2),#round(100*fcf_1 / rev_1, 2),
                            #round(100*fcf_2 / rev_2, 2),
                            #round(100*fcf_3 / rev_3, 2),
                            ]],
                          columns=["ticker",
                                   "fcf_0", #"fcf_1","fcf_2",#"fcf_3",
                                   "rev", #"rev-1", "rev-2",#"rev-3",
                                   "fcf_margin_0", #"fcf_margin_1","fcf_margin_2",#"fcf_margin_3",
                                   #"netincome"
                                   ])
        output = output.append(df, ignore_index=True)
    except:
        pass


output.to_csv("financials_sp500.csv")


ratios_download("AAPL").loc["Free Cash Flow USD Mil"].iloc[0]