#!/usr/bin/python
 
import sys
import csv
 
reader =csv.reader(sys.stdin,delimiter='\t')
next(reader,None) # skip the header,read the 1st line
 
for line in reader:
    
    if len(line) !=19:
        continue
    
    if line[5] =='question':
        print '{0}\t{1}\t{2}'.format(line[0],line[5][0],len(line[4]))
        
    elif line[5] =='answer':
        print '{0}\t{1}\t{2}'.format(line[7],line[5][0],len(line[4]))