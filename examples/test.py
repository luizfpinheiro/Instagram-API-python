#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
import json 

api = InstagramAPI("user", "password")
if (api.login()):
    api.getSelfUserFeed()  # get self user feed
    print(api.LastJson)  # print last response JSON
     
    with open('userInfos.json', 'w') as file: # write log api.LastJson in a json file
        json.dump(api.LastJson, file) 

    
    print("Login succes!")
else:
    print("Can't login!")
