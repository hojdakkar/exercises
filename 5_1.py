# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 21:50:48 2020

@author: Karolina
"""

def check_fermat(a,b,c,n):
    if n>2:
        if a**n + b**n == c**n :
            print('Do licha, Fermat się mylił!')
        else:
            print('Nie, to nie działa')
    else:
        print('N jest mniejsze badz rowne 2')
        
def function():
    prompt='Wprowadź wartosc paramtetru\n'
    a = input(prompt)
    a = int(a)
    b = input(prompt)
    b = int(b)
    c = input(prompt)
    c = int(c)
    n = input(prompt)
    n = int(n)
    return a,b,c,n

    
a,b,c,n = function()
print(a,b,c,n)
check_fermat(a,b,c,n)
