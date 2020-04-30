# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 08:55:29 2020

@author: Ashish
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#for_delay_and_loss
file = open("DelayAndLoss1.txt",'r')
dataset = file.read()
dataset= dataset.split("\n")
dataset=dataset[:-1]
length=int((len(dataset))/3);
index=[i for i in range(length)]
df= pd.DataFrame(dataset)
df_2=pd.DataFrame(index=index,columns=["delay","loss","throughput"])
df_2["delay"] = df.iloc[df.index%3==0,][0].to_list()
df_2["loss"] = df.iloc[df.index%3==1,][0].to_list()
df_2["throughput"] = df.iloc[df.index%3==2,][0].to_list()

file = open("DelayAndLoss2.txt",'r')
dataset = file.read()
dataset= dataset.split("\n")
dataset=dataset[:-1]
length=int((len(dataset))/3);
index=[i for i in range(length)]
df= pd.DataFrame(dataset)
df_2["throughput1"] = (df.iloc[df.index%3==2,][0].to_list())
df_2["throughput"] = pd.to_numeric(df_2["throughput"])+pd.to_numeric(df_2["throughput1"])

file = open("DelayAndLoss3.txt",'r')
dataset = file.read()
dataset= dataset.split("\n")
dataset=dataset[:-1]
length=int((len(dataset))/3);
index=[i for i in range(length)]
df= pd.DataFrame(dataset)
df_2["throughput1"] = df.iloc[df.index%3==2,][0].to_list()
df_2["throughput"] = pd.to_numeric(df_2["throughput"])+pd.to_numeric(df_2["throughput1"])

file = open("DelayAndLoss4.txt",'r')
dataset = file.read()
dataset= dataset.split("\n")
dataset=dataset[:-1]
length=int((len(dataset))/3);
index=[i for i in range(length)]
df= pd.DataFrame(dataset)
df_2["throughput1"] = df.iloc[df.index%3==2,][0].to_list()
df_2["throughput"] = pd.to_numeric(df_2["throughput"])+pd.to_numeric(df_2["throughput1"])


file = open("DelayAndLoss5.txt",'r')
dataset = file.read()
dataset= dataset.split("\n")
dataset=dataset[:-1]
length=int((len(dataset))/3);
index=[i for i in range(length)]
df= pd.DataFrame(dataset)
df_2["throughput1"] = df.iloc[df.index%3==2,][0].to_list()
df_2["throughput"] = pd.to_numeric(df_2["throughput"])+pd.to_numeric(df_2["throughput1"])

df_2["throughput"]= df_2["throughput"].div(5)
lis=list(df_2["delay"].unique())

for i in range(len(lis)):
    temp = df_2.loc[df_2['delay'] == lis[i]]
    plt.plot([float(i) for i in temp['loss'].to_list()],[float(i) for i in temp['throughput'].to_list()])
    plt.legend(lis[:i+1], loc='upper left')
    plt.savefig(f'./plots/DelayAndLoss/delay_{lis[i]}.png')
plt.show()

#for_delay_and_corrupt

file = open("DelayAndCorrupt1.txt",'r')
dataset = file.read()
dataset= dataset.split("\n")
dataset=dataset[:-1]
length=int((len(dataset))/3);
index=[i for i in range(length)]
df= pd.DataFrame(dataset)
df_2=pd.DataFrame(index=index,columns=["delay","corrupt","throughput"])
df_2["delay"] = df.iloc[df.index%3==0,][0].to_list()
df_2["corrupt"] = df.iloc[df.index%3==1,][0].to_list()
df_2["throughput"] = df.iloc[df.index%3==2,][0].to_list()

file = open("DelayAndCorrupt2.txt",'r')
dataset = file.read()
dataset= dataset.split("\n")
dataset=dataset[:-1]
length=int((len(dataset))/3);
index=[i for i in range(length)]
df= pd.DataFrame(dataset)
df_2["throughput1"] = df.iloc[df.index%3==2,][0].to_list()
df_2["throughput"] = pd.to_numeric(df_2["throughput"])+pd.to_numeric(df_2["throughput1"])

file = open("DelayAndCorrupt3.txt",'r')
dataset = file.read()
dataset= dataset.split("\n")
dataset=dataset[:-1]
length=int((len(dataset))/3);
index=[i for i in range(length)]
df= pd.DataFrame(dataset)
df_2["throughput1"] = df.iloc[df.index%3==2,][0].to_list()
df_2["throughput"] = pd.to_numeric(df_2["throughput"])+pd.to_numeric(df_2["throughput1"])

file = open("DelayAndCorrupt4.txt",'r')
dataset = file.read()
dataset= dataset.split("\n")
dataset=dataset[:-1]
length=int((len(dataset))/3);
index=[i for i in range(length)]
df= pd.DataFrame(dataset)
df_2["throughput1"] = df.iloc[df.index%3==2,][0].to_list()
df_2["throughput"] = pd.to_numeric(df_2["throughput"])+pd.to_numeric(df_2["throughput1"])

file = open("DelayAndCorrupt5.txt",'r')
dataset = file.read()
dataset= dataset.split("\n")
dataset=dataset[:-1]
length=int((len(dataset))/3);
index=[i for i in range(length)]
df= pd.DataFrame(dataset)
df_2["throughput1"] = df.iloc[df.index%3==2,][0].to_list()
df_2["throughput"] = pd.to_numeric(df_2["throughput"])+pd.to_numeric(df_2["throughput1"])

df_2["throughput"]= df_2["throughput"].div(5)
lis=list(df_2["delay"].unique())

for i in range(len(lis)):
    temp = df_2.loc[df_2['delay'] == lis[i]]
    plt.plot([float(i) for i in temp['corrupt'].to_list()],[i for i in temp['throughput'].to_list()])
    plt.legend(lis[:i+1], loc='upper left')
    plt.savefig(f'./plots/DelayAndCorrupt/delay_{lis[i]}.png')
plt.show()

####for_delay
file = open("Delay1.txt",'r')
dataset = file.read()
dataset= dataset.split("\n")
dataset= dataset[:-1]
length=int((len(dataset))/2);
index=[i for i in range(length)]
df= pd.DataFrame(dataset)
df_2=pd.DataFrame(index=index,columns=["delay","throughput"])
df_2["delay"] = df.iloc[df.index%2==0,][0].to_list()
df_2["throughput"] = df.iloc[df.index%2==1,][0].to_list()

file = open("Delay2.txt",'r')
dataset = file.read()
dataset= dataset.split("\n")
dataset= dataset[:-1]
length=int((len(dataset))/2);
index=[i for i in range(length)]
df= pd.DataFrame(dataset)
df_2["throughput1"] = df.iloc[df.index%2==1,][0].to_list()
df_2["throughput"] = pd.to_numeric(df_2["throughput"])+pd.to_numeric(df_2["throughput1"])

file = open("Delay3.txt",'r')
dataset = file.read()
dataset= dataset.split("\n")
dataset= dataset[:-1]
length=int((len(dataset))/2);
index=[i for i in range(length)]
df= pd.DataFrame(dataset)
df_2["throughput1"] = df.iloc[df.index%2==1,][0].to_list()
df_2["throughput"] = pd.to_numeric(df_2["throughput"])+pd.to_numeric(df_2["throughput1"])

file = open("Delay4.txt",'r')
dataset = file.read()
dataset= dataset.split("\n")
dataset= dataset[:-1]
length=int((len(dataset))/2);
index=[i for i in range(length)]
df= pd.DataFrame(dataset)
df_2["throughput1"] = df.iloc[df.index%2==1,][0].to_list()
df_2["throughput"] = pd.to_numeric(df_2["throughput"])+pd.to_numeric(df_2["throughput1"])

file = open("Delay5.txt",'r')
dataset = file.read()
dataset= dataset.split("\n")
dataset= dataset[:-1]
length=int((len(dataset))/2);
index=[i for i in range(length)]
df= pd.DataFrame(dataset)
df_2["throughput1"] = df.iloc[df.index%2==1,][0].to_list()
df_2["throughput"] = pd.to_numeric(df_2["throughput"])+pd.to_numeric(df_2["throughput1"])


df_2["throughput"]= df_2["throughput"].div(5)
plt.plot([float(i) for i in df_2['delay'].to_list()],[i for i in df_2['throughput'].to_list()])
plt.savefig(f'./plots/Delay/delay.png')
plt.show()

####for_reorder
file = open("Reorder1.txt",'r')
dataset = file.read()
dataset= dataset.split("\n")
dataset=dataset[:-1]
length=int((len(dataset))/2);
index=[i for i in range(length)]
df= pd.DataFrame(dataset)
df_2=pd.DataFrame(index=index,columns=["reorder","throughput"])
df_2["reorder"] = df.iloc[df.index%2==0,][0].to_list()
df_2["throughput"] = df.iloc[df.index%2==1,][0].to_list()

file = open("Reorder2.txt",'r')
dataset = file.read()
dataset= dataset.split("\n")
dataset=dataset[:-1]
length=int((len(dataset))/2);
index=[i for i in range(length)]
df= pd.DataFrame(dataset)
df_2["throughput1"] = df.iloc[df.index%2==1,][0].to_list()
df_2["throughput"] = pd.to_numeric(df_2["throughput"])+pd.to_numeric(df_2["throughput1"])

file = open("Reorder3.txt",'r')
dataset = file.read()
dataset= dataset.split("\n")
dataset=dataset[:-1]
length=int((len(dataset))/2);
index=[i for i in range(length)]
df= pd.DataFrame(dataset)
df_2["throughput1"] = df.iloc[df.index%2==1,][0].to_list()
df_2["throughput"] = pd.to_numeric(df_2["throughput"])+pd.to_numeric(df_2["throughput1"])

file = open("Reorder4.txt",'r')
dataset = file.read()
dataset= dataset.split("\n")
dataset=dataset[:-1]
length=int((len(dataset))/2);
index=[i for i in range(length)]
df= pd.DataFrame(dataset)
df_2["throughput1"] = df.iloc[df.index%2==1,][0].to_list()
df_2["throughput"] = pd.to_numeric(df_2["throughput"])+pd.to_numeric(df_2["throughput1"])

file = open("Reorder5.txt",'r')
dataset = file.read()
dataset= dataset.split("\n")
dataset=dataset[:-1]
length=int((len(dataset))/2);
index=[i for i in range(length)]
df= pd.DataFrame(dataset)
df_2["throughput1"] = df.iloc[df.index%2==1,][0].to_list()
df_2["throughput"] = pd.to_numeric(df_2["throughput"])+pd.to_numeric(df_2["throughput1"])

df_2["throughput"]= df_2["throughput"].div(5)

plt.plot([float(i) for i in df_2['reorder'].to_list()],[i for i in df_2['throughput'].to_list()])
plt.savefig(f'./plots/Reorder/reorder.png')
plt.show()

    
