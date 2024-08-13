# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 20:25:34 2024

@author: PC
"""

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
delta = b**2 - 4*a*c
import math
if a == 0:
    if b == 0:
        print("Vô nghiệm hoặc vô số nghiệm")
    else:
        print("Nghiệm: {}".format(-c / b))
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Nghiệm phân biệt: x1 = {}, x2 = {}".format(x1, x2))
    elif delta == 0:
        print("Nghiệm kép: x = {}".format(-b / (2 * a)))
    else:
        print("Vô nghiệm")