#Reads in seeing data from multiple files
#saves the seeing data points in text files for each hour in each month
#Need seeing log files in same directory as script
#Takes about 10 minutes to run

#Takes input from twi_18_dusk.txt, twi_18_dawn.txt,
#and a text log file (seeing_log_*_*_*.log) for every day (2011-2016) (~2100)

#Outputs to seeing_full.txt for temporary storage,
#and to a text file seeing_*_*.txt for every hour for each month (~130)

#Written by jkpearman
#Thank you to pmnied for debugging and general help

################################################################################

#imports
from string import digits
from datetime import datetime
from pytz import timezone
import numpy as np
import statistics
import math
import glob
import pytz

#output file
fout = open('seeing_full.txt', 'w')

#lists
outp_data_seeing_full=list()
outp_stats_seeing_full=list()
outp_day_stats_seeing_full=list()
outp = list()
seeing_stats=list()
month_list=[1,2,3,4,5,6,7,8,9,10,11,12]
hour_list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

#variables
filename='string'
fname='string'
date='string'
time='string'

#timezones
utc=pytz.utc
pacific=timezone('US/Pacific')

################################################################################

#create dictionary from table of 18 degree twilight times, dusk and dawn
lines = np.genfromtxt("twi_18_dusk.txt", delimiter=",", dtype=str)
dusk_18 = dict()
for i in range(len(lines)):
    dusk_18[lines[i][0]] = lines[i][1]

lines = np.genfromtxt("twi_18_dawn.txt", delimiter=",", dtype=str)
dawn_18 = dict()
for i in range(len(lines)):
    dawn_18[lines[i][0]] = lines[i][1]

#make a list of all the files to look through, with * being a wildcard
list_of_files = glob.glob('seeing_log_*-*-*')   

#iterate through all of the files in the list of files
for filename in list_of_files :

    try :    
        fhand = open( filename, "r" )
    except :
        fname=str(filename)
        print( 'file '+fname+' does not exist or cannot be opened')
        continue
    
#iterate through each line in the current text file
    for line in fhand :
        try:
            data = line.split()
        except:
            print("Can't split")
            continue

        seeing_point = float(data[4])
        meas_num = int(data[5])

#exclude data point if the seeing is too low or high, 
#or if the monitor did not get all 9 data points it attempted to get
        if seeing_point < 0.5 or seeing_point > 5 :
            continue
        if meas_num<9:
            continue

#save the year, month, day, hour, minute, and second from the given line
        month_point=int(str(data[1]).split('/')[0])
        day_point=int(str(data[1]).split('/')[1])
        year_point=int(str(data[1]).split('/')[2])

        hour_point=int(str(data[0]).split(':')[0])
        minute_point=int(str(data[0]).split(':')[1])
        second_point=int(str(data[0]).split(':')[2])

#convert time to UT using pytz
        loc_dt=pacific.localize(datetime(year_point,month_point,day_point,
            hour_point,minute_point,second_point))

        utc_dt=loc_dt.astimezone(utc)
        date=str(utc_dt).split()[0]
        time=str(utc_dt).split()[1].split('+')[0]


#Use dictionaries to look up twilight times for given date
#make a time object for both dusk and dawn 18 degree twilight
        dusk_twi=datetime(int(date.split('-')[0]),int(date.split('-')[1]),
            int(date.split('-')[2]),int(dusk_18[date].split(':')[0]),
            int(dusk_18[date].split(':')[1]),int(dusk_18[date].split(':')[2]),
            tzinfo=pytz.utc)
        
        dawn_twi=datetime(int(date.split('-')[0]),int(date.split('-')[1]),
            int(date.split('-')[2]),int(dawn_18[date].split(':')[0]),
            int(dawn_18[date].split(':')[1]),int(dawn_18[date].split(':')[2]),
            tzinfo=pytz.utc)


#compare time to twilight time and exlude value if outside of dark time
        if utc_dt<dusk_twi:
            continue
        if utc_dt>dawn_twi:
            continue

        # utc_dt_str=str(utc_dt)
        # utc_data=utc_dt_str.split()
        # utc_time_long=str(utc_data[1])
        # utc_time_data=utc_time_long.split(':')
        # utc_hour=utc_time_data[0]
        # dt=str(loc_dt.astimezone(utc)).split()

        utc_hour=str(str(loc_dt.astimezone(utc)).split()[1]).split(':')[0]        
        outp=(month_point,day_point,utc_hour,minute_point,seeing_point)
        seeing_stats.append(outp)
        
    fhand.close()


#write values from list of seeing values to file and end it with 'end_of_lines'
#remove unnecessary characters
for item in seeing_stats:
    val = ''.join([c for c in str(item) if c in
        '1234567890.-,\/:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'])
    fout.write(val)
    fout.write('\n')
fout.write('end_of_lines')
fout.close()

################################################################################

#iterate through each month and each hour and save the seeing values in separate
#text files for each hour of each month
for moon in month_list:
    print(moon)
    for hr in hour_list:
        print(hr)
        fhand_seeing=open('seeing_full.txt','r')
#read through text file line by line
        for item in fhand_seeing:
#if line is 'end_of_lines' write seeing data to text file
            if item=="end_of_lines":
#if there are too few datapoints for the day and hour, just skip it
                if len(outp_data_seeing_full)<100:
                    break
#write seeing values to a text file named for the month and hour for that data
                # moon_str=str(moon)
                # hr_str=str(hr)
                # filename=str('seeing_'+moon_str+'_'+hr_str)
                # fout_data_seeing_full=open(filename+'.txt','w')
                fout_data_seeing_full=open(str('seeing_'+str(moon)
                    +'_'+str(hr))+'.txt','w')
                for stat_line_seeing_full in outp_data_seeing_full:
                    fout_data_seeing_full.write(str(stat_line_seeing_full)+'\n')                    
                fout_data_seeing_full.close()
                outp_data_seeing_full.clear()
            else:
#if line was NOT 'end_of_lines', identify if date on line matches
                line=item.split(',')
                month=int(line[0])
                hour=int(line[2])
#and save in list if it is
                if month==moon:
                    if hour==hr:
                        seeing=float(line[4])
                        outp_data_seeing_full.append(seeing)
        fhand_seeing.close()
