# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 08:55:29 2020

@author: Ashish
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#for_delay_and_loss
file = open("DelayAndLoss.txt",'r')
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

lis=list(df_2["delay"].unique())

for i in range(len(lis)):
    temp = df_2.loc[df_2['delay'] == lis[i]]
    plt.plot([float(i) for i in temp['loss'].to_list()],[float(i) for i in temp['throughput'].to_list()])
    plt.legend(lis[:i+1], loc='upper left')
    plt.savefig(f'./plots/DelayAndLoss/delay_{lis[i]}.png')
plt.show()

#for_delay_and_corrupt

file = open("DelayAndCorrupt.txt",'r')
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

lis=list(df_2["delay"].unique())

for i in range(len(lis)):
    temp = df_2.loc[df_2['delay'] == lis[i]]
    plt.plot([float(i) for i in temp['corrupt'].to_list()],[float(i.split()[2]) for i in temp['throughput'].to_list()])
    plt.legend(lis[:i+1], loc='upper left')
    plt.savefig(f'./plots/DelayAndCorrupt/delay_{lis[i]}.png')
plt.show()

####for_delay
file = open("Delay.txt",'r')
dataset = file.read()
dataset= dataset.split("\n")
dataset= dataset[:-2]
length=int((len(dataset))/2);
index=[i for i in range(length)]
df= pd.DataFrame(dataset)
df_2=pd.DataFrame(index=index,columns=["delay","throughput"])
df_2["delay"] = df.iloc[df.index%2==0,][0].to_list()
df_2["throughput"] = df.iloc[df.index%2==1,][0].to_list()

plt.plot([float(i) for i in df_2['delay'].to_list()],[float(i.split()[2]) for i in df_2['throughput'].to_list()])
plt.savefig(f'./plots/Delay/delay.png')
plt.show()

####for_reorder
file = open("Reorder.txt",'r')
dataset = file.read()
dataset= dataset.split("\n")
dataset=dataset[:-1]
length=int((len(dataset))/2);
index=[i for i in range(length)]
df= pd.DataFrame(dataset)
df_2=pd.DataFrame(index=index,columns=["reorder","throughput"])
df_2["reorder"] = df.iloc[df.index%2==0,][0].to_list()
df_2["throughput"] = df.iloc[df.index%2==1,][0].to_list()

plt.plot([float(i) for i in df_2['reorder'].to_list()],[float(i.split()[2]) for i in df_2['throughput'].to_list()])
plt.savefig(f'./plots/Reorder/reorder.png')
plt.show()

    
