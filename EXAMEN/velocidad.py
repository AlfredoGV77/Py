
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

import statistics as stats
def vbarra():

    tab = pd.crosstab(index=df['velocidad'],columns='Frecuencia')
    velocidad = [ i for i in df['velocidad']]

    data = velocidad
    result = []
    for i in data:
                if i not in result:
                                result.append(i)

    dataLimpio=[]
    for i in result:
                
                if i > 0:
                                dataLimpio.append(i)

    dataLimpio.sort()

    
    freq = [ item for item in tab['Frecuencia']]
    x = dataLimpio
    energy = freq

    x_pos = [i for i, _ in enumerate(dataLimpio)]

    plt.bar(x_pos, freq, color='purple')
    plt.xticks(x_pos, dataLimpio)
    plt.show()


def vPastel():
    tab = pd.crosstab(index=df['velocidad'],columns='Frecuencia')
    velocidad = [ i for i in df['velocidad']]
    data = velocidad
    result = []
    for i in data:
                if i not in result:
                                result.append(i)

    dataLimpio=[]
    for i in result:
                
                if i > 0:
                                dataLimpio.append(i)
    dataLimpio.sort()
    freq = [ i for i in tab['Frecuencia']]
    labels = dataLimpio
    sizes = freq
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()

def vFAcumulada():
    tab = pd.crosstab(index=df['velocidad'],columns='Frecuencia')
    velocidad = [ i for i in df['velocidad']]

    data = velocidad
    result = []
    for i in data:
                if i not in result:
                                result.append(i)

    dataLimpio=[]
    for i in result:
                if i > 0:
                                dataLimpio.append(i)

    dataLimpio.sort()

    freq = [ i for i in tab['Frecuencia']]


    orden=[]
    acumulado=0
    for valor in freq:
                acumulado = acumulado + valor 
                orden.append(acumulado)


    x = dataLimpio
    energy = orden

    x_pos = [i for i, _ in enumerate(x)]
    plt.bar(x_pos, orden, color='green')
    plt.xticks(x_pos, dataLimpio)
    plt.show()

def vPoligono():
    tab = pd.crosstab(index=df['velocidad'],columns='Frecuencia')
    velocidad = [ item for item in df['velocidad']]
    result = []
    for i in velocidad:
                if i not in result:
                                result.append(i)
    dataLimpio=[]
    for i in result:
                
                if i > 0:
                                dataLimpio.append(i)

    dataLimpio.sort()

    freq = [ i for i in tab['Frecuencia']]

    fig, ax = plt.subplots()
    ax.plot(dataLimpio, freq)
    plt.show()