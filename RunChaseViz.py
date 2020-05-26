# -*- coding: utf-8 -*-
"""
Created on Tue May 26 08:43:48 2020

@author: zgilf
"""

import yaml
import numpy as np
import matplotlib.pyplot as plt




with open('C:/Users/zgilf/Documents/Projects/cricket/1178419.yaml') as file:
    dta = yaml.load(file, Loader=yaml.FullLoader)



#Make a graph showing the run chase and wickets (could use Pandas instead of NP array)
first=dta["innings"][0]["1st innings"]["deliveries"]
runs1=np.zeros((120,4))
ball=1
total=0
for i in range(len(first)):
    for x in first[i]:
        over=np.floor(x)
    runs1[ball-1,0]=ball
    runs1[ball-1,1]+= first[i][x]["runs"]["total"]
    runs1[ball-1,2]= total+first[i][x]["runs"]["total"]
    total+=first[i][x]["runs"]["total"]
    if "wicket" in first[i][x]:
        runs1[ball-1,3]=1
    if "extras" in first[i][x]:
        if "wides" not in first[i][x]["extras"]:
            ball=ball+1
    else:
        ball=ball+1

second=dta["innings"][1]["2nd innings"]["deliveries"]
runs2=np.zeros((120,4))
ball=1
total=0
for i in range(len(second)):
    for x in second[i]:
        over=np.floor(x)
    runs2[ball-1,0]=ball
    runs2[ball-1,1]+= second[i][x]["runs"]["total"]
    runs2[ball-1,2]= total+second[i][x]["runs"]["total"]
    total+=second[i][x]["runs"]["total"]
    if "wicket" in second[i][x]:
        runs2[ball-1,3]=1
    if "extras" in second[i][x]:
        if "wides" not in second[i][x]["extras"]:
            ball=ball+1
    else:
        ball=ball+1
runs2=runs2[runs2[:,0]>0] #where ball>0

plt.plot(runs1[:,0],runs1[:,2], label="First Innings")
plt.scatter(runs1[runs1[:,3]==1,0],runs1[runs1[:,3]==1,2], marker="x")
plt.plot(runs2[:,0],runs2[:,2], label="Run Chase")
plt.scatter(runs2[runs2[:,3]==1,0],runs2[runs2[:,3]==1,2], marker="x")
plt.xlabel("Ball")
plt.ylabel("Runs")
plt.legend(loc="upper left")




#For stats across all matches, could look at:
# 1. avgs by ball for each innings
# 2. avgs by over for each innings
# 3. avgs by ball or over 2nd innings based on score, RRR, wickets








