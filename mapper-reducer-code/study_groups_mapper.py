#!/usr/bin/python
 
import sys
import csv
 
reader =csv.reader(sys.stdin,delimiter='\t')
 
for line in reader:
    
    if len(line) !=19:
        continue
    
    if line[5] =='question':
        # For question:print id and author_id
        print '{0}\t{1}'.format(line[0],line[3])
        
    else:
        # For Answer and comments:print parent_id and author_id
        print '{0}\t{1}'.format(line[6],line[3])