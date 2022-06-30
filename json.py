# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 18:20:37 2022

@author: chetu
"""

import json

d={
   'course_name':'python',
   'fees':15000
   
   
   }
print(type(d))
f=json.dumps(d)
print(f)
print(type(f))