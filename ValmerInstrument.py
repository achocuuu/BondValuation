# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 10:44:11 2022

@author: jaime.valenzuela
"""
import pandas as pd
import pyodbc

def ValmerVector(fecha_proceso,instrumento):
    #fecha_proceso = dt.datetime(2022,2,15)
    
    fecha_str=fecha_proceso.strftime("%Y%m%d")
    #instrumento = 'M_BONOS_381118'
    sql_conn = pyodbc.connect('DRIVER={SQL Server};SERVER=VMTDBDEVELO;uid=Riesgo;Trusted_Connection=True') 
    
    #query = """select * from Valmer.Vector where fecha  = '""" +fecha_str+""" and instrumento = '""" + instrumento + """'"""
    
    query = """SELECT 
        FECHA
        , INSTRUMENTO
        , PRECIOSUCIO
        , PRECIOLIMPIO
        , INTERESES
        , DIASVENC
        , PLAZO
        , SOBRETASA
        , RENDIMIENTO
        , DURACION
        , CONVEXIDAD
        , TASACUPON
    FROM 
        VALMER.VECTOR
    WHERE 
        FECHA = '""" + fecha_str +"""' 
        AND INSTRUMENTO = '"""+ instrumento +"""'"""
        
    return pd.read_sql(query, sql_conn)