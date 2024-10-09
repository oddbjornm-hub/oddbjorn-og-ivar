# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 19:10:25 2024

@author: ivarn
"""

from pylab import *
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

n=0
tid=[]
temperatur=[]
luftrykk_havnivaa=[]
with open('temperatur_trykk_met_samme_rune_time_datasett.csv.txt', 'r') as fil:
    for linje in fil:
        #print(linje)
        if n>=1:
            # Splitter linjen på mellomrom for å få hver kolonne som et element i en liste
            kolonner = linje.split(';')
            t=kolonner[2].strip()
            tid.append(t)
            temperatur.append(kolonner[3].replace(',','.'))
            luftrykk_havnivaa.append(kolonner[4].replace(',','.'))
        n+=1

temperatur=temperatur[:-1]
luftrykk_havnivaa=luftrykk_havnivaa[:-1]
tid=tid[:-1]

temperatur_S = [float(temp) for temp in temperatur]
luftrykk_havnivaa_S = [float(lufttrykk) for lufttrykk in luftrykk_havnivaa]
tid_S=[datetime.strptime(t,'%d.%m.%Y %H:%M') for t in tid]
#print(temperatur)
#print(luftrykk_havnivaa_S)
#print(tid_S)



n=0
tid_UIS=[]
tid_sidenstart=[]
temperatur_UIS=[]
trykk_UIS=[]
absolutt_trykk_UIS=[]
tid_UIS2=[]
tid_UIS_min=[]
sek=0
with open('trykk_og_temperaturlogg_rune_time.csv.txt', 'r') as fil:
    for linje in fil:
        #print(linje)
        if n>=1:
            # Splitter linjen på mellomrom for å få hver kolonne som et element i en liste
            kolonner = linje.split(';')
            try:
                t=kolonner[0].strip()
                t2=datetime.strptime(t,'%m.%d.%Y %H:%M')
                temperatur_UIS.append(kolonner[4].replace(',','.'))
                trykk_UIS.append(kolonner[2].replace(',','.'))
                absolutt_trykk_UIS.append(kolonner[3].replace(',','.'))
                #tid_UIS2.append(t2)
                
                if sek==0:
                    tid_UIS2.append(t2)
                    #tid_UIS_min.append(t2)
                    sek=10
                elif sek==10:
                    t2=t2+timedelta(seconds=sek)
                    tid_UIS2.append(t2)
                    sek=20
                elif sek==20:
                    t2=t2+timedelta(seconds=sek)
                    tid_UIS2.append(t2)
                    sek=30
                elif sek==30:
                    t2=t2+timedelta(seconds=sek)
                    tid_UIS2.append(t2)
                    sek=40
                elif sek==40:
                    t2=t2+timedelta(seconds=sek)
                    tid_UIS2.append(t2)
                    sek=50
                elif sek==50:
                    t2=t2+timedelta(seconds=sek)
                    tid_UIS2.append(t2)
                    sek=60
                else:
                    tid_UIS2.append(t2)
                    sek=0
                    #tid_UIS_min.append(t2)
                
            except ValueError:
                i=0
            tid_UIS.append(t)
            #tid_sidenstart.append(kolonner[1])
            
            
        n+=1

print(tid_UIS_min)  
#print(tid_UIS2)

temperatur_UIS = [float(temp) for temp in temperatur_UIS]
#print(temperatur_UIS)
absolutt_trykk_UIS=[float(abtrykk) for abtrykk in absolutt_trykk_UIS]
absolutt_trykk_UIS_hpa=[]
k=30
temp_glatt=[]
for i in range (k, len(temperatur_UIS) - k):
    temp_glatt.append(mean(temperatur_UIS[(i - k):(i + k)]))

for i in absolutt_trykk_UIS:
    absolutt_trykk_UIS_hpa.append(i*10)

#print(absolutt_trykk_UIS)
#hvert min måles trykk på UIS
trykk_UIS_hpa=[]
for t, p in zip(tid_UIS2, trykk_UIS):
    if p != '':  # Hvis trykkverdien ikke er tom
        trykk_UIS_hpa.append(float(p)*10)  # Konverter til float
        tid_UIS_min.append(t)
#trykk_UIS_b = [verdi for verdi in trykk_UIS if verdi]
    
#trykk_UIS_b=[float(trykk) for trykk in trykk_UIS_b]
"""

for i in trykk_UIS_b:
    trykk_UIS_hpa.append(i*10)
"""
#print(trykk_UIS_b)
#tid uis stopper tidligere enn verdier jeg har fra uis på grunn av endring av måten å skrive tiden på


plt.plot(tid_S,temperatur_S)
plt.plot(tid_UIS2,temperatur_UIS)
plt.plot(tid_UIS2[k:len(temperatur_UIS) - k],temp_glatt)
plt.show()


plt.plot(tid_S,luftrykk_havnivaa_S)
plt.plot(tid_UIS2,absolutt_trykk_UIS_hpa)
plt.plot(tid_UIS_min,trykk_UIS_hpa)
plt.show()















