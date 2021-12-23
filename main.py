# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 20:16:03 2021

@author: Sergio Leal
"""
import pagoFunction

with open('workers.txt', "r") as data:
    FileContent = data.readlines()
    
weekend = ['SA','SU']

for worker in range(len(FileContent)):
    user,dWors = FileContent[worker].split('=')
    dias = dWors.strip('\n').split(',')
    
    x = []
    y = []
    mM = []
    dic = {}
    suma = 0

    for i in range(len(dias)):
        day = dias[i][2]
        hou = dias[i][1]

        x.append((dias[i].split(day))[0])
        y.append((dias[i].split(hou))[-1])
        m = int(y[i][0:2])
        M = int(y[i][6:8])
        dic.update({x[i]:[m,M]})

        if x[i] in weekend:
            flag = 2
            usd = pagoFunction.pago(m,M,flag)
        else:
            flag = 1
            usd = pagoFunction.pago(m,M,flag)
            
        suma += usd
        
    print(f'The amount to pay {user} is: {suma} USD')