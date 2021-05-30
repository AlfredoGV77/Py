
import matplotlib.pyplot as plt
import pandas as pd
import csv
import statistics as stats
import numpy as np
import matplotlib.dates as mdates
import datetime as dt
import pylab as pl


global datos
datos=pd.read_csv('datos.csv')
global df
df=pd.DataFrame(datos)



def abarra():
    tab=pd.crosstab(index=df['altura'],columns='frecuencia')
    
    plt.bar(tab.index,tab["frecuencia"])
    plt.xlabel("Frecuencia del Peso")
    plt.show()

def apastel():
    tab = pd.crosstab(index=df['altura'],columns='Frecuencia')

    pesos = [ item for item in df['peso']]

    data = pesos
    result = []
    for i in pesos:
                if i not in result:
                                result.append(i)
    result.sort()
    x=result
    freq = [ i for i in tab['Frecuencia']]
    fig1,ax1 = plt.subplots()
    ax1.pie(freq, labels=x, autopct='%1.1f%%',shadow=False, startangle=90)
    ax1.axis('equal')
    plt.show()
    

def aFAcumulada():
    tab = pd.crosstab(index=df['altura'],columns='Frecuencia')

    pesos = [ i for i in df['altura']]
    data = pesos
    result = []
    for i in data:
                if i not in result:
                                result.append(i)
    result.sort()
    freq = [ i for i in tab['Frecuencia']]

    orden=[]
    acumulado=0
    for valor in freq:
                acumulado = acumulado + valor 
                orden.append(acumulado)
    
    x = result
    x_pos = [i for i, _ in enumerate(result)]
    plt.bar(x_pos,orden, color='blue')

    plt.xticks(x_pos, x)
    plt.show()   
    
    

def aPoligonos():
    tab = pd.crosstab(index=df['altura'],columns='Frecuencia')

    pesos = [ i for i in df['altura']]
    resultado = []
    for i in pesos:
                if i not in resultado:
                                resultado.append(i)

    resultado.sort()

    frecuencia = [ i for i in tab['Frecuencia']]

    fig, ax = plt.subplots()
    ax.plot(resultado, frecuencia)
    plt.show()
