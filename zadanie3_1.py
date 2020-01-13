# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 23:00:24 2019

@author: Karolina
"""

import turtle
import math

def square(t,length):
    for i in range(4):
        t.fd(length) # fd- forward- 
        t.rt(90)

def polygon(t,length,n):#n- l.boków
    angle=360/n
    for i in range(n):
        t.fd(length) # fd- forward- 
        t.rt(angle)
        
def circle(t,r):
    length=2*math.pi*r/128
    polygon(t,length,128)
    
def arch(t,r,angle):
    circumferential=2*math.pi*r
    n=128
    length=circumferential/n
    polygon(t,n,length)
    
zenon= turtle.Turtle()
#square(zenon,50)
#polygon(zenon,50,12)
circle(zenon,50)
arch(zenon,50,30)
print(zenon)


 