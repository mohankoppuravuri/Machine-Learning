
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data =  pd.read_csv("D:\Downlaods\kc_house_data.csv")

x = data.sqft_lot
y = data.price
x=x[:100]
y=y[:100]

for i in range(100):
    x=(x-min(x))/(max(x)-min(x))

for i in range(100):
    y=(y-min(y))/(max(y)-min(y))    
    


b=np.cov(x,y,ddof=0)[0,1]/np.var(x)
a=(np.mean(y)-b*np.mean(x))/2
h=0
y_pred=[]
i=0
while (True):
    i+=1
    for i in range(100):
        y_pred.append(a+b*x[i])

    sse=[]
    for i in range(100):
        sse.append(((y[i]-y_pred[i])**2)*0.5)
    t_sse=0

    for i in range(100):
       t_sse+=sse[i]

    da=[]
    db=[]

    for i in range(100):
        da.append(-(y[i]-y_pred[i]))
        db.append(da[i]*x[i])
    
    suma=0
    sumb=0   

    for i in range(100):
        suma+=da[i]
        sumb+=db[i]
        
    a=a-0.01*suma
    b=b-0.01*sumb   
    
    for i in range(100):
        y_pred[i]=a+b*x[i]

    for i in range(100):
        sse[i]=((y[i]-y_pred[i])**2)*0.5
    psse=0

    for i in range(100):
       psse+=sse[i]
    if (psse>t_sse):
       a+=0.01*suma
       b+=0.01*sumb
       print(a)
       print(b)
       print(i)
       break


y_p=[]
for i in range(100):
    y_p.append(a +b*x[i])

sum1=0
for i in range(100):
    sum1 =sum1+ (y[i]-y_p[i])**2
    
plt.scatter(x,y)
plt.plot(x,a+b*x)

print("Heloo please delete this line");
