import matplotlib.pyplot as plt
import numpy as np
import csv

fp = open('sbg.csv','r')
month = []
ac = []
dt = []
rf = []
es = []
ma = []

csvReader = csv.reader(fp)
for row in csvReader:
    month.append(row[0])
    ac.append(row[1])
    dt.append(row[2])
    rf.append(row[3])
    es.append(row[4])
    ma.append(row[5])
fp.close()

plt.figure(figsize=(15, 7), dpi=120, facecolor='white')
plt.plot(ac[1:], label='Actual Consumption', linewidth=2)
plt.plot(rf[1:],'v-', label='Random Forest', linewidth=2)
plt.plot(dt[1:],'s--', label='Decision Tree', linewidth=2 )
plt.plot(es[1:],'p:', label='Exponential Smoothing', linewidth=2)
plt.plot(ma[1:],'+:', label='Moving Average', linewidth=2)
plt.xlim(0,len(month)-1)
plt.xlabel('Month', fontsize=20)
plt.ylabel('Electrical Load (kWh)', fontsize=20)
plt.xticks(np.arange(len(month)-1), month[1:], rotation=45,)
plt.legend(loc='upper left', fontsize=15)

plt.show()