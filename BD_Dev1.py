# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 14:43:18 2019

@author: patricio.a.drasal
"""
import csv
import subprocess
from datetime import datetime
import pandas as pd
import getpass
from tabulate import tabulate

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
(-) The "servers" file name, with this format: server,database,port,usr,pass

============================================================================
''')
Query = input("Enter SQL file name (e.g.: query1.sql): ")
ServerFile  = input("Enter the servers file name (e.g: <servers.txt>): ")

#print ("Enter credentials")
#username = input("Username: ")
#password = getpass.getpass("Password: ")
username = "Admin"
password = "Xporacle2145"

print()

ReportName='DBReport_'+datetime.now().strftime("%d%m%Y-%H%M%S")+'.csv'
Reporthtml='DBReport_'+datetime.now().strftime("%d%m%Y-%H%M%S")+'.html'

print(' **** Your report will be written to the files: '+ ReportName +' & '+ Reporthtml+' ****\n')

SqlplusIn='CSV ON'

f = open(ReportName, "wb")
f.close()

df = pd.DataFrame(columns=['Server','Database','Result','Message'])

with open(ServerFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(f'\.....executing SQL statements on server {row[0]} database {row[1]}')
        #cmd = 'echo exit | sqlplus -S -L -M '+'"'+SqlplusIn+'"'+' '+str(row[3])+'/'+'"'+str(row[4])+'"'+'@'+str(row[0])+':'+str(row[2])+'/'+str(row[1])+' @'+Query+' >> '+ReportName                       
        cmd = 'echo exit | sqlplus -S -L -M '+'"'+SqlplusIn+'"'+' '+username+'/'+'"'+password+'"'+'@'+str(row[0])+':'+str(row[2])+'/'+str(row[1])+' @'+Query+' >> '+ReportName
        retcode = subprocess.run(cmd,shell=True)
        if retcode.returncode == 0:
            new_row = {'Server':row[0],'Database':'x','Result':'successful','Message':'-'}
            df = df.append(new_row, ignore_index=True)
            prgreen('successful')
        else:
            new_row = {'Server':row[0],'Database':'x','Result':'Failed','Message':'Error'}
            df = df.append(new_row, ignore_index=True)
            prred('failed')
 
pryellow(f'Script execution completed\n')
print("Execution summary is as follows")

pdtabulate=lambda df:tabulate(df,headers='keys',tablefmt='psql')
print(pdtabulate(df))

df.to_html('summary.html') 

df2 = pd.read_csv(ReportName)
html = df2.to_html()

#write html to file
text_file = open(Reporthtml, "w")
text_file.write(html)
text_file.close()    


   
