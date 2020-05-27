# -*- coding: utf-8 -*-
"""
Created on Tue May 26 08:43:48 2020

@author: zgilf
"""

import yaml
import numpy as np
import matplotlib.pyplot as plt
import os



#Loop through all games and find avg by ball, over, ball in over
#Also find wicket % by same cats

runs1=np.zeros((120,4))
runs2=np.zeros((120,4))
for i in range(120):
    runs1[i,0]=i
    runs2[i,0]=i


for files in os.listdir('C:/Users/zgilf/Documents/Projects/cricket/data/'):
    with open(os.path.join('C:/Users/zgilf/Documents/Projects/cricket/data/', files)) as file:
        dta = yaml.load(file, Loader=yaml.FullLoader)
    
        if files=="419155.yaml" or "result" in dta["info"]["outcome"]:
            continue
     
    first=dta["innings"][0]["1st innings"]["deliveries"]
    ball=1
    for i in range(len(first)):
        for x in first[i]:
            over=np.floor(x)
        runs1[ball-1,1]+= first[i][x]["runs"]["total"]
        if "extras" in first[i][x]:
            if "wides" not in first[i][x]["extras"] and "noballs" not in first[i][x]["extras"]:
                runs1[ball-1,2]+=1
                ball=ball+1
        else:
            runs1[ball-1,2]+=1
            ball=ball+1
    ball=1
    
    second=dta["innings"][1]["2nd innings"]["deliveries"]
    ball=1
    for i in range(len(second)):
        for x in second[i]:
            over=np.floor(x)
        runs2[ball-1,1]+= second[i][x]["runs"]["total"]
        if "extras" in second[i][x]:
            if "wides" not in second[i][x]["extras"] and "noballs" not in second[i][x]["extras"]:
                runs2[ball-1,2]+=1
                ball=ball+1
        else:
            runs2[ball-1,2]+=1
            ball=ball+1
    ball=1




#avg by ball
runs1[:,3]=runs1[:,1]/runs1[:,2]
runs2[:,3]=runs2[:,1]/runs2[:,2]
plt.plot(runs1[:,0],runs1[:,3], label="Average Runs: First Innings")
plt.plot(runs2[:,0],runs2[:,3], label="Average Runs: Chase")
plt.axvline(x=36.5, color="red", label="End of Powerplay")
plt.xlabel("Ball")
plt.ylabel("Average Runs")
plt.legend(loc="lower right")
plt.ylim((0,2.2))


#avg by over
over1=np.zeros((20,4))
over2=np.zeros((20,4))
for i in range(20):
    over1[i,0]=i+1
    over2[i,0]=i+1
for i in range(120):
    over1[i//6,1]+=runs1[i,1]
    over1[i//6,2]+=runs1[i,2]
    over2[i//6,1]+=runs2[i,1]
    over2[i//6,2]+=runs2[i,2]
over1[:,3]=6*over1[:,1]/over1[:,2]
over2[:,3]=6*over2[:,1]/over2[:,2]
plt.scatter(over1[:,0],over1[:,3], label="Average Runs: First Innings")
plt.scatter(over2[:,0],over2[:,3], label="Average Runs: Chase")
plt.axvline(x=6.5, color="red", label="End of Powerplay")
plt.xlabel("Ball")
plt.ylabel("Average Runs")
plt.legend(loc="lower right")
plt.ylim((0,12))

#avg by ball in over 
ball1=np.zeros((6,4))
ball2=np.zeros((6,4))
for i in range(6):
    ball1[i,0]=i+1
    ball2[i,0]=i+1
for i in range(120):
    ball1[i%6,1]+=runs1[i,1]
    ball1[i%6,2]+=runs1[i,2]
    ball2[i%6,1]+=runs2[i,1]
    ball2[i%6,2]+=runs2[i,2]
ball1[:,3]=ball1[:,1]/ball1[:,2]
ball2[:,3]=ball2[:,1]/ball2[:,2]
plt.scatter(ball1[:,0],ball1[:,3], label="Average Runs: First Innings")
plt.scatter(ball2[:,0],ball2[:,3], label="Average Runs: Chase")
plt.xlabel("Ball")
plt.ylabel("Average Runs")
plt.legend(loc="lower right")
plt.ylim((0,2))


