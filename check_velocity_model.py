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
    depth=[]
    vs=[]
    vp=[]
    for i in range(1,len(data)):
        depth.append(data[i][0])
        vs.append(data[i][1])
        vp.append(data[i][2])
    ax1=plt.figure().add_subplot(111)
    ax1.plot(vp,depth)
    ax1.plot(vs,depth)
    ax1.invert_yaxis()
    plt.savefig('check_velocity_model.png')

data=read("1_lola_97_22")
draw(data)
