# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:05:54 2024

@author: PC
bai 1: 
    --------------
    
"""

km = float(input("Nhập số km quãng đường đi được: "))
tien = 0
if km == 1:
    tien = 20000
elif km >=2 and km<=3:
    tien = km * 13000
elif km >= 4 and km <= 8:
    tien = 3 * 13000 + (km - 3) * 12000
else:
    tien = 3 * 13000 + 4 * 12000 + (km - 8) * 10000
if tien > 100000:
    tien *= 0.92
print(f"Tổng tiền taxi là: {tien:.0f} VND")
