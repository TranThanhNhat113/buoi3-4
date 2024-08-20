# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 18:41:38 2024

@author: Student
"""

chuoi = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
sub_strings = [s.strip() for s in chuoi.split(',')]
for s in sub_strings:
    print(s)
