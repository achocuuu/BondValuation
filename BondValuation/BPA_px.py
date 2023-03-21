# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 09:42:54 2023

@author: jaime.valenzuela
"""
import pandas as pd
import tkinter
from tkinter import filedialog
import os
path = "C:\\Users\\jaime.valenzuela\\Documents\\Spyder_Scripts\\pyfiles\\VMetrix\\BondValuation\\"
os.chdir(path) #C:\Users\jaime.valenzuela\Documents\Spyder_Scripts\pyfiles\VMetrix\BondValuation
import sys
import datetime as dt
import mktConventions as mktConv
from datetime import datetime
import flowFunc as fl
# import numpy as np
import calendar_MXN as cMXN
sys.path.insert(1,"C:\\Users\\jaime.valenzuela\\Documents\\Spyder_Scripts\\pyfiles\\VMetrix")
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import math

#get vector
# tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
# folder_path = filedialog.askopenfilename(title='Tasas de Referencia') #JVG-20220901: Gets the file from a window that appear
# file = os.path.split(folder_path)[1]#res[1]
# ruta = os.path.split(folder_path)[0]
# separador = ','
# data = pd.read_csv(folder_path,sep=separador)

#Bond Data Input
instrumento = 'IQ_BPAG91_240111'
valDate = dt.datetime(2023,3,17)
yield_rate = 0.1178
notional = 100.0 
tasaCupon = 10.82/100.00 #if FX
tasaCuponVigente = 10.82/100.0 #if FL
tasaCuponFF = 11.63/100.0 #if FL
tipoBono = "FL"
# instrument_type = dataBond['INSTRUMENT_TYPE'][0] #Usar para cuando
fechaVencimiento = dt.datetime.strptime('2024-01-11','%Y-%m-%d')
yieldComposition = "Quarterly (91/360)"
paymentComposition = yieldComposition
dayCountConvention = "Act/360"
yieldCalcMethod = "True Period" # dataBond['YIELD_CALC_METHOD'][0]
#FERIADOS
holidays = cMXN.holidays(valDate, fechaVencimiento)

fechas_flujos = fl.fechasFlujos(fechaVencimiento, valDate, paymentComposition, "Preceding", holidays)
dcf = [] 
dcf_to_Maturity = []
interes= []
amortizacion = []
flujo = []
dfactor = []
vp = []
tasa_cupon = []
#Calculo para bullet
for i in range(len(fechas_flujos)):
    
    if(i==0 and tipoBono == "FL"):
        tasaCupon = tasaCuponVigente
    elif(tipoBono == "FL"):
        tasaCupon = tasaCuponFF   
    dcf.append(mktConv.dayCountFactor(fechas_flujos[i,0], fechas_flujos[i,1], dayCountConvention))
    tasa_cupon.append(tasaCupon)
    interes.append(mktConv.dayCountFactor(fechas_flujos[i,0], fechas_flujos[i,1], dayCountConvention)*tasaCupon*notional)
    amortizacion.append(notional if i==len(fechas_flujos)-1 else 0.0)
    flujo.append(mktConv.dayCountFactor(fechas_flujos[i,0], fechas_flujos[i,1], dayCountConvention)*tasaCupon*notional + notional if i==len(fechas_flujos)-1 else mktConv.dayCountFactor(fechas_flujos[i,0], fechas_flujos[i,1], dayCountConvention)*tasaCupon*notional)
    dcf_to_Maturity.append(mktConv.dayCountFactor(valDate, fechas_flujos[i,1], dayCountConvention))
    m = 1 / mktConv.dayCountFactor(fechas_flujos[i,0], fechas_flujos[i,1], dayCountConvention) if yieldCalcMethod == "True Period" else 1 / mktConv.yieldComposition(yieldComposition)
    n = dcf_to_Maturity[i]
    dfactor.append(fl.df(n, m, yield_rate, "Compound"))#df.append(1/(1+yield_rate/m)**(m*n))       
    vp.append(dfactor[i]*flujo[i])
    

d = {"Fecha Inicial": fechas_flujos[:,0], "Fecha Final": fechas_flujos[:,1], "Day Count Factor": dcf, "Tasa Cupon": tasa_cupon, "Interes": interes,
     "Amortizacion": amortizacion, "Flujo": flujo, "DCF Maturity": dcf_to_Maturity,"Discount Factor": dfactor, "PV": vp}
df = pd.DataFrame(d)


sum(vp)


