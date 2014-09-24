import sys

oldKey =None
post_hour ={} # tuple pairs in dict,like {(key1:value1),(key2:value2), ...}

def get_max_hour(key,maxhour):
   mhour =0
   mx_value =[]
   
   for k,value in maxhour.items(): # return (k,value) tuple pairs in maxhour dict
       if mhour < value:
           mhour =value
           mx_value =[]
           mx_value.append(k) # add maximum value into list
       elif mhour ==value:
           mx_value.append(k) # add maximum value into list
   
   for i in range(0,len(mx_value)):
       print key,'\t',mx_value[i]

#1.read thpost_houre sorted data from mapper
for line in sys.stdin:
    data_mapped =line.strip().split('\t')
    
    #2.verify the dataset
    if len(data_mapped) !=2:
        continue
        
    thisKey,hour =data_mapped
    
    #3.check if the key changed from previous one
    if oldKey and oldKey !=thisKey:
    
        #4.calculate the count in hour under the same student,
        #  get maximum counts in posted hour under the same student
       

        #5.print out maximum hour from step 4.
        # for example,
        #  if student_id, hour in mapper is:
        #    100000,6
        #    100000,7
  
        #  In reducer,it can print either
        #  "100000,6" or "100000,7"

        #   The loop in the end
        get_max_hour(oldKey,post_hour)

        #6.clear previous(old) student data
        post_hour ={}
        
    #7.update the count in next student data
    if hour in post_hour:
        post_hour[hour] +=1
    else:
        post_hour[hour] =1
    #8.update the student_id in next student data
    oldKey =thisKey
    
#9. check oldkey is not None
if oldKey !=None:
    get_max_hour(oldKey,post_hour)