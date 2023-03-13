# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 15:54:03 2022

@author: jaime.valenzuela
"""
import pandas as pd
import pyodbc

def InstrumentData(instrumento):
    #fecha_proceso = dt.datetime(2022,2,15)
    #instrumento = 'M_BONOS_381118'
    sql_conn = pyodbc.connect('DRIVER={SQL Server};SERVER=VMTDBDEVELO;uid=Riesgo;Trusted_Connection=True') 
    
    query = """select * FROM BOND_BD_TEST  where TICKER = '"""+ instrumento +"""'"""
        
    return pd.read_sql(query, sql_conn)