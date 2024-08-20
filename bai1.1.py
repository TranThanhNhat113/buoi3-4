# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 20:00:02 2024

@author: Student
"""

chuoi = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
sub_strings = [s.strip() for s in chuoi.split(',')]
loaibo = [s.replace('P. ', '').replace('Q. ', '').replace('Tp. ', '') for s in sub_strings]
for s in loaibo:
    print(s)
