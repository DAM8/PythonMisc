import pandas as pd
import matplotlib.pyplot as plt
import base64
from pandas import ExcelWriter
from pandas import ExcelFile

#df = pd.read_excel('C:\Govi\Python\productivity.xlsx', sheet_name='Sheet1')
df = pd.DataFrame({'day':[1,2,3,4,5], 'sleep':[8,2,3,5,6], 'freshup':[1,3,2,4,3], 'upskill':[3,2,4,3,5]}, index =['0','1','2','3','4'])
print(df)
#print("Column headings:")
#print(df.columns)
sleep = 0
freshup = 0
office= 0
lunch= 0
eveng = 0
commute= 0
dinner=0
upskill = 0
lst = []
lst = df.values
"""
for i in lst:
   # sleep  = sleep + df[sleep][i]
    #freshup  = freshup+df[freshup][i]
    #office  =office+ df[office][i]
   # lunch  =lunch+ df[lunch][i]
    #eveng  = eveng+df[eveng][i]
   # commute  = commute+df[commute][i]
   # dinner  = dinner+df[dinner][i]
   # upskill = upskill+ df[upskill][i]
    k = 0
    for j in i:
        
        print(j, end=" ")
        sleep = sleep +j
    k+= 1
print("\n",sleep) """
"""   
print("it is",df.index)
#print(df.columns)
#print(df['sleep'])

for i in df.index:
    print(df['sleep'][i])
    sleep = sleep + df['sleep'][i]
    print(sleep)

"""

sleeps = df['sleep']
days= df['day']
for i in sleeps:
    sleep = sleep +i
freshups = df['freshup']
for i in freshups:
    freshup = freshup +i 
upskills = df['upskill']
for i in upskills:
    upskill = upskill + i         
#print(sleep)
#plt.plot(days, sleeps, 'bo')
p1 =plt.bar(days, sleeps)
p2 =plt.bar(days, freshups)
#plt.bar(days, upskill)
plt.xlabel('Days')
plt.ylabel('Sleeping hrs')
plt.title("My Sleeping tracker")
plt.legend((p1[0],p2[0]), ('sleep', 'freshup'))
print(plt.figure())
"""
plt.savefig('image.png')
with open("image.png", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print(str)

"""


