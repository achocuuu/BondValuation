# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 16:17:34 2021

@author: jaime.valenzuela
"""
import datetime as dt
#import pandas as pd

def holidays(fecha_ini,fecha_fin):
    holidays = []
    years = fecha_fin.year - fecha_ini.year 

    for i in range(years+1):
        year = fecha_ini.year + i
        holidays.append(newyear(year)) 
        holidays.append(GoodFriday(year))
        holidays.append(HolyThurdsday(year))
        holidays.append(ConstitutionDay(year))
        holidays.append(JuarezBirthday(year))
        holidays.append(laborDay(year))
        holidays.append(IndependenceDay(year))
        holidays.append(AllSoulsDay(year))
        holidays.append(MexicanRevolution(year))
        holidays.append(OurLadyGuadalpe(year))
        holidays.append(navidad(year))
           
    for i in range((fecha_fin - fecha_ini).days):
        
        fecha_t = fecha_ini + dt.timedelta(i)
        if fecha_t.weekday() == 5 or fecha_t.weekday() == 6:
            holidays.append(fecha_t)

    holidays.sort()
    return holidays
    
def newyear(year):
    new_year = dt.datetime(year,1,1)
    return new_year

def EasterDate(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1    
    return dt.datetime(year, month, day)

def GoodFriday(year):
    easter = EasterDate(year)
    friday = easter - dt.timedelta(days=2)
    return friday

def HolyThurdsday(year):
    easter = EasterDate(year)
    thursdayHoly = easter - dt.timedelta(days=3)
    return thursdayHoly
    
def ConstitutionDay(year):
    constitutionDay = dt.datetime(year,2,1)
    dayOfWeek = constitutionDay.weekday()
    while dayOfWeek != 0:
        constitutionDay = constitutionDay + dt.timedelta(days=1)
        dayOfWeek = constitutionDay.weekday()
    return constitutionDay

def JuarezBirthday(year):
    juarezBirthday = dt.datetime(year,3,1)
    dayOfWeek = juarezBirthday.weekday()
    while dayOfWeek != 0:
        juarezBirthday = juarezBirthday + dt.timedelta(days=1)
        dayOfWeek = juarezBirthday.weekday()
    return juarezBirthday

def laborDay(year):
    laborDay = dt.datetime(year,5,1)
    return laborDay

def IndependenceDay(year):
    IndependenceDay = dt.datetime(year,9,16)
    return IndependenceDay

def AllSoulsDay(year):
    AllSoulsDay = dt.datetime(year,11,2)
    return AllSoulsDay

def MexicanRevolution(year):
    MexicanRevolution = dt.datetime(year,11,1)
    dayOfWeek = MexicanRevolution.weekday()
    while dayOfWeek != 0:
        MexicanRevolution = MexicanRevolution + dt.timedelta(days=1)
        dayOfWeek = MexicanRevolution.weekday()
    return MexicanRevolution

def OurLadyGuadalpe(year):
    OurLadyGuadalpe = dt.datetime(year,12,12)
    return OurLadyGuadalpe


def navidad(year):
    navidad = dt.datetime(year,12,25)
    return navidad

