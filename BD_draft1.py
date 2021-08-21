# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 14:43:18 2019

@author: patricio.a.drasal
"""
import csv
import cx_Oracle as cx

filename="coco.csv"
FILE=open(filename,"a");
output=csv.writer(FILE)

#tnsname entry
#connection = cx_Oracle.connect("Admin", "Xporacle214", "patodb_high", encoding="UTF-8")
#defaul port
#connection = cx_Oracle.connect("hr", userpwd, "dbhost.example.com/orclpdb1", encoding="UTF-8")
#non default port
#connection = cx_Oracle.connect("hr", userpwd, "dbhost.example.com:1984/orclpdb1",encoding="UTF-8")

try:
    connection = cx.connect("Admin", "Xporacle2145", "patodb_high", encoding="UTF-8")
except cx.DatabaseError as e:
    print(cx.Error)
    errorObj, = e.args
    print("Error Code:", errorObj.code)
    print("Error Message:", errorObj.message)
else:
    with connection.cursor() as cursor:
        for row in cursor.execute("select name,dbid from v$database"):
            print(row)
            output.writerow(row)
        
FILE.close()


