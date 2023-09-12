import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pop = pd.read_excel('C:/Users/kim96/Desktop/program/python/data/01. population_in_Seoul.xls',usecols='B,D,G,J,N',header= 2)
pop.head()
dates=pd.date_range('20130101',periods=6)
dates
np.random.randn(6,4)
df = pd.DataFrame(np.random.randn(6,4), index=dates ,columns=['A','B','C','D'])
df.head()
df.values
df['20130102':'20130104']
df.loc[dates[0]]
t =np.arange(0,12,0.01)
y=np.sin(t)
plt.figure(figsize =(10,6))
plt.plot(t,y)
plt.show()
# git test