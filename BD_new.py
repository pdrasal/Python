# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 14:43:18 2019

@author: patricio.a.drasal
"""
import csv
#import os
import subprocess
from datetime import datetime
#from subprocess import call,Popen, PIPE
import getpass

def prred(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prgreen(skk): print("\033[92m {}\033[00m" .format(skk))
def pryellow(skk): print("\033[93m {}\033[00m" .format(skk))

print(
'''
============================================================================
        Bulk SQL execution and reporting for Database servers
============================================================================

During this process you will be required to provide:
(-) The SQL file name containing the SQL statement\s to execute.
(-) The "servers" file name, with this format: server,database,port
(-) Output Report type: html or csv.

============================================================================
''')
Query = input("Enter SQL file name (e.g.: query1.sql): ")
ServerFile  = input("Enter the servers file name (e.g: <servers.txt>): ")
ReportType = int(input("Select the report type: Enter 1 for html or 2 for csv: "))
print ("Enter credentials")
username = input("Username: ")
password = getpass.getpass("Password: ")

print()
dt_string = datetime.now().strftime("%d%m%Y-%H%M%S")
ReportName='DBReport_'+dt_string
if ReportType == 1 :
    ReportName=ReportName+'.html'
    SqlplusIn="HTML ON"
if ReportType == 2 :
    ReportName=ReportName+'.csv'
    SqlplusIn='CSV ON'

print(' **** Your report will be written to the file: '+ ReportName +' ****\n')

f = open(ReportName, "wb")
f.close()

T = []

with open(ServerFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(f'\.....executing SQL statements on server {row[0]} database {row[1]}')
        #cmd = 'echo exit | sqlplus -S -L -M '+'"'+SqlplusIn+'"'+' '+str(row[3])+'/'+'"'+str(row[4])+'"'+'@'+str(row[0])+':'+str(row[2])+'/'+str(row[1])+' @'+Query+' >> '+ReportName                       
        cmd = 'echo exit | sqlplus -S -L -M '+'"'+SqlplusIn+'"'+' '+username+'/'+'"'+password+'"'+'@'+str(row[0])+':'+str(row[2])+'/'+str(row[1])+' @'+Query+' >> '+ReportName
        retcode = subprocess.run(cmd,shell=True)
        if retcode.returncode == 0:
            T.insert(len(T),[row[0], row[1], 'OK'])
            prgreen('success')
        else:
            T.insert(len(T),[row[0], row[1], 'Failed'])
            prred('failed')
 
pryellow(f'Script execution completed\n')
print("Execution summary is as follows")
print()
for row in T:
    print(row)
    


   
