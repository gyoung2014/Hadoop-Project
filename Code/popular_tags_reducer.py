#!/usr/bin/python

import sys

oldKey =None
count =0
top_question=[]

def get_top_count(question_count):
    # question_count is a tuple,including [(tagname,count)]
    for i in question_count:
        print '{0}\t{1}'.format(i[0],i[1])
        
        
def top10(question_count,tagname,count):
    question_count.append((tagname,count))
    topten_count =sorted(question_count,key=lambda i:i[1],reverse=True)[0:10] # select top 10 count
    return topten_count
    

#1.read the sorted data from mapper
for line in sys.stdin:
    data_mapped =line.strip().split('\t')
    
    #2.verify the dataset
    if len(data_mapped) !=2:
        continue
        
    thisKey,thisType =data_mapped
    
    #3.check if the key changed from previous one
    if oldKey and oldKey !=thisKey:
    
        #4.calculate the count in tagname under the same student,
        #  get maximum counts in tagname under the same student
       
        top_question = top10(top_question, oldKey, count)
        

        #5.clear previous(old) line
        count =0
        
    #6.update the count in next line
    
    count +=1
    #7.update the key(tagname) in next student data
    oldKey =thisKey
    
#8. check oldkey is not None
if oldKey !=None:
    top_question = top10(top_question, oldKey, count)

#9. After get sorted data,then select Top 10 tagname
get_top_count(top_question)