# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:04:08 2020

@author: Administrator
"""

import azure.cosmos.cosmos_client as cosmos_client

url = 'https://az900-accountdbnamepato.documents.azure.com:443/'
key = 'U0X4qQmVVykFdecJfKWlBoZRElgzmvmIgTwLWU2xqK5JBAcPR82K0kUTGjtlrDveversDuB7FnIjbkQSsK4cWg=='
client = cosmos_client.CosmosClient(url, {'masterKey': key})


### esto funcionó --> client.create_database('Prueba')

database_id = 'WorldData'
container_id = 'container1'
#container = client.ReadContainer("dbs/" + database_id + "/colls/" + container_id)

# Enumerate the returned items
import json
for item in client.QueryItems("dbs/" + database_id + "/colls/" + container_id,
                              'SELECT * FROM ' + container_id + ' r WHERE r.id="item3"',
                              {'enableCrossPartitionQuery': True}):
    print(json.dumps(item, indent=True))