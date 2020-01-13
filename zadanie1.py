# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 20:46:23 2019

@author: Karolina
"""

def right_justify(s,x):
    print((x-len(s))*' ' + s)
    
z=['zdanie','oj','ala ma kota', 'fiu bzdziu i trele morele']
for i in z:
    right_justify(i,40)

print(5*'ala ma kota ') 