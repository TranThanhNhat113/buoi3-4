# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:03:59 2024

@author: PC
"""

import random
Luachon = ["kéo", "búa", "bao"]
ngchoi = input("Lựa chọn (kéo-búa-bao): ")
may = random.choice(Luachon)
print(f"Bạn chọn: {ngchoi}")
print(f"Máy chon: {may}")
if ngchoi == may:
    print("Hoa")
elif ngchoi =="kéo" and may == "bao" or \
     ngchoi =="búa" and may == "kéo" or \
     ngchoi =="bao" and may == "búa" :
    print("Bạn thắng")
else:
    print("Bạn thua")