import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib.pyplot as pylt

plt = pd.read_excel('C:\Govi\Python\productivity.xlsx', sheet_name= 'Sheet1')
plot = plt.plot(title='World Population', lw=2, colormap='jet', marker='.', markersize=10)
#print("Column Headings")
#print(df.columns)
x_axis = 0
y_axis = 0

for i in plt.index:
    #print(df['sleep'][i])
    x_axis = x_axis+plt['sleep'][i]
    y_axis = plt['freshup'][i]

print(x_axis)
#df.plot()
#plt.show()

plot.set_xlabel("Sleep")
plot.set_ylabel("rest of the time")
#plt.plot()
#plt.show()
