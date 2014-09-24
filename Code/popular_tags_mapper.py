#!/usr/bin/python
 
import sys
import csv
 
reader =csv.reader(sys.stdin,delimiter='\t')
next(reader,None) # skip the header,read the 1st line
 
for line in reader:
    
    
    if len(line) !=19:
        continue
        
    tagname =line[2].strip().split()
    
    if line[5] =='question':
        for i in range(0,len(tagname)):
            print '{0}\t{1}'.format(tagname[i].lower(),line[5][0])
        
    