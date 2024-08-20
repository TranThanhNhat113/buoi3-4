# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:57:40 2024

@author: Student
"""

chuoi = "i’m a cat"
a = chuoi.title()
b = chuoi.upper()
indices_to_upper = [2, 7, 8]
c = ''.join(c.upper() if i in indices_to_upper else c for i, c in enumerate(chuoi))
d= chuoi.capitalize()
print(a)
print(b)
print(c)
print(d)