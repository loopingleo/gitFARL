print("hello FARL")


import datetime
import pandas as pd
import quandl
import matplotlib.pyplot as plt


#irgendwas

oTime = datetime.datetime.now()
print(oTime.isoformat())

#quandl functions

mydata = quandl.get("FRED/GDP")
#normieren
mydata_pct_change = mydata.pct_change()
mydata_ind = (mydata["Value"] - mydata["Value"][1]) / mydata["Value"][1]*100.0 + 100.00


plt.plot(mydata_ind)





