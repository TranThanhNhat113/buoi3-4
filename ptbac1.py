# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 19:38:13 2024

@author: PC
"""

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
if a==0:
    if b==0:
        print("phuong trinh vo so nghiem")
    else :
        print("phuong trinh vo nghiem")
else:
    x = -b/a
    print("phuong trinh co 1 nghiem x=", x)
