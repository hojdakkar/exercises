# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 21:10:59 2020

@author: Karolina
"""

import turtle
import math

    
def polyline(t,n,length,angle):
    for i in range(n):
        t.fd(length)
        t.rt(angle)
        
def polygon(t,n,length):
    angle = 360.0/n
    polyline(t,n,length,angle)
    
def arch(t,r,angle):
    arch_length = 2*math.pi*r*angle/360
    n=int(arch_length/3)+1
    step_length = arch_length/n
    step_angle = float(angle)/n
    polyline(t,n,step_length,step_angle)
         
def circle(t,r):
    arch(t,r,360)
    
zenon= turtle.Turtle()
polyline(zenon,5,15,70)
polygon(zenon,5,70)
circle(zenon,25)

