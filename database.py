# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 11:27:19 2022

@author: chetu
"""

#database connectivity

import mysql.connector as c
con=c.connect(host="localhost", user="root",passwd="Pranjal@123",auth_plugin="mysql_native_password",database="test")
if con.is_connected():
    print("connected successfully")
    
else:
    print("not connected")