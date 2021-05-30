


# Youtube: https://www.youtube.com/c/MagnoEfren

from tkinter import Tk, Label, Button, Frame,  messagebox, filedialog, ttk, Scrollbar, VERTICAL, HORIZONTAL
import pandas as pd
from tkinter import *
import random
import re


ventana = Tk()
ventana.config(bg='black')
ventana.geometry('600x400')
ventana.minsize(width=600, height=400)
ventana.title('Consulta de elementos que inicien con S y tengan un precio mayor a 1000')

ventana.columnconfigure(0, weight = 25)
ventana.rowconfigure(0, weight= 25)
ventana.columnconfigure(0, weight = 1)
ventana.rowconfigure(1, weight= 1)

frame1 = Frame(ventana, bg='gray26')
frame1.grid(column=0,row=0,sticky='nsew')
frame2 = Frame(ventana, bg='gray26')
frame2.grid(column=0,row=1,sticky='nsew')

frame1.columnconfigure(0, weight = 1)
frame1.rowconfigure(0, weight= 1)

frame2.columnconfigure(0, weight = 1)
frame2.rowconfigure(0, weight= 1)
frame2.columnconfigure(1, weight = 1)
frame2.rowconfigure(0, weight= 1)

frame2.columnconfigure(2, weight = 1)
frame2.rowconfigure(0, weight= 1)

frame2.columnconfigure(3, weight = 2)
frame2.rowconfigure(0, weight= 1)



def datos_excel():

	datos_obtenidos = indica['text']
	try:
		archivoexcel = r'{}'.format(datos_obtenidos)
		df=pd.read_excel("camaras2.xlsx",sheet_name="csv_camaras_2.csv",header=0, usecols=[0,2,7])

	except ValueError:
		messagebox.showerror('Informacion', 'Formato incorrecto')
		return None

	except FileNotFoundError:
		messagebox.showerror('Informacion', 'El archivo esta \n malogrado')
		return None

	Limpiar()

	tabla['column'] = list(df.columns)
	tabla['show'] = "headings"  #encabezado
     

	for columna in tabla['column']:
		tabla.heading(columna, text= columna)
	
	#Aqui se filtran los datos, el anterior solo eran las columnas
	df_fila = df.to_numpy().tolist()
	#Aqui recorremos cada dato del excel
	for fila in df_fila:
		#Lo que hace es buscar los datos que empiecen por una S
		letra_inicial=fila[0].find("S")
		#Si la posicion de la S es 0 entonces empieza por s
		#Se agregan las condiciones de filtrado
		#Ojo, los datos se guardan en listas
		if(letra_inicial==0 and fila[2]>1000 and fila[1]<40):
			#Si cumple que empieza con "S", el precio es menor a 1000 y el MFR es menor a 40
			#Se inserta en la tabla el dato
			tabla.insert('', 'end', values =fila)


def Limpiar():
	tabla.delete(*tabla.get_children())


tabla = ttk.Treeview(frame1 , height=10)
tabla.grid(column=0, row=0, sticky='nsew')

ladox = Scrollbar(frame1, orient = HORIZONTAL, command= tabla.xview)
ladox.grid(column=0, row = 1, sticky='ew') 

ladoy = Scrollbar(frame1, orient =VERTICAL, command = tabla.yview)
ladoy.grid(column = 1, row = 0, sticky='ns')

tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)

estilo = ttk.Style(frame1)
estilo.theme_use('clam') #  ('clam', 'alt', 'default', 'classic')
estilo.configure(".",font= ('Arial', 14), foreground='red2')
estilo.configure("Treeview", font= ('Helvetica', 12), foreground='black',  background='white')
estilo.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

#Para los botones
boton2 = Button(frame2, text= 'Mostrar', bg='blue', command= datos_excel)
boton2.grid(column = 1, row = 0, sticky='nsew', padx=10, pady=10)

boton3 = Button(frame2, text= 'Limpiar', bg='red', command= Limpiar)
boton3.grid(column = 2, row = 0, sticky='nsew', padx=10, pady=10)


indica = Label(frame2, fg= 'white', bg='gray26', text= 'Ubicación del archivo', font= ('Arial',10,'bold') )
indica.grid(column=3, row = 0)

ventana.mainloop()



