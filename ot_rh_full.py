#Processes weather data and produces various stats
#Need data_full.txt in same directory as script
#This script will take several hours to run. It's the damn recursive for loops
#Written by jkpearman shortly after learning python. Forgive me...
#Thank you to pmnied for debugging and general help

################################################################################

#Removes day air and rh data

import math
import statistics
import xlrd

outp = list()
outp0 = list()
outp1 = list()
outp2 = list()
outp3 = list()
outp4 = list()
outp5 = list()
outp6 = list()
outp7 = list()
outp8 = list()
outp9 = list()
outp10 = list()
outp11 = list()
outp12 = list()

fout_dark_data = open('data_dark.txt', 'w')

fhand_full_data = open( 'data_full.txt', "r" )

for line in fhand_full_data :        
    dark_data = line.split()
    try:
        dark=int(dark_data[4])
    except:
        continue
    if dark==1:
        outp1.append(line)
fhand_full_data.close()

    

for item in outp1:
#    print>>fout1, item
    fout_dark_data.write(item)
    
    
fout_dark_data.close()

outp.clear()
outp0.clear()
outp1.clear()
outp2.clear()
outp3.clear()
outp4.clear()
outp5.clear()
outp6.clear()
outp7.clear()
outp8.clear()
outp9.clear()
outp10.clear()
outp11.clear()
outp12.clear()


################################################################################



#Records outside temp and rh

#outp1 is ot
#outp2 is rh


fout_ot_year = open('data_ot.txt', 'w')
fout_rh_year = open('data_rh.txt', 'w')

fhand_dark_year = open( 'data_dark.txt', "r" )


for line in fhand_dark_year :        
    data_dark_year = line.split()
    dateEXCEL=float(data_dark_year[0])
    date = xlrd.xldate.xldate_as_tuple(dateEXCEL, 0)
    ot=float(data_dark_year[5])
    if ot<-20 or ot>35:
        continue
    ot_list=[date, ot]
    ot_line=str(ot_list)
    outp1.append(ot_line)
    dp=float(data_dark_year[6])
    if dp>30 or dp<-39:
        continue
    rh=100*(6.116441*(10**((7.591386*dp)/(240.7263+dp)))
        /(6.116441*(10**((7.591386*ot)/(240.7263+ot)))))
    
    if rh>100:
#        print(rh)
        rh=100
    rh_list=[date, rh]
    rh_line=str(rh_list)
    outp2.append(rh_line)

    
fhand_dark_year.close()

    

for item in outp1:
    val = ''.join([c for c in item if c in '1234567890.-,'])
    fout_ot_year.write(val + '\n')
#    print>>fout1, item
for item in outp2:
    val = ''.join([c for c in item if c in '1234567890.-,'])
    fout_rh_year.write(val + '\n')
#    print>>fout2, item
    
    
fout_ot_year.close()
fout_rh_year.close()

outp.clear()
outp0.clear()
outp1.clear()
outp2.clear()
outp3.clear()
outp4.clear()
outp5.clear()
outp6.clear()
outp7.clear()
outp8.clear()
outp9.clear()
outp10.clear()
outp11.clear()
outp12.clear()




################################################################################

#Split ot values into months




fout_ot_1 = open('ot1.txt', 'w')
fout_ot_2 = open('ot2.txt', 'w')
fout_ot_3 = open('ot3.txt', 'w')
fout_ot_4 = open('ot4.txt', 'w')
fout_ot_5 = open('ot5.txt', 'w')
fout_ot_6 = open('ot6.txt', 'w')
fout_ot_7 = open('ot7.txt', 'w')
fout_ot_8 = open('ot8.txt', 'w')
fout_ot_9 = open('ot9.txt', 'w')
fout_ot_10 = open('ot10.txt', 'w')
fout_ot_11 = open('ot11.txt', 'w')
fout_ot_12 = open('ot12.txt', 'w')


fhand_ot_year = open( 'data_ot.txt', "r" )

    
    
for line in fhand_ot_year :        
    ot_full_data = line.split(',')
    try :
        month= int(ot_full_data[1])
#        ot_point_value=str(ot_full_data[6])
#        ot_point=float(ot_point_value[0:-2])
        ot_point=float(ot_full_data[6])
    except :
        continue
    if month==1:
        if ot_point>18:
            continue
        outp1.append(line)
    if month==2:
        if ot_point>18:
            continue
        outp2.append(line)
    if month==3:
        outp3.append(line)
    if month==4:
        outp4.append(line)
    if month==5:
        outp5.append(line)
    if month==6:
        outp6.append(line)
    if month==7:
        outp7.append(line)
    if month==8:
        outp8.append(line)
    if month==9:
        outp9.append(line)
    if month==10:
        if ot_point>21:
            continue
        outp10.append(line)
    if month==11:
        outp11.append(line)
    if month==12:
        outp12.append(line)            
fhand_ot_year.close()

    

for item in outp1:
#    print>>fout1, item
    fout_ot_1.write(item)
for item in outp2:
    fout_ot_2.write(item)
for item in outp3:
    fout_ot_3.write(item)
for item in outp4:
    fout_ot_4.write(item)
for item in outp5:
    fout_ot_5.write(item)
for item in outp6:
    fout_ot_6.write(item)
for item in outp7:
    fout_ot_7.write(item)
for item in outp8:
    fout_ot_8.write(item)
for item in outp9:
    fout_ot_9.write(item)
for item in outp10:
    fout_ot_10.write(item)
for item in outp11:
    fout_ot_11.write(item)
for item in outp12:
    fout_ot_12.write(item)
    
fout_ot_1.close()
fout_ot_2.close()
fout_ot_3.close()
fout_ot_4.close()
fout_ot_5.close()
fout_ot_6.close()
fout_ot_7.close()
fout_ot_8.close()
fout_ot_9.close()
fout_ot_10.close()
fout_ot_11.close()
fout_ot_12.close()

outp.clear()
outp0.clear()
outp1.clear()
outp2.clear()
outp3.clear()
outp4.clear()
outp5.clear()
outp6.clear()
outp7.clear()
outp8.clear()
outp9.clear()
outp10.clear()
outp11.clear()
outp12.clear()

################################################################################


#Split rh values into months



fout_rh_1 = open('rh1.txt', 'w')
fout_rh_2 = open('rh2.txt', 'w')
fout_rh_3 = open('rh3.txt', 'w')
fout_rh_4 = open('rh4.txt', 'w')
fout_rh_5 = open('rh5.txt', 'w')
fout_rh_6 = open('rh6.txt', 'w')
fout_rh_7 = open('rh7.txt', 'w')
fout_rh_8 = open('rh8.txt', 'w')
fout_rh_9 = open('rh9.txt', 'w')
fout_rh_10 = open('rh10.txt', 'w')
fout_rh_11 = open('rh11.txt', 'w')
fout_rh_12 = open('rh12.txt', 'w')


fhand_rh_year = open( 'data_rh.txt', "r" )

    
    
for line in fhand_rh_year :        
    rh_full_data = line.split(',')
    try :
        month= int(rh_full_data[1])
    except :
        continue
    if month==1:
        outp1.append(line)
    if month==2:
        outp2.append(line)
    if month==3:
        outp3.append(line)
    if month==4:
        outp4.append(line)
    if month==5:
        outp5.append(line)
    if month==6:
        outp6.append(line)
    if month==7:
        outp7.append(line)
    if month==8:
        outp8.append(line)
    if month==9:
        outp9.append(line)
    if month==10:
        outp10.append(line)
    if month==11:
        outp11.append(line)
    if month==12:
        outp12.append(line)            
fhand_rh_year.close()

    

for item in outp1:
#    print>>fout1, item
    fout_rh_1.write(item)
for item in outp2:
    fout_rh_2.write(item)
for item in outp3:
    fout_rh_3.write(item)
for item in outp4:
    fout_rh_4.write(item)
for item in outp5:
    fout_rh_5.write(item)
for item in outp6:
    fout_rh_6.write(item)
for item in outp7:
    fout_rh_7.write(item)
for item in outp8:
    fout_rh_8.write(item)
for item in outp9:
    fout_rh_9.write(item)
for item in outp10:
    fout_rh_10.write(item)
for item in outp11:
    fout_rh_11.write(item)
for item in outp12:
    fout_rh_12.write(item)
    
fout_rh_1.close()
fout_rh_2.close()
fout_rh_3.close()
fout_rh_4.close()
fout_rh_5.close()
fout_rh_6.close()
fout_rh_7.close()
fout_rh_8.close()
fout_rh_9.close()
fout_rh_10.close()
fout_rh_11.close()
fout_rh_12.close()

outp.clear()
outp0.clear()
outp1.clear()
outp2.clear()
outp3.clear()
outp4.clear()
outp5.clear()
outp6.clear()
outp7.clear()
outp8.clear()
outp9.clear()
outp10.clear()
outp11.clear()
outp12.clear()


################################################################################


#analyze ot monthly data to get stats


import statistics
import math

def median(l):
    srt = sorted(l)
    mid = len(l)//2
    if len(l) % 2: 
            return srt[mid]
    else:
        med = (srt[mid] + srt[mid-1]) / 2  
        return med


fhand_ot_1 = open('ot1.txt', 'r')
fhand_ot_2 = open('ot2.txt', 'r')
fhand_ot_3 = open('ot3.txt', 'r')
fhand_ot_4 = open('ot4.txt', 'r')
fhand_ot_5 = open('ot5.txt', 'r')
fhand_ot_6 = open('ot6.txt', 'r')
fhand_ot_7 = open('ot7.txt', 'r')
fhand_ot_8 = open('ot8.txt', 'r')
fhand_ot_9 = open('ot9.txt', 'r')
fhand_ot_10 = open('ot10.txt', 'r')
fhand_ot_11 = open('ot11.txt', 'r')
fhand_ot_12 = open('ot12.txt', 'r')


lines1 = fhand_ot_1.readlines()
lines2 = fhand_ot_2.readlines()
lines3 = fhand_ot_3.readlines()
lines4 = fhand_ot_4.readlines()
lines5 = fhand_ot_5.readlines()
lines6 = fhand_ot_6.readlines()
lines7 = fhand_ot_7.readlines()
lines8 = fhand_ot_8.readlines()
lines9 = fhand_ot_9.readlines()
lines10 = fhand_ot_10.readlines()
lines11 = fhand_ot_11.readlines()
lines12 = fhand_ot_12.readlines()


fhand_ot_1.close()
fhand_ot_2.close()
fhand_ot_3.close()
fhand_ot_4.close()
fhand_ot_5.close()
fhand_ot_6.close()
fhand_ot_7.close()
fhand_ot_8.close()
fhand_ot_9.close()
fhand_ot_10.close()
fhand_ot_11.close()
fhand_ot_12.close()




outp_ot_COUNT=list()
outp_ot_AVG=list()
outp_ot_MED=list()
outp_ot_MAX=list()
outp_ot_MIN=list()
outp_ot_STDEV=list()

fhand_stats_ot = open('stats_ot.txt', 'w')

count = 0
total = 0

lines_list_ot=[lines1,lines2,lines3,lines4,lines5,lines6,lines7,lines8,lines9,
    lines10,lines11,lines12]

#iterate through months
for item in lines_list_ot:
    lines=item
    del outp[:]
    count=0
    total=0
    #iterate through lines in month
    for line in lines :
        data = line.split(',')
        value = (str(data[6])) 
        ot=float(value[0:-3])
        outp.append(ot)
        count = count + 1
        total = total + ot

    maximum = max(outp)
    minimum = min(outp)
    med = median(outp)
    avg = total / count
    stdev =statistics.stdev(outp)
    
    outp_ot_COUNT.append(count)
    outp_ot_AVG.append(round(avg,2))
    outp_ot_MED.append(round(med,2))
    outp_ot_MAX.append(round(maximum,2))
    outp_ot_MIN.append(round(minimum,2))
    outp_ot_STDEV.append(round(stdev,2))


lines_stats_ot=list()



outp1=['Month: ,Jan,Feb,Mar,Apr,May,June,July,Aug,Sept,Oct,Nov,Dec']
outp2=['Count: ',outp_ot_COUNT]
outp3=['Max: ',outp_ot_MAX]
outp4=['Min: ',outp_ot_MIN]
outp5=['Median: ',outp_ot_MED]
outp6=['Average: ',outp_ot_AVG]
outp7=['Stdev: ',outp_ot_STDEV]

lines_stats_ot.append(str(outp1))
lines_stats_ot.append(str(outp2))
lines_stats_ot.append(str(outp3))
lines_stats_ot.append(str(outp4))
lines_stats_ot.append(str(outp5))
lines_stats_ot.append(str(outp6))
lines_stats_ot.append(str(outp7))

for item in lines_stats_ot:
    val = ''.join([c for c in item if c in 
        '1234567890.-,\/:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'])
    fhand_stats_ot.write(val)
    fhand_stats_ot.write('\n')
fhand_stats_ot.close()


outp.clear()
outp0.clear()
outp1.clear()
outp2.clear()
outp3.clear()
outp4.clear()
outp5.clear()
outp6.clear()
outp7.clear()
outp8.clear()
outp9.clear()
outp10.clear()
outp11.clear()
outp12.clear()



################################################################################


#analyze rh monthly data to get stats


fhand_rh_1 = open('rh1.txt', 'r')
fhand_rh_2 = open('rh2.txt', 'r')
fhand_rh_3 = open('rh3.txt', 'r')
fhand_rh_4 = open('rh4.txt', 'r')
fhand_rh_5 = open('rh5.txt', 'r')
fhand_rh_6 = open('rh6.txt', 'r')
fhand_rh_7 = open('rh7.txt', 'r')
fhand_rh_8 = open('rh8.txt', 'r')
fhand_rh_9 = open('rh9.txt', 'r')
fhand_rh_10 = open('rh10.txt', 'r')
fhand_rh_11 = open('rh11.txt', 'r')
fhand_rh_12 = open('rh12.txt', 'r')


lines1 = fhand_rh_1.readlines()
lines2 = fhand_rh_2.readlines()
lines3 = fhand_rh_3.readlines()
lines4 = fhand_rh_4.readlines()
lines5 = fhand_rh_5.readlines()
lines6 = fhand_rh_6.readlines()
lines7 = fhand_rh_7.readlines()
lines8 = fhand_rh_8.readlines()
lines9 = fhand_rh_9.readlines()
lines10 = fhand_rh_10.readlines()
lines11 = fhand_rh_11.readlines()
lines12 = fhand_rh_12.readlines()


fhand_rh_1.close()
fhand_rh_2.close()
fhand_rh_3.close()
fhand_rh_4.close()
fhand_rh_5.close()
fhand_rh_6.close()
fhand_rh_7.close()
fhand_rh_8.close()
fhand_rh_9.close()
fhand_rh_10.close()
fhand_rh_11.close()
fhand_rh_12.close()


outp_rh_COUNT=list()
outp_rh_AVG=list()
outp_rh_MED=list()
outp_rh_MAX=list()
outp_rh_MIN=list()
outp_rh_STDEV=list()

fhand_stats_rh = open('stats_rh.txt', 'w')

count = 0
total = 0

lines_list=[lines1,lines2,lines3,lines4,lines5,lines6,lines7,lines8,lines9,
    lines10,lines11,lines12]

#iterate through months
for item in lines_list:
    lines=item
    del outp[:]
    count=0
    total=0
    #iterate through lines in month
    for line in lines :
        data = line.split(',')
        value = (str(data[6])) 
        ot=float(value[0:-3])
        outp.append(ot)
        count = count + 1
        total = total + ot

    maximum = max(outp)
    minimum = min(outp)
    med = median(outp)
    avg = total / count
    stdev =statistics.stdev(outp)
    
    outp_rh_COUNT.append(count)
    outp_rh_AVG.append(round(avg,2))
    outp_rh_MED.append(round(med,2))
    outp_rh_MAX.append(round(maximum,2))
    outp_rh_MIN.append(round(minimum,2))
    outp_rh_STDEV.append(round(stdev,2))

lines_stats_rh=list()

outp1=['Month: ,Jan,Feb,Mar,Apr,May,June,July,Aug,Sept,Oct,Nov,Dec']
outp2=['Count: ',outp_rh_COUNT]
outp3=['Max: ',outp_rh_MAX]
outp4=['Min: ',outp_rh_MIN]
outp5=['Median: ',outp_rh_MED]
outp6=['Average: ',outp_rh_AVG]
outp7=['Stdev: ',outp_rh_STDEV]

lines_stats_rh.append(str(outp1))
lines_stats_rh.append(str(outp2))
lines_stats_rh.append(str(outp3))
lines_stats_rh.append(str(outp4))
lines_stats_rh.append(str(outp5))
lines_stats_rh.append(str(outp6))
lines_stats_rh.append(str(outp7))

for item in lines_stats_rh:
    val = ''.join([c for c in item if c in
        '1234567890.-,\/:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'])
    fhand_stats_rh.write(val)
    fhand_stats_rh.write('\n')
fhand_stats_rh.close()


outp.clear()
outp0.clear()
outp1.clear()
outp2.clear()
outp3.clear()
outp4.clear()
outp5.clear()
outp6.clear()
outp7.clear()
outp8.clear()
outp9.clear()
outp10.clear()
outp11.clear()
outp12.clear()

################################################################################

#data cleaner
#removes extraneous characters from data and prints the data to a text file

#ot

from string import digits
import math



file_list=['rh1.txt','rh2.txt','rh3.txt','rh4.txt','rh5.txt','rh6.txt',
    'rh7.txt','rh8.txt','rh9.txt','rh10.txt','rh11.txt','rh12.txt']

for file in file_list:
    fhand=open(file,'r')
    lines=fhand.readlines()
    for item in lines:
        val = ''.join([c for c in item if c in '1234567890.-,'])
        outp.append(val)
    fhand.close()

fout=open('data_rh_clean.txt','w')        
for item in outp:
    fout.write(item+'\n')
fout.write('end_of_lines')
fout.close()

outp.clear()
outp0.clear()
outp1.clear()
outp2.clear()
outp3.clear()
outp4.clear()
outp5.clear()
outp6.clear()
outp7.clear()
outp8.clear()
outp9.clear()
outp10.clear()
outp11.clear()
outp12.clear()

#ot

file_list=['ot1.txt','ot2.txt','ot3.txt','ot4.txt','ot5.txt','ot6.txt',
    'ot7.txt','ot8.txt','ot9.txt','ot10.txt','ot11.txt','ot12.txt']

for file in file_list:
    fhand=open(file,'r')
    lines=fhand.readlines()
    for item in lines:
        val = ''.join([c for c in item if c in '1234567890.-,'])
        outp.append(val)
    fhand.close()

fout=open('data_ot_clean.txt','w')        
for item in outp:
    fout.write(item+'\n')
fout.write('end_of_lines')
fout.close()

outp.clear()
outp0.clear()
outp1.clear()
outp2.clear()
outp3.clear()
outp4.clear()
outp5.clear()
outp6.clear()
outp7.clear()
outp8.clear()
outp9.clear()
outp10.clear()
outp11.clear()
outp12.clear()




################################################################################

#Reads in ot and rh values for each day and produces stats
#versions follow for every individual day in range (FULL), days averaged from 
#every year (DAYS), and months averaged from every year (MONTHS)

#FULL



#for each day in list, search file for lines from that date
#when 'end_of_lines' is reached in the text file, produce stats for that day
#move to next day and repeat
#when you are out of dates, print the stats to a text file

from string import digits
import statistics
import math
import datetime

fout_stats_ot_full=open('daily_stats_ot_full.txt','w')

outp_data_ot_full=list()
outp_stats_ot_full=list()
outp_day_stats_ot_full=list()
year=0
month=0
day=0
ot=0.0
month_list=[1,2,3,4,5,6,7,8,9,10,11,12]
day_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,
    27,28,29,30,31]
year_list=[2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]

#iterate through days one at a time
for anum in year_list:
    print(anum)
    for moon in month_list:
        print(moon)
        for date in day_list:
            print(date)
            fhand_ot_full=open('data_ot_clean.txt','r')
#read through text file line by line
            for item in fhand_ot_full:
#if line is 'end_of_lines' compute stats for the day
                if item=='end_of_lines':
#but if there are too few datapoints for the day, just skip it
                    if len(outp_data_ot_full)<3:
                        break
#compute stats for day, print them, and save them to list
                    maximum=max(outp_data_ot_full)
                    minimum=min(outp_data_ot_full)
                    med=statistics.median(outp_data_ot_full)
                    avg=statistics.mean(outp_data_ot_full)
                    stdev=statistics.stdev(outp_data_ot_full)
                    count=len(outp_data_ot_full)
                    outp_day_stats_ot_full=[anum,moon,date,count,maximum,
                        minimum,med,avg,stdev]
                    outp_stats_ot_full.append(str(outp_day_stats_ot_full))
                    print(outp_day_stats_ot_full)
                    outp_data_ot_full.clear()
                    outp_day_stats_ot_full.clear()
                else:
#if line was NOT 'end_of_lines', identify if date on line matches, 
#and save in list if it is
                    line=item.split(',')
                    year=int(line[0])
                    month=int(line[1])
                    day=int(line[2])
                    if year==anum:
                        if month==moon:
                            if day==date:
                                ot=float(line[6])
                                outp_data_ot_full.append(ot)
            fhand_ot_full.close()

#print stats to text file, removing unnecessary characters
for stat_line_ot_full in outp_stats_ot_full:
    val_ot_full=''.join([c for c in stat_line_ot_full if c in '1234567890.-,'])
    fout_stats_ot_full.write(val_ot_full+'\n')                    
fout_stats_ot_full.close()            


################################################################################



#Reads in values for each day and produces stats 

#for each day in list, search file for lines from that date
#when 'end_of_lines' is reached in the text file, produce stats for that day
#move to next day and repeat
#when you are out of dates, print the stats to a text file

from string import digits
import statistics
import math
import datetime

fout_stats_rh_full=open('daily_stats_rh_full.txt','w')

outp_data_rh_full=list()
outp_stats_rh_full=list()
outp_day_stats_rh_full=list()
year=0
month=0
day=0

month_list=[1,2,3,4,5,6,7,8,9,10,11,12]
day_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,
    27,28,29,30,31]
year_list=[2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]

#iterate through days one at a time
for anum in year_list:
    print(anum)
    for moon in month_list:
        print(moon)
        for date in day_list:
            print(date)
            fhand_rh_full=open('data_rh_clean.txt','r')
#read through text file line by line
            for item in fhand_rh_full:
#if line is 'end_of_lines' compute stats for the day
                if item=='end_of_lines':
#but if there are too few datapoints for the day, just skip it
                    if len(outp_data_rh_full)<3:
                        break
#compute stats for day, print them, and save them to list
                    maximum=max(outp_data_rh_full)
                    minimum=min(outp_data_rh_full)
                    med=statistics.median(outp_data_rh_full)
                    avg=statistics.mean(outp_data_rh_full)
                    stdev=statistics.stdev(outp_data_rh_full)
                    count=len(outp_data_rh_full)
                    outp_day_stats_rh_full=[anum,moon,date,count,maximum,
                        minimum,med,avg,stdev]
                    outp_stats_rh_full.append(str(outp_day_stats_rh_full))
                    print(outp_day_stats_rh_full)
                    outp_data_rh_full.clear()
                    outp_day_stats_rh_full.clear()
                else:
#if line was NOT 'end_of_lines', identify if date on line matches,
#and save in list if it is
                    line=item.split(',')
                    year=int(line[0])
                    month=int(line[1])
                    day=int(line[2])
                    if year==anum:
                        if month==moon:
                            if day==date:
                                rh=float(line[6])
                                outp_data_rh_full.append(rh)
            fhand_rh_full.close()

#print stats to text file, removing unnecessary characters
for stat_line_rh_full in outp_stats_rh_full:
    val_rh_full=''.join([c for c in stat_line_rh_full if c in '1234567890.-,'])
    fout_stats_rh_full.write(val_rh_full+'\n')                   
fout_stats_rh_full.close()    





################################################################################

#MONTHS

#Reads in values for each day and produces stats 

#for each day in list, search file for lines from that date
#when 'end_of_lines is reached in the text file, produce stats for that day
#move to next day and repeat
#when you are out of dates, print the stats to a text file

from string import digits
import statistics
import math
import datetime

fout_stats_ot_month=open('daily_stats_ot_month.txt','w')

outp_data_ot_month=list()
outp_stats_ot_month=list()
outp_day_stats_ot_month=list()
year=0
month=0
day=0
ot=0.0


month_list=[1,2,3,4,5,6,7,8,9,10,11,12]
day_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,
    27,28,29,30,31]
year_list=[2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]

length=0

#iterate through months one at a time
for moon in month_list:
    print(moon)
    fhand_ot_month=open('data_ot_clean.txt','r')
#read through text file line by line
    for item in fhand_ot_month:
#if line is 'end_of_lines' compute stats for the month
        if item=='end_of_lines':
#but if there are too few datapoints for the day, just skip it
            if len(outp_data_ot_month)<3:
                break
#compute stats for month, print them, and save them to list
            maximum=max(outp_data_ot_month)
            minimum=min(outp_data_ot_month)
            med=statistics.median(outp_data_ot_month)
            avg=statistics.mean(outp_data_ot_month)
            stdev=statistics.stdev(outp_data_ot_month)
            count=len(outp_data_ot_month)
            outp_day_stats_ot_month=[moon,count,maximum,minimum,med,avg,stdev]
            outp_stats_ot_month.append(str(outp_day_stats_ot_month))
            print(outp_day_stats_ot_month)
            outp_data_ot_month.clear()
            outp_day_stats_ot_month.clear()
        else:
#if line was NOT 'end_of_lines', identify if date on line matches,
#and save in list if it is
            line=item.split(',')
            year=int(line[0])
            month=int(line[1])
            day=int(line[2])
            if month==moon:
                ot=float(line[6])
                outp_data_ot_month.append(ot)
    fhand_ot_month.close()
#print stats to text file, removing unnecessary characters
for stat_line_ot_mon in outp_stats_ot_month:
    val_ot_month=''.join([c for c in stat_line_ot_mon if c in '1234567890.-,'])
    fout_stats_ot_month.write(val_ot_month+'\n')        
fout_stats_ot_month.close()            



################################################################################


fout_stats_rh_month=open('daily_stats_rh_month.txt','w')

outp_data_rh_month=list()
outp_stats_rh_month=list()
outp_day_stats_rh_month=list()
year=0
month=0
day=0

#iterate through months one at a time
for moon in month_list:
    print(moon)
    fhand_rh_month=open('data_rh_clean.txt','r')
#read through text file line by line
    for item in fhand_rh_month:
#if line is 'end_of_lines' compute stats for the month
        if item=='end_of_lines':
#but if there are too few datapoints for the day, just skip it
            if len(outp_data_rh_month)<3:
                break
#compute stats for month, print them, and save them to list
            maximum=max(outp_data_rh_month)
            minimum=min(outp_data_rh_month)
            med=statistics.median(outp_data_rh_month)
            avg=statistics.mean(outp_data_rh_month)
            stdev=statistics.stdev(outp_data_rh_month)
            count=len(outp_data_rh_month)
            outp_day_stats_rh_month=[moon,count,maximum,minimum,med,avg,stdev]
            outp_stats_rh_month.append(str(outp_day_stats_rh_month))
            print(outp_day_stats_rh_month)
            outp_data_rh_month.clear()
            outp_day_stats_rh_month.clear()
        else:
#if line was NOT 'end_of_lines', identify if date on line matches,
#and save in list if it is
            line=item.split(',')
            year=int(line[0])
            month=int(line[1])
            day=int(line[2])
            if month==moon:
                rh=float(line[6])
                outp_data_rh_month.append(rh)
    fhand_rh_month.close()
#print stats to text file, removing unnecessary characters
for stat_line_rh_mon in outp_stats_rh_month:
    val_rh_month=''.join([c for c in stat_line_rh_mon if c in '1234567890.-,'])
    fout_stats_rh_month.write(val_rh_month+'\n')        
fout_stats_rh_month.close()    


################################################################################


#DAYS

#Reads in values for each day and produces stats 

#for each day in list, search file for lines from that date
#when 'end_of_lines' is reached in the text file, produce stats for that day
#move to next day and repeat
#when you are out of dates, print the stats to a text file

from string import digits
import statistics
import math
import datetime

fout_stats_ot_day=open('daily_stats_ot_day.txt','w')

outp_data_ot_day=list()
outp_stats_ot_day=list()
outp_day_stats_ot_day=list()
year=0
month=0
day=0
ot=0.0


month_list=[1,2,3,4,5,6,7,8,9,10,11,12]
day_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,
    27,28,29,30,31]
year_list=[2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]

length=0

#iterate through days one at a time
for moon in month_list:
    print(moon)
    for date in day_list:
        print(date)
        fhand_ot_day=open('data_ot_clean.txt','r')
#read through text file line by line
        for item in fhand_ot_day:
#if line is 'end_of_lines' compute stats for the day
            if item=='end_of_lines':
#but if there are too few datapoints for the day, just skip it
                if len(outp_data_ot_day)<3:
                    break
#compute stats for day, print them, and save them to list
                maximum=max(outp_data_ot_day)
                minimum=min(outp_data_ot_day)
                med=statistics.median(outp_data_ot_day)
                avg=statistics.mean(outp_data_ot_day)
                stdev=statistics.stdev(outp_data_ot_day)
                count=len(outp_data_ot_day)
                outp_day_stats_ot_day=[moon,date,count,maximum,minimum,med,avg,
                    stdev]
                outp_stats_ot_day.append(str(outp_day_stats_ot_day))
                print(outp_day_stats_ot_day)
                outp_data_ot_day.clear()
                outp_day_stats_ot_day.clear()
            else:
#if line was NOT 'end_of_lines', identify if date on line matches,
#and save in list if it is

                line=item.split(',')
                year=int(line[0])
                month=int(line[1])
                day=int(line[2])
                if month==moon:
                    if day==date:
                        ot=float(line[6])
                        outp_data_ot_day.append(ot)
        fhand_ot_day.close()
#print stats to text file, removing unnecessary characters
for stat_line_ot_day in outp_stats_ot_day:
    val_ot_day = ''.join([c for c in stat_line_ot_day if c in '1234567890.-,'])
    fout_stats_ot_day.write(val_ot_day+'\n')
fout_stats_ot_day.close()

################################################################################


fout_stats_rh_day=open('daily_stats_rh_day.txt','w')

outp_data_rh_day=list()
outp_stats_rh_day=list()
outp_day_stats_rh_day=list()
year=0
month=0
day=0


#iterate through days one at a time
for moon in month_list:
    print(moon)
    for date in day_list:
        print(date)
        fhand_rh_day=open('data_rh_clean.txt','r')
#read through text file line by line
        for item in fhand_rh_day:
#if line is 'end_of_lines' compute stats for the day
            if item=='end_of_lines':
#but if there are too few datapoints for the day, just skip it
                if len(outp_data_rh_day)<3:
                    break
#compute stats for day, print them, and save them to list
                maximum=max(outp_data_rh_day)
                minimum=min(outp_data_rh_day)
                med=statistics.median(outp_data_rh_day)
                avg=statistics.mean(outp_data_rh_day)
                stdev=statistics.stdev(outp_data_rh_day)
                count=len(outp_data_rh_day)
                outp_day_stats_rh_day=[moon,date,count,maximum,minimum,med,avg,
                    stdev]
                outp_stats_rh_day.append(str(outp_day_stats_rh_day))
                print(outp_day_stats_rh_day)
                outp_data_rh_day.clear()
                outp_day_stats_rh_day.clear()
            else:
#if line was NOT 'end_of_lines', identify if date on line matches,
#and save in list if it is

                line=item.split(',')
                year=int(line[0])
                month=int(line[1])
                day=int(line[2])
                if month==moon:
                    if day==date:
                        rh=float(line[6])
                        outp_data_rh_day.append(rh)
        fhand_rh_day.close() 
for stat_line_rh_day in outp_stats_rh_day:
    val_rh_day = ''.join([c for c in stat_line_rh_day if c in '1234567890.-,'])
    fout_stats_rh_day.write(val_rh_day+'\n')
fout_stats_rh_day.close()

###############################################################################
#ALL

#Reads in values for each day and produces stats 

#for each day in list, search file for lines from that date
#when 'end_of_lines' is reached in the text file, produce stats for that day
#move to next day and repeat
#when you are out of dates, print the stats to a text file

from string import digits
import statistics
import math
import datetime

fout_stats_ot_all=open('daily_stats_ot_all.txt','w')

outp_data_ot_all=list()
outp_stats_ot_all=list()
outp_all_stats_ot_all=list()
year=0
month=0
day=0
ot=0.0


month_list=[1,2,3,4,5,6,7,8,9,10,11,12]
day_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,
    27,28,29,30,31]
year_list=[2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]

length=0


# for moon in month_list:
    # print(moon)
    # for date in all_list:
        # print(date)
fhand_ot_all=open('data_ot_clean.txt','r')
#read through text file line by line
for item in fhand_ot_all:
#if line is 'end_of_lines' compute stats for the all
    if item=='end_of_lines':
#but if there are too few datapoints for the all, just skip it
        if len(outp_data_ot_all)<3:
            break
#compute stats for all, print them, and save them to list
        maximum=max(outp_data_ot_all)
        minimum=min(outp_data_ot_all)
        med=statistics.median(outp_data_ot_all)
        avg=statistics.mean(outp_data_ot_all)
        stdev=statistics.stdev(outp_data_ot_all)
        count=len(outp_data_ot_all)
        outp_all_stats_ot_all=[moon,date,count,maximum,minimum,med,avg,
            stdev]
        outp_stats_ot_all.append(str(outp_all_stats_ot_all))
        print(outp_all_stats_ot_all)
        outp_data_ot_all.clear()
        outp_all_stats_ot_all.clear()
    else:
#if line was NOT 'end_of_lines', identify if date on line matches,
#and save in list if it is

        line=item.split(',')
        ot=float(line[6])
        outp_data_ot_all.append(ot)
fhand_ot_all.close()
#print stats to text file, removing unnecessary characters
for stat_line_ot_all in outp_stats_ot_all:
    val_ot_all = ''.join([c for c in stat_line_ot_all if c in '1234567890.-,'])
    fout_stats_ot_all.write(val_ot_all+'\n')
fout_stats_ot_all.close()

################################################################################


fout_stats_rh_all=open('daily_stats_rh_all.txt','w')

outp_data_rh_all=list()
outp_stats_rh_all=list()
outp_all_stats_rh_all=list()
year=0
month=0
day=0


#iterate through alls one at a time
for moon in month_list:
    print(moon)
    for date in all_list:
        print(date)
        fhand_rh_all=open('data_rh_clean.txt','r')
#read through text file line by line
        for item in fhand_rh_all:
#if line is 'end_of_lines' compute stats for the all
            if item=='end_of_lines':
#but if there are too few datapoints for the all, just skip it
                if len(outp_data_rh_all)<3:
                    break
#compute stats for all, print them, and save them to list
                maximum=max(outp_data_rh_all)
                minimum=min(outp_data_rh_all)
                med=statistics.median(outp_data_rh_all)
                avg=statistics.mean(outp_data_rh_all)
                stdev=statistics.stdev(outp_data_rh_all)
                count=len(outp_data_rh_all)
                outp_all_stats_rh_all=[moon,date,count,maximum,minimum,med,avg,
                    stdev]
                outp_stats_rh_all.append(str(outp_all_stats_rh_all))
                print(outp_all_stats_rh_all)
                outp_data_rh_all.clear()
                outp_all_stats_rh_all.clear()
            else:
#if line was NOT 'end_of_lines', identify if date on line matches,
#and save in list if it is

                rh=float(line[6])
                outp_data_rh_all.append(rh)
        fhand_rh_all.close() 
for stat_line_rh_all in outp_stats_rh_all:
    val_rh_all = ''.join([c for c in stat_line_rh_all if c in '1234567890.-,'])
    fout_stats_rh_all.write(val_rh_all+'\n')
fout_stats_rh_all.close()


################################################################################
# Stats for all days combined

from string import digits
import statistics
import math
import datetime

fout_stats_ot_all=open('daily_stats_ot_all.txt','w')

outp_data_ot_all=list()
outp_stats_ot_all=list()
outp_all_stats_ot_all=list()
year=0
month=0
day=0
ot=0.0


month_list=[1,2,3,4,5,6,7,8,9,10,11,12]
day_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,
    27,28,29,30,31]
year_list=[2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]

length=0


# for moon in month_list:
    # print(moon)
    # for date in all_list:
        # print(date)
fhand_ot_all=open('data_ot_clean.txt','r')
#read through text file line by line
for item in fhand_ot_all:
#if line is 'end_of_lines' compute stats for the all
    if item=='end_of_lines':
#but if there are too few datapoints for the all, just skip it
        if len(outp_data_ot_all)<3:
            break
#compute stats for all, print them, and save them to list
        maximum=max(outp_data_ot_all)
        minimum=min(outp_data_ot_all)
        med=statistics.median(outp_data_ot_all)
        avg=statistics.mean(outp_data_ot_all)
        stdev=statistics.stdev(outp_data_ot_all)
        count=len(outp_data_ot_all)
        outp_all_stats_ot_all=[count,maximum,minimum,med,avg,
            stdev]
        outp_stats_ot_all.append(str(outp_all_stats_ot_all))
        print(outp_all_stats_ot_all)
        outp_data_ot_all.clear()
        outp_all_stats_ot_all.clear()
    else:
#if line was NOT 'end_of_lines', identify if date on line matches,
#and save in list if it is

        line=item.split(',')
        year=int(line[0])
        month=int(line[1])
        day=int(line[2])
        rh=float(line[6])
        outp_data_ot_all.append(rh)
fhand_ot_all.close()
#print stats to text file, removing unnecessary characters
for stat_line_ot_all in outp_stats_ot_all:
    val_ot_all = ''.join([c for c in stat_line_ot_all if c in '1234567890.-,'])
    fout_stats_ot_all.write(val_ot_all+'\n')
fout_stats_ot_all.close()

################################################################################
# Stats for all days combined

fout_stats_rh_all=open('daily_stats_rh_all.txt','w')

outp_data_rh_all=list()
outp_stats_rh_all=list()
outp_all_stats_rh_all=list()
year=0
month=0
day=0


#iterate through alls one at a time

fhand_rh_all=open('data_rh_clean.txt','r')
#read through text file line by line
for item in fhand_rh_all:
#if line is 'end_of_lines' compute stats for the all
    if item=='end_of_lines':
#but if there are too few datapoints for the all, just skip it
        if len(outp_data_rh_all)<3:
            break
#compute stats for all, print them, and save them to list
        maximum=max(outp_data_rh_all)
        minimum=min(outp_data_rh_all)
        med=statistics.median(outp_data_rh_all)
        avg=statistics.mean(outp_data_rh_all)
        stdev=statistics.stdev(outp_data_rh_all)
        count=len(outp_data_rh_all)
        outp_all_stats_rh_all=[count,maximum,minimum,med,avg,
            stdev]
        outp_stats_rh_all.append(str(outp_all_stats_rh_all))
        print(outp_all_stats_rh_all)
        outp_data_rh_all.clear()
        outp_all_stats_rh_all.clear()
    else:
#if line was NOT 'end_of_lines', identify if date on line matches,
#and save in list if it is

        line=item.split(',')
        year=int(line[0])
        month=int(line[1])
        day=int(line[2])
        rh=float(line[6])
        outp_data_rh_all.append(rh)
fhand_rh_all.close() 
for stat_line_rh_all in outp_stats_rh_all:
    val_rh_all = ''.join([c for c in stat_line_rh_all if c in '1234567890.-,'])
    fout_stats_rh_all.write(val_rh_all+'\n')
fout_stats_rh_all.close()