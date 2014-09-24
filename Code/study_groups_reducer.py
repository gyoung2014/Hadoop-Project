#!/usr/bin/python

import sys

oldKey =None
get_students=[] # all lists save in tuple

def print_students(key,get_students):
    print '{0}\t{1}'.format(key,get_students)
        

#1.read the sorted data from mapper
for line in sys.stdin:
    data_mapped =line.strip().split('\t')
    
    #2.verify the dataset
    if len(data_mapped) !=2:
        continue
        
    thisKey,thisStudent =data_mapped
    
    #3.check if the key changed from previous one
    if oldKey and oldKey !=thisKey:
    
        #4.get student id list under the same student,and
        #  store the oldKey information
        print_students(oldKey,get_students)
            

        #5.clear previous(old) line
        get_students=[]
        
    #6.update the student id list in next line
    
    get_students.append(thisStudent)
    #7.update the key(forum id) in next line
    oldKey =thisKey
    
#8. check oldkey is not None,and print the last line
if oldKey !=None:
    print_students(oldKey,get_students)
