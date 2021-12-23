# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 20:57:57 2021

@author: Sergio Leal
"""

def pago(m,M,flag):
    
    M=24 if M==0 else M
    time = M-m
    m=0.1 if m==0 else m
    
    pg = {1:[25,15,20],2:[30,20,25]} # 1 Para MO2FR 2 para SA2SU
    dolar = pg[flag]
    
    if m>0 and M<=9:
        earn = time*dolar[0]
    elif m>9 and M<=18:
        earn = time*dolar[1]
    else:
        earn = time*dolar[2]
        
    return(earn)