#
# TODO: Unsure if we need to define custom search commands.
#
#
import sys,splunk.Intersplunk
results = []
  
try:
     results,dummyresults,settings = splunk.Intersplunk.getOrganizedResults()
  
############### YOUR CODE HERE ##############
     import csv
 
     ifile  = open('/opt/splunk/var/run/splunk/check.csv', "rb")
     reader = csv.reader(ifile)
 
     
  
############### DATA MANIPULATION HERE ##############
   
except:
     import traceback
     stack =  traceback.format_exc()
     results = splunk.Intersplunk.generateErrorResults("Error : Traceback: " + str(stack))
  
splunk.Intersplunk.outputResults( results )

