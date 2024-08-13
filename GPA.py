# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 19:36:52 2024

@author: PC
"""

GPA=float(input("nhap diem trung binh(GPA): "))
if GPA < 3.5:
    print("hoc kuc kem")
elif GPA >=3.5 and GPA <5.0:
    print("hoc luc yeu")
elif GPA >=5.0 and GPA <7.0:
    print("hoc luc trung binh")
elif GPA >=7.0 and GPA <8.0:
    print("hoc luc kha")
elif GPA >=8.0 and GPA <9.0:
    print("hoc luc gioi")
else:
    print("hoc luc xuat sac")