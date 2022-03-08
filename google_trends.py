import pandas as pd
import matplotlib.pyplot as plt
from pytrends.request import TrendReq

pytrends = TrendReq()

kw_list = ["python","java","javascript","visual-basic"]

pytrends.build_payload(kw_list, cat= None, timeframe="2010-01-01 2022-01-01" , geo ="US")

df =pytrends.interest_over_time()
df.to_excel("us_prog_lang_trends.xls")

plt.figure(figsize=(10,8))
plt.plot(df.index,df.python,"k*")
plt.plot(df.index,df.java,"r*")
plt.plot(df.index,df.javascript,"b*")
plt.plot(df.index,df["visual basic"],"g*")
plt.legend(["python","java","javascript","visual-basic"])
plt.show()