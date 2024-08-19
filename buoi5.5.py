# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:58:49 2024

@author: Student
"""
from datetime import datetime
Namsinh=int(input("Nhap nam sinh: "))
dt=datetime.now().year
tuoi=dt-Namsinh
print(f"Bạn sinh năm {Namsinh} vậy bạn {tuoi} tuổi")