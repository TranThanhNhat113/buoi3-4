# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:33:34 2024

@author: Student
"""

N=int(input("Nhập 2 số nguyên dương: "))
a= N//10
b= N%10
tong=a+b
if 10 <= N <= 99:
    print("Tổng các chữ số của N:", tong)
else:
    print("N không phải là 2 số nguyên dương, hãy nhập lại!!!")