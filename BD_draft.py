# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 14:43:18 2019

@author: patricio.a.drasal
"""
from datetime import datetime
import csv
import cx_Oracle as cx
import pandas as pd
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
(-) The "servers" file name, with this format: server,database,port,usr,pass
(-) Output Report type: html or csv.

============================================================================
''')
    
#string.center(width[, fillchar])

Query = input("Enter SQL file name (e.g.: query1.sql): ")
ServerFile  = input("Enter the servers file name (e.g: <servers.txt>): ")
ReportType = int(input("Select the report type: Enter 1 for html or 2 for csv: "))

#print ("Enter credentials")
#username = input("Username: ")
#password = getpass.getpass("Password: ")
username = "Admin"
password = "Xporacle2145"

if ReportType == 1 :
    ReportName='DBReport_'+datetime.now().strftime("%d%m%Y-%H%M%S")+'.html'
if ReportType == 2 :
    ReportName='DBReport_'+datetime.now().strftime("%d%m%Y-%H%M%S")+'.csv'

print(' **** Your report will be written to the file: '+ ReportName +' ****\n')

with open(Query, 'r') as file:
    data = file.read()

df = pd.DataFrame(columns=['Server','Database','Result','Message'])
   
FILE=open(ReportName,"a")
output=csv.writer(FILE)

with open(ServerFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(f'\.....executing SQL statements on server {row[0]} database {row[0]}')
        try:
            connection = cx.connect(username, password, row[0], encoding="UTF-8")
        except cx.DatabaseError as e:
            errorObj, = e.args
            prred("Failed")
            new_row = {'Server':row[0],'Database':'x','Result':'Failed','Message':errorObj.message}
            df = df.append(new_row, ignore_index=True)
        else:
            with connection.cursor() as cursor:
                for row in cursor.execute(data):
                    output.writerow(row)
                    prgreen('successful')
                    new_row = {'Server':row[0],'Database':'x','Result':'successful','Message':'-'}
                    df = df.append(new_row, ignore_index=True)
FILE.close()
pryellow('***** Script execution completed *****\n')

pryellow("Execution summary:")
print(df.to_string())