# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:50:29 2024

@author: Student
"""

a=int(input("Nhap so a: "))
b=int(input("Nhap so b: "))
tong= a+b
hieu= a-b
tich= a*b
print("tong 2 so la: ", tong)
print("hieu 2 so la: ", hieu)
print("tich 2 so la: ", tich)
if b!=0:
    thuong= a/b
    chia_lay_du= a%b
    chia_lay_nguyen= a//b
    print("Thương: ", round(thuong,3))
    print("Chia lấy dư: ", chia_lay_du)
    print("Chia lấy nguyên: ", chia_lay_nguyen)
else:
    thuong= chia_lay_du= chia_lay_nguyen= "khong the chia het cho 0"
    print("thuong: ", thuong)
