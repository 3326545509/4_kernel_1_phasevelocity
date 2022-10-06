#画二维相速度图
#draw 2D phase velocity
import numpy as np
from matplotlib import pyplot as plt
def read(path):
    with open(path,'r')as f:
        row=f.readlines()

    data=[]
    for i in range(2,len(row)):
        temp=row[i]
        temp=np.array(temp.split()).astype(float)
        data.append(temp)
    return data

def draw(data):
    x=[]
    y=[]
    sensitivity=[]
    for i in range(1,len(data)):
        x.append(data[i][0])
        y.append(data[i][1])
        sensitivity.append(data[i][2])
    plt.scatter(x,y,c=sensitivity,cmap='seismic')
    plt.colorbar()
    plt.savefig('out.png')

data=read("f_0.05.phvel.txt")
draw(data)
