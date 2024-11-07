import random
import math
def yy(n):
    y=[random.uniform(0,10) for i in range(n)]
    yp=[random.uniform(0,10) for i in range(n)]
    return y, yp
def mae(n,y,yp):
    sum=0
    for i in range(1,n,1):
        sum+=abs(y[i]-yp[i])
    return sum/n
def mse(n,y,yp):
    sum=0
    for i in range(1,n,1):
        sum+=(y[i]-yp[i])**2
    return sum/n
def rmse(n,y,yp):
    sum=0
    for i in range(1,n,1):
        sum+=(y[i]-yp[i])**2
    return math.sqrt(sum/n)
def Huber_Loss(n,y,yp):
    sum=0
    if(abs(y-yp)<=0.5):
        for i in range(n):
            sum+=0.5*((y[i]-yp[i])**2)
    else:
        for i in range(n):
            sum+=0.5*(abs(y[i]-yp[i])-0.5*0.5)
    return sum/n

n = int(input("Nhap num_samples: "))
if(n<=0):
    print("number of samples must be a postive integer number")
else:
    str = input("Nhap ham( MAE| MSE| RMSE| Huber_Loss): ")
    y, yp = yy(n)
    res = 0
    if(str=="MSE"):
        res = mse(n,y,yp)
    elif(str=="MAE"):
        res = mae(n,y,yp)
    elif(str=="RMSE"):
        res = rmse(n,y,yp)
    elif(str=="Huber_Loss"):
        res = rmse(n,y,yp)
    else:
        print('loss name loss is not supported')
    if(str=="MSE" or str=="MAE" or str=="RMSE" or str=="Huber_Loss"):
        print(f'Target: {y}')
        print(f'Predict: {yp}')
        print(f'{str}: {res}')
