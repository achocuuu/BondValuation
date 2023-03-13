# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 10:22:28 2022

@author: jaime.valenzuela
"""

def dayCountFactor(fecha_inicial, fecha_final, dayCountConvention):
    yearFraction = 0
    Y1 = fecha_inicial.year
    Y2 = fecha_final.year;
    M1 = fecha_inicial.month;
    M2 = fecha_final.month;
    D1 = fecha_inicial.day;
    D2 = fecha_final.day;
    
    if dayCountConvention == "30/360": 
        #Condicion de mes 31 para el día
        if D1 == 31:
            D1 = 30
        if D2 == 31 and (D1 == 30 or D1 == 31):
            D2 = 30
    
        yearFraction = (360 * (Y2 - Y1) + 30 * (M2 - M1) + (D2 - D1)) / 360.00
        
        
    elif dayCountConvention == "30E/360": #Llamado eurobond basis
    #Condicion de mes 31 para el día
        if D1 == 31:
            D1 = 30
        if D2 == 31:
            D2 = 30
        yearFraction = (360 * (Y2 - Y1) + 30 * (M2 - M1) + (D2 - D1)) / 360.00
        
    
    elif dayCountConvention == "Act/360":
        yearFraction = (fecha_final - fecha_inicial).days / 360.00
    
    elif dayCountConvention == "Act/365":
        yearFraction = (fecha_final - fecha_inicial).days / 365.00

    return yearFraction

def yieldComposition(dayFreq, baseCount = 360):

    dayCountComposition = 0
    if dayFreq == "Daily":
        if baseCount==360:
            dayCountComposition = 1 / 360
        elif baseCount == 365:
            dayCountComposition = 1 / 365
        else:
            dayCountComposition = 1 / baseCount
    
    if (dayFreq == "Monthly"):
        dayCountComposition = 1.0 / 12.0
    if (dayFreq == "Quarterly"):
        dayCountComposition = 1.0 / 4.0
    if (dayFreq == "Semi-Annual"):
        dayCountComposition = 1.0 / 2.0
    if (dayFreq == "Annual"):
        dayCountComposition = 1.0 / 1.0
    #Composicion MXN
    if (dayFreq == "Daily (1/360)"):
        dayCountComposition = 1.0 / 360.0
    if (dayFreq == "Monthly (28/360)"):
        dayCountComposition = 28.0 / 360.0
    if (dayFreq == "Quarterly (91/360)"):
        dayCountComposition = 91.0 / 360.0
    if (dayFreq == "Semi-Annual (182/360)"):
        dayCountComposition = 182.0 / 360.0
    if (dayFreq == "Annual (364/360)"):
        dayCountComposition = 364.0 / 360.0
    if (dayFreq == "None" or dayFreq == "True"):
        dayCountComposition = 1
    
    
    return dayCountComposition

def dayCount(fecha_inicial, fecha_final, dayCountConvention):
    yearFraction = 0
    Y1 = fecha_inicial.year
    Y2 = fecha_final.year;
    M1 = fecha_inicial.month;
    M2 = fecha_final.month;
    D1 = fecha_inicial.day;
    D2 = fecha_final.day;
    
    if dayCountConvention == "30/360": 
        #Condicion de mes 31 para el día
        if D1 == 31:
            D1 = 30
        if D2 == 31 and (D1 == 30 or D1 == 31):
            D2 = 30
    
        yearFraction = (360 * (Y2 - Y1) + 30 * (M2 - M1) + (D2 - D1))
        
        
    elif dayCountConvention == "30E/360": #Llamado eurobond basis
    #Condicion de mes 31 para el día
        if D1 == 31:
            D1 = 30
        if D2 == 31:
            D2 = 30
        yearFraction = (360 * (Y2 - Y1) + 30 * (M2 - M1) + (D2 - D1))
        
    
    elif dayCountConvention == "Act/360":
        yearFraction = (fecha_final - fecha_inicial).days
    
    elif dayCountConvention == "Act/365":
        yearFraction = (fecha_final - fecha_inicial).days

    return yearFraction

   
    