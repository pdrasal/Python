# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 14:43:18 2019

@author: patricio.a.drasal
"""
import csv
import os
from datetime import datetime

def prred(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prgreen(skk): print("\033[92m {}\033[00m" .format(skk))
def pryellow(skk): print("\033[93m {}\033[00m" .format(skk))

print()
print()
print (('-').center(100, '-'))
print ((('Bulk SQL execution and reporting for Database servers').upper()).center(100))  
print (('-').center(100, '-'))
print()
print('During this process you will be required to provide: \n ')
print('(-) The SQL file name containing the SQL statement\s to execute.')
print('(-) The "servers" file name, with this format: server,database,port,usr,pass')
print('(-) Output Report type: html or csv.')
##print('(-) Output type: one consolidated file for all DBs or one file per DB \n')
print (('-').center(100, '-'))
print()    
Query = input("Enter SQL file name (e.g.: query1.sql): ")
ServerFile  = input("Enter the servers file name (e.g: <servers.txt>): ")
ReportType = int(input("Select the report type: Enter 1 for html or 2 for csv: "))
##Reportcount= int(input("Select output: Enter 1 for one consolidated report for all DBs and 2 for one file per DB: "))
print()
dt_string = datetime.now().strftime("%d%m%Y-%H%M%S")
ReportName='DBReport_'+dt_string
if ReportType == 1 :
    ReportName=ReportName+'.html'
    SqlplusIn="HTML ON"
if ReportType == 2 :
    ReportName=ReportName+'.csv'
    SqlplusIn='CSV ON'

print(' **** Your report will be written to the file: '+ ReportName +' ****')
print()
# Delete the file if exists
f = open(ReportName, "wb")
f.close()

## Read file section

with open(ServerFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(f'\.....executing SQL statements on server {row[0]} database {row[1]}')
        ##if Reportcount == 1 :
        cmd = 'echo exit | sqlplus -S -L -M '+'"'+SqlplusIn+'"'+' '+str(row[3])+'/'+'"'+str(row[4])+'"'+'@'+str(row[0])+':'+str(row[2])+'/'+str(row[1])+' @'+Query+' >> '+ReportName                       
        #if Reportcount == 2 :
        #    cmd = 'echo exit | sqlplus -S -L -M '+'"'+SqlplusIn+'"'+' '+str(row[3])+'/'+'"'+str(row[4])+'"'+'@'+str(row[0])+':'+str(row[2])+'/'+str(row[1])+' @'+Query+' > '+str(row[0])+'_'+str(row[1])+'_'+ReportName   
        returned_value = os.system(cmd)
        prgreen('success') if returned_value==0 else prred('failed')     
print()
pryellow(f'Script execution completed')


# $result_file="$($Nextserver.Server)-$($Nextserver.database).html"

