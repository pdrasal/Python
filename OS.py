# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 14:43:18 2019

@author: patricio.a.drasal
"""

import subprocess
from subprocess import Popen, PIPE

def prred(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prgreen(skk): print("\033[92m {}\033[00m" .format(skk))
def pryellow(skk): print("\033[93m {}\033[00m" .format(skk))

myarg = input("Enter argument")
print(myarg)

#https://www.pythonforbeginners.com/os/subprocess-for-system-administrators/

cmd='sqlplus / as sysdba'
#subprocess.call(['dir', myarg],shell=True)
ver=subprocess.run(cmd,shell=True)
print(ver)
retcode = subprocess.run(cmd,shell=True)
if retcode == 0:
    prgreen('success')
else:
    prred('failed')

pryellow(f'Script execution completed')


#from subprocess import Popen, PIPE
#p = Popen(['command', 'and', 'args'], stdout=PIPE, stderr=PIPE, stdin=PIPE)
#
#output = p.stdout.read()
#p.stdin.write(input)
