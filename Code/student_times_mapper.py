#!/usr/bin/python
   
import sys
import csv
 
reader =csv.reader(sys.stdin,delimiter='\t')
next(reader,None) # skip the header of the column,and read the 1st line

# read each line in reader
for line in reader:
       
    if len(line) !=19 :
        continue # skip this line
        
    hour = line[8][11:13] # select hour 
    print '%s\t%s' %(line[3],int(hour))