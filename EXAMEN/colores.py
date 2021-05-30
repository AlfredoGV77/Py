
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



def cbarra():

    tab = pd.crosstab(index=df['color'],columns='Frecuencia')

    colores = [ i for i in df['color']]

    data = colores
    coloresClean=[]
    for elemento in colores:

                if(type(elemento)!=float):
                                coloresClean.append(elemento)

    result = []
    for i in data:
                if i not in result:
                                result.append(i)

    freq = [ i for i in tab['Frecuencia']]
    tam = len(result)
    tam = tam -1 
    result.pop(tam)
    freq.sort()
    coloresGrafica = ["cyan","yellow","green"]
    x_pos = [i for i, _ in enumerate(result)]

    plt.bar(x_pos, freq, color=coloresGrafica)

    plt.xticks(x_pos, result)
    plt.show()
    

def cpastel():
    tab = pd.crosstab(index=df['color'],columns='Frecuencia')

    colores = [ item for item in df['color']]
    data = colores
    coloresLimpio=[]
    for elemento in colores:

                if(type(elemento)!=float):
                                coloresLimpio.append(elemento)

    result = []
    for item in data:
                if item not in result:
                                result.append(item)

    freq = [ item for item in tab['Frecuencia']]
    tam = len(result)
    tam = tam -1 
    result.pop(tam)
    freq.sort()

    
    colores = ["cyan","gold","lime"]
    labels = result
    sizes = freq

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',colors=colores,shadow=True, startangle=90)
    ax1.axis('equal') 

    plt.show()
    

def cFAcumulada():
    print("No pude :(")
    

def cPoligonos():
    tab = pd.crosstab(index=df['color'],columns='Frecuencia')
    colores = [ item for item in df['color']]
    data = colores
    coloresLimpio=[]
    for elemento in colores:

                if(type(elemento)!=float):
                                coloresLimpio.append(elemento)
    result = []
    for i in colores:
                if i not in result:
                                result.append(i)
    freq = [ item for item in tab['Frecuencia']]
    tam = len(result)
    tam = tam -1 
    result.pop(tam)
    freq.sort()

    fig, ax = plt.subplots()
    ax.plot(result, freq)
    plt.show()
