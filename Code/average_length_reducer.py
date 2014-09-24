#!/usr/bin/python
 
import sys
 
oldKey =None
total =0
count =0
post =0
 
def length_result(key,post,total,count):
    if count ==0:
        print "%s\t%s\t%0.2f" %(key,post,0)
        
    else:
        print "%s\t%s\t%0.2f" %(key,post,float(total)/count)
        
#1.read the sorted data from mapper        
for line in sys.stdin:
    data_mapped =line.strip().split('\t')
    
    #2.verify the dataset
    if len(data_mapped) !=3 :
        continue
      
    thisKey,thisType,thisLength =data_mapped
    
    #3.check if the key changed from previous one
    if oldKey and oldKey != thisKey:
        length_result(oldKey,post,total,count)
        
        #4.clear previous(old) line
        total =0
        count =0
        post =0
        
    if thisType =='q':
        post =thisLength
        
    elif thisType =='a':
        total += int(thisLength)
        count +=1
    
    #5.update the key in next line  
    oldKey =thisKey

#6.check oldkey is not None
if oldKey != None:
    length_result(oldKey,post,total,count)