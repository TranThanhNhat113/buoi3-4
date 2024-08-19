# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 21:56:53 2024

@author: PC
"""

import math 
a = float(input("Nhap so thuc a:"))
b = float(input("Nhap so thuc b:"))
a1=math.sqrt(a)
a2=math.sqrt(math.sqrt(a))
ab=math.sqrt(math.sqrt(a*b))
b1=math.sqrt(b)
b2=math.sqrt(math.sqrt(b))
x = ((a1-b1)/(a2-b2)) - ((a1+ab)/(a2+b2))
print(f"Gia tri cua bieu thuc la: {x}")
