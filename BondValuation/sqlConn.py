# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 12:22:05 2022

@author: jaime.valenzuela
"""
import pandas as pd
import pyodbc

sql_conn = pyodbc.connect('DRIVER={SQL Server};SERVER=VMTDBDEVELO;uid=Riesgo;Trusted_Connection=True') 

query = """select * from Bonos.Instrumento where Nombre  = 'M_BONOS_381118'"""

df = pd.read_sql(query, sql_conn)

