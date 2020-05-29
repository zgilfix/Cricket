# -*- coding: utf-8 -*-
"""
Created on Thu May 28 09:00:42 2020

@author: zgilf
"""

import yaml
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

#Create a dataset with one' row for each ball in 2nd innings (can roll up to over later if want to)
#Columns: ID, Ball, Runs, Wicket, Score, Target, RRR, Date, Hitting Team, Bowling Team 

df = pd.DataFrame(columns=['ID','Ball','Runs','Wicket','Score','Target','RRR','Date','Hitting','Bowling'])





for files in os.listdir('C:/Users/zgilf/Documents/Projects/cricket/data/'):
    with open(os.path.join('C:/Users/zgilf/Documents/Projects/cricket/data/', files)) as file:
        dta = yaml.load(file, Loader=yaml.FullLoader)
    
        if files=="419155.yaml" or "result" in dta["info"]["outcome"]:
            continue
     
    #Find Target    
    first=dta["innings"][0]["1st innings"]["deliveries"]
    target=0
    for i in range(len(first)):
        for x in first[i]:
            over=np.floor(x)
        target+= first[i][x]["runs"]["total"]
    
    #Go through each ball in second innings
    second=dta["innings"][1]["2nd innings"]["deliveries"]
    ball=1
    runs=0
    score=0
    wicket=0
    for i in range(len(second)):
        for x in second[i]:
            over=np.floor(x)
        RRR=((target-score)/(121-ball))*6    
        runs+= second[i][x]["runs"]["total"]
        score+= second[i][x]["runs"]["total"]
        if "wicket" in second[i][x]:
            wicket=1
        if "extras" in second[i][x]:
            if "wides" not in second[i][x]["extras"] and "noballs" not in second[i][x]["extras"]:
                df=df.append({'ID':files,'Ball':ball,'Runs':runs,'Wicket':wicket,
                          'Score':score,'Target':target,'RRR':RRR,'Date':dta['info']['dates'],
                          'Hitting':dta["innings"][1]["2nd innings"]["team"],
                          'Bowling':dta["innings"][0]["1st innings"]["team"]},ignore_index=True)
                ball=ball+1
                runs=0
                wicket=0
        else:
            df=df.append({'ID':files,'Ball':ball,'Runs':runs,'Wicket':wicket,
                      'Score':score,'Target':target,'RRR':RRR,'Date':dta['info']['dates'],
                      'Hitting':dta["innings"][1]["2nd innings"]["team"],
                      'Bowling':dta["innings"][0]["1st innings"]["team"]},ignore_index=True)
            ball=ball+1
            runs=0
            wicket=0
        


#Save data
df.to_csv("C:/Users/zgilf/Documents/Projects/cricket/data/innings2.csv", index=False)

