# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 11:59:48 2022

@author: chetu
"""

class DemoClass:
    a=10
    b=2
    #constructor is initiated using init and 
    #it is not required to call
    def __init__(self):
        print("welcome to constructor")
    def showvalue(self):
        print(self.a)
        self.c=self.a*self.b
        print(self.c)
        
    def suma(self,a,b):
        print(a+b)
obj=DemoClass()
obj.showvalue()
obj.suma(4,1)