# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 13:19:50 2020

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

def flower(t,r,n):
    angle=360.0/n
    for i  in range(n):
        t.setheading(i*angle)
        arch(t,r,angle)
        t.rt(180-angle)
        arch(t,r,angle)


        #an = an + angle + 180.0
       # print(an%360.0)
#        t.rt(2*angle)
#        t.rt(angle+90.0)  
        
zenon= turtle.Turtle()
zenon.speed(0)       
flower(zenon,100,17)
         
    
#arch(zenon,100,90)
#zenon.rt(90)
#arch(zenon,100,90)
#arch(zenon,100,90)
#zenon.rt(90)
#arch(zenon,100,90)
#arch(zenon,100,90)
#zenon.rt(90)
#arch(zenon,100,90)
#arch(zenon,100,90)
#zenon.rt(90)
#arch(zenon,100,90)
#
#zenon.rt(45)
#arch(zenon,100,90)
#zenon.rt(90)
#arch(zenon,100,90)
#arch(zenon,100,90)
#zenon.rt(90)
#arch(zenon,100,90)
#arch(zenon,100,90)
#zenon.rt(90)
#arch(zenon,100,90)
#arch(zenon,100,90)
#zenon.rt(90)
#arch(zenon,100,90)