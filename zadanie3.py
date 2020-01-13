# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 22:35:29 2019

@author: Karolina
"""

import turtle #import modułu
bob= turtle.Turtle() #moduł turtle zapewnia funkcje Turtle tworząc obiekt żółwia przypisywany zmiennej bob
print(bob)

for i in range(4):
    bob.fd(100) # fd- forward- 
    bob.lt(90)

turtle.mainloop()


