# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 10:41:47 2022

@author: jaime.valenzuela
"""
import os
path = os.getcwd()
os.chdir(path)
import datetime as dt
import mktConventions as mktConv
import numpy as np
import flowFunc as fl
import math

# Busca el feriado de un vector de fechas y hace el shift de la fecha según su business convention.
def paymentConventionShift(fecha, calendarios, paymentConvention):
    if paymentConvention == "Following":
        while fecha in calendarios:
            fecha = fecha + dt.timedelta(days=1)
    elif paymentConvention == "Preceding":
        while fecha in calendarios:
            fecha = fecha + dt.timedelta(days=-1)
    return fecha

#Es una funcion que hace el cambio de fechas de manera recursiva, es decir partiendo desde la fecha de vencimiento
def shiftDate(fecha, dayFreq):
    #Composicion Americana
    if (dayFreq == "Daily"):
        fecha = fecha + dt.timedelta(days=-1)#
    if (dayFreq == "Monthly"):
        fecha = fecha + dt.timedelta(months=-1)
    if (dayFreq == "Quarterly"):
        fecha = fecha + dt.timedelta(months=-3)#fecha.AddMonths(-3);
    if (dayFreq == "Semi-Annual"):
        fecha = fecha + dt.timedelta(months=-6)#fecha.AddMonths(-6);
    if (dayFreq == "Annual"):
        fecha = fecha + dt.timedelta(months=-12)#fecha.AddMonths(-12);

    #Composicion MXN
    if (dayFreq == "Daily (1/360)"):
        fecha = fecha + dt.timedelta(days=-1)#fecha.AddDays(-1);
    if (dayFreq == "Monthly (28/360)"):
        fecha = fecha + dt.timedelta(days=-28)#fecha.AddDays(-28);
    if (dayFreq == "Quarterly (91/360)"):
        fecha = fecha + dt.timedelta(days=-91)#fecha.AddDays(-91);
    if (dayFreq == "Semi-Annual (182/360)"):
        fecha = fecha + dt.timedelta(days=-182)#fecha.AddDays(-182);
    if (dayFreq == "Annual (364/360)"):
        fecha = fecha + dt.timedelta(days=-364)#fecha.AddDays(-364);

    return fecha;

#Genera la cantidad de cupones que tendra el instrumento
def paymentCoupons(fechaVencimiento, fechaEmision, paymentComposition):
    yearDiff = fechaVencimiento.year - fechaEmision.year
    monthDiff = fechaVencimiento.month - fechaEmision.month
    #dayDiff = fechaVencimiento.day - fechaEmision.day
    paymentsInYear = np.round(1 / mktConv.yieldComposition(paymentComposition),0)
    
    if paymentComposition == "Monthly" or paymentComposition == "Monthly (28/360)":
        cantPagos = paymentsInYear * yearDiff + monthDiff #Cantidad de pagos en un año * cantidad de años
    elif paymentComposition == "Quarterly" or paymentComposition == "Quarterly (91/360)":
        cantPagos = paymentsInYear * yearDiff + math.ceil(monthDiff / 4.00)
    elif paymentComposition == "Semi-Annual" or paymentComposition == "Semi-Annual (182/360)":
        cantPagos = paymentsInYear * yearDiff + math.ceil(monthDiff / 6.00)
    elif paymentComposition == "None":
        cantPagos = 1
    else:
        cantPagos = paymentsInYear * yearDiff; #Cantidad de pagos en un año * cantidad de años 
    
    return cantPagos
    
def fechasFlujos(fechaVencimiento, valDate, paymentComposition, paymentConvention, holidays):
    intCantPagos = np.int64(fl.paymentCoupons(fechaVencimiento, valDate, paymentComposition))
    
    fechaFinal = [fechaVencimiento]
    fechaInicial = [fl.paymentConventionShift(fl.shiftDate(fechaFinal[0], paymentComposition), holidays, paymentConvention)]
    fechaFinalAdj = []
    fechaInicialAdj = []
    for i in range(intCantPagos):
        if i>0:
            fechaFinal.append(fechaInicial[i-1])
            fechaInicial.append(fl.shiftDate(fechaFinal[i], paymentComposition))    
        
        fechaFinalAdj.append(fl.paymentConventionShift(fechaFinal[i], holidays, paymentConvention))
        fechaInicialAdj.append(fl.paymentConventionShift(fechaInicial[i], holidays, paymentConvention))        
    
    fechaInicialAdj.sort()
    fechaFinalAdj.sort()
    
    return np.column_stack((fechaInicialAdj,fechaFinalAdj))

#m = base/periodo e.g 360/182 (yield compound) n = days / base
def df(n, m, rate, dfConvention):
    if dfConvention == "Linear":
        df = 1 / (1+rate*n)
    elif dfConvention == "Compound":
        df = 1 / (1+rate/m)**(m*n)
        #hay que poner que pasa si es true period como en los amortizables  1 / (1+rate*dias_cupon/360)**(du/dcupon) 
    elif dfConvention == "Exponential":
        df = np.exp(-rate*n)
    return df    
    
    
    
    
    
