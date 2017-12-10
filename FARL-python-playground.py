print("hello FARL")


import datetime
import pandas as pd
import quandl
import matplotlib.pyplot as plt

quandl.ApiConfig.api_key = "skVfzQSMxY-BnuR-7Zz3"

#irgendwas

oTime = datetime.datetime.now()
print(oTime.isoformat())

#quandl functions

mydata = quandl.get("FRED/GDP")
#normieren
mydata_pct_change = mydata.pct_change()
mydata_ind = (mydata["Value"] - mydata["Value"][1]) / mydata["Value"][1]*100.0 + 100.00


plt.plot(mydata_ind)


crudedata = quandl.get("EIA/PET_RWTC_D")

plt.plot(crudedata)



#Apple financials
AAPLdata = quandl.get_table('ZACKS/FC', ticker='AAPL')
AAPLdata = pd.DataFrame(AAPLdata)
list(AAPLdata.columns.values)

AAPLdata.tot_revnu
AAPLdata.per_end_date
AAPLdata.sic_code