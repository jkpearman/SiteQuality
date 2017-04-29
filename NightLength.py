#NightLength.py

#Reads time lost table, outputs total night lengths by month
#Takes about 10 minutes to run

#Takes time lost data from TimeLost.txt
#Takes twilight times from twi_12_dusk.txt and twi_12_dawn.txt

#Outputs the night length for every night into a text file for each month


#Written by jkpearman
#Thank you to pmnied for debugging and general help

################################################################################

#imports - some of these might not be necessary
from string import digits
from datetime import datetime, timedelta
from pytz import timezone
import numpy as np
import statistics
import math
import pytz


night_length=list()

year_list=[2014,2015,2016]
month_list=[1,2,3,4,5,6,7,8,9,10,11,12]
month_list2=[1,2,3,4,5,6,7,8,9,10,11,12]
hour_list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
day_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,
    27,28,29,30,31]
    
#variables
filename='string'
fname='string'
date='string'


#timezones
utc=pytz.utc

################################################################################

#create dictionary from table of 12 degree twilight times, dusk and dawn
lines = np.genfromtxt("twi_12_dusk.txt", delimiter=",", dtype=str)
dusk_12 = dict()
for i in range(len(lines)):
    dusk_12[lines[i][0]] = lines[i][1]

lines = np.genfromtxt("twi_12_dawn.txt", delimiter=",", dtype=str)
dawn_12 = dict()
for i in range(len(lines)):
    dawn_12[lines[i][0]] = lines[i][1]

#Iterate through each month. This is the month you're currently looking for
for month in month_list:
#clear the list of night lengths from the previous month
    night_length.clear()
#Figure out what you want the text file for that month called, and then make it
    filename=str(str(month)+".txt")
    fout=open(filename,"w")
    
    for year in year_list:
        for moon in month_list2:

        
#for each day check if date is valid, make a date, and get twilight times
            for day in day_list:
            
                day_found=0
                fhand=open('TimeLost.txt',"r")
#check that date is valid
                try:
                    utc_dt=utc.localize(datetime(year,month,day,12,0,0))
                except:
                    continue
#make date string
                date=str(utc_dt).split()[0]

#get twilight times for dusk
                try:
                    dusk_twi=datetime(year,moon,day,
                        int(dusk_12[date].split(':')[0]),
                        int(dusk_12[date].split(':')[1]),
                        int(dusk_12[date].split(':')[2]),tzinfo=pytz.utc)
                except:
                    continue
#get twilight times for dawn
                try:
                    dawn_twi=datetime(year,moon,day,
                        int(dawn_12[date].split(':')[0]),
                        int(dawn_12[date].split(':')[1]),
                        int(dawn_12[date].split(':')[2]),tzinfo=pytz.utc)
                except:
                    continue
#get total night length from twilight times (in HH:MM:SS) and make it a decimal
                total_nl=str(dawn_twi-dusk_twi)
                total_nl_dec=round(float(int(total_nl.split(":")[0])+
                    float(int(total_nl.split(":")[1])/60)),1)
                    
#iterate through each line in the time lost text file
                for line in fhand :
#check if any line in the file matches the date you're looking for, this order 
#of operations is the fastest
                    day_point=int(str(line.split()[0]).split('/')[1])
                    if day!=day_point:
                        continue
                    month_point=int(str(line.split()[0]).split('/')[0])
                    if month!=month_point:
                        continue
                    year_point=int(str(line.split()[0]).split('/')[2])
                    if year!=year_point:
                        continue
#if it does, remember the date was found in time lost file
                    day_found=1
#store the date that was found
                    date_tl=str(str(year_point)+"-"+str(month_point)+"-"+
                        str(day_point))
#turn the time lost (in minutes) into decimal hours
                    time_lost_dec=float((float(line.split()[1]))/(float(60)))
#subtract time lost from total night length to get actual night length
                    actual_nl=round(float(total_nl_dec-time_lost_dec),1)
#if actual night length turns negative, just make it zero
                    if actual_nl<0:
                        actual_nl=0.0
#check that the date is in the month you're looking for, and append it if so
                    if moon==month:
                        night_length.append(actual_nl)
#immediately end the loop because the night has been found
                    break
                fhand.close()
#if the date you're looking for didn't have time lost
#AND if it is in the month you're looking for
#append the total night length calculated from the twilight times
                if moon==month:
                    if day_found==0:
                        night_length.append(total_nl_dec)

#write the list of night lengths to a text file for each month
    for item in night_length:
        val = ''.join([c for c in str(item) if c in '1234567890.'])
        fout.write(val)
        fout.write('\n')
    fout.close()