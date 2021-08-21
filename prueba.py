# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 14:43:18 2019

@author: patricio.a.drasal
"""


import subprocess as sp
import getpass

print ("Enter credentials")
username = input("Username: ")
password = getpass.getpass("Password: ")

print("Username: [%s], password [%s]" % (username, password))

#write to file
#cmd = 'echo exit | sqlplus -S -L -M '+'"HTML ON" '+username+'/'+'"'+password+'"'+'@patodb_high @query.sql >> coco.html'
cmd = 'echo exit | sqlplus -S -L -M '+'"CSV ON" '+username+'/'+'"'+password+'"'+'@patodb_high @query.sql'

p = sp.Popen(cmd, shell=True,universal_newlines=True,stdout=sp.PIPE,stderr=sp.PIPE)
#print (p.communicate()[0])
#print (p.communicate()[1])

outF = open("myOutFile.csv", "a")
outF.writelines((p.communicate()[0]))
outF.close()
