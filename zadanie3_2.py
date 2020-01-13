# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 14:25:32 2019

@author: Karolina
"""

import turtle
import math

def square(t,length):
    for i in range(4):
        t.fd(length) # fd- forward- 
        t.rt(90)

def polygon(t,n,length):#n- l.boków
    angle=360/n
    for i in range(n):
        t.fd(length) # fd- forward- 
        t.rt(angle)
        
def circle(t,r):
    circumference=2*math.pi*r
    n=128
    length=circumference/n
    polygon(t,n,length)


def arch(t,r,angle):
    arch_length = 2*math.pi*r*angle/360
    n=int(arch_length/3)+1
    step_length = arch_length/n
    step_angle = angle/n
    
    for i in range(n):
        t.fd(step_length)
        t.rt(step_angle)
    
zenon= turtle.Turtle()
polygon(zenon,7,70)
circle(zenon,50)
arch(zenon,60,160)
