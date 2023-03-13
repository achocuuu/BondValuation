# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 15:49:24 2022

@author: jaime.valenzuela
"""
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
import ValmerInstrument as valmer
import InstrumentData as iData
import warnings
warnings.filterwarnings('ignore')
import pandas as pd


def BondValuation(instrumento,valDate,yield_rate):
    #Bond/Instrument Data
    dataBond = iData.InstrumentData(instrumento)
    notional = dataBond['NOMINAL'][0]
    tasaCupon = dataBond['TASA_CUPON'][0]
    # instrument_type = dataBond['INSTRUMENT_TYPE'][0] #Usar para cuando
    fechaVencimiento = dt.datetime.strptime(dataBond['FECHA_VENCIMIENTO'][0],'%Y-%m-%d')
    yieldComposition = dataBond['YIELD_COMPOSITION'][0]
    paymentComposition = yieldComposition
    dayCountConvention = dataBond['YIELD_BASIS'][0]
    yieldCalcMethod = dataBond['YIELD_CALC_METHOD'][0]
    #FERIADOS
    holidays = cMXN.holidays(valDate, fechaVencimiento)
    
    fechas_flujos = fl.fechasFlujos(fechaVencimiento, valDate, paymentComposition, "Following", holidays)
    dcf = [] 
    dcf_to_Maturity = []
    interes= []
    amortizacion = []
    flujo = []
    dfactor = []
    vp = []
    #Poner condicion si es Amortizable, Bullet, Amortizable_Calendarizado, De un Solo Flujo.
    #Calculo para bullet
    for i in range(len(fechas_flujos)):
        dcf.append(mktConv.dayCountFactor(fechas_flujos[i,0], fechas_flujos[i,1], dayCountConvention))
        interes.append(mktConv.dayCountFactor(fechas_flujos[i,0], fechas_flujos[i,1], dayCountConvention)*tasaCupon*notional)
        amortizacion.append(notional if i==len(fechas_flujos)-1 else 0.0)
        flujo.append(mktConv.dayCountFactor(fechas_flujos[i,0], fechas_flujos[i,1], dayCountConvention)*tasaCupon*notional + notional if i==len(fechas_flujos)-1 else mktConv.dayCountFactor(fechas_flujos[i,0], fechas_flujos[i,1], dayCountConvention)*tasaCupon*notional)
        dcf_to_Maturity.append(mktConv.dayCountFactor(valDate, fechas_flujos[i,1], dayCountConvention))
        m = 1 / mktConv.dayCountFactor(fechas_flujos[i,0], fechas_flujos[i,1], dayCountConvention) if yieldCalcMethod == "True Period" else 1 / mktConv.yieldComposition(yieldComposition)
        n = dcf_to_Maturity[i]
        dfactor.append(fl.df(n, m, yield_rate, "Compound"))#df.append(1/(1+yield_rate/m)**(m*n))       
        vp.append(dfactor[i]*flujo[i])
    
    return sum(vp)


def main():
   #Bond Data Input
    instrumento = 'S_UDIBONO_401115'
    valDate = dt.datetime(2022,1,3)
    yield_rate = 0.03
    Valor_Mercado = "Yes"
    #Valmer data
    dataValmer = valmer.ValmerVector(valDate, instrumento)
    precio_valmer = dataValmer['PRECIOSUCIO'][0]
    
    yield_rate = dataValmer['RENDIMIENTO'][0]/100 if Valor_Mercado == "Yes" else yield_rate
    
    vp = BondValuation(instrumento, valDate, yield_rate)
    #MONEDA
    udi_valmer = valmer.ValmerVector(valDate, '*C_MXPUDI_UDI')
    udi = udi_valmer['PRECIOSUCIO'][0]
    
    print("Precio :" + str(vp))
    print("Precio Valmer: " + str(precio_valmer/udi))
    
if __name__ == '__main__':
    main()


