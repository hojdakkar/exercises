# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 21:28:07 2019

@author: Karolina
"""

def do_twice(f,g):
    f(g)
    f(g)
     
def print_spam(a): 
    print(a)
    
def print_ham(b): 
    print('spam')
    
do_twice(print_spam,' mikołajeq')
do_twice(print_ham,' mikołajeq')


    