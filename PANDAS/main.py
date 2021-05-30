
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
import re
from io import open
import string
from tkinter import Tk, Label, Button, Frame,  messagebox, filedialog, ttk, Scrollbar, VERTICAL, HORIZONTAL

"""LA NETA NO SE PORQUE DA ALERTAS, PERO SI FUNCIONA XD..."""

def ventanaconsultas(a):
    ventanacon = Tk()
    ventanacon.title("PROGRAMA DE CONSULTAS")
    ventanacon.geometry("250x200")
    ventanacon.config(bg="blue")
            
    #Los botones pa las consultas
    btnIniciar = Button(ventanacon, text="CONSULTA 1",command=con1).place(x=20, y=10)
    btnIniciar = Button(ventanacon, text="CONSULTA 2",command=con2).place(x=20, y=50)
    btnIniciar = Button(ventanacon, text="CONSULTA 3",command=con3).place(x=20, y=90)
    btnIniciar = Button(ventanacon, text="CONSULTA 4",command=con4).place(x=20, y=130)
    btnIniciar = Button(ventanacon, text="CONSULTA 5",command=con5).place(x=20, y=170)
    btnIniciar = Button(ventanacon, text="CONSULTA 6",command=con6).place(x=150, y=10)
    btnIniciar = Button(ventanacon, text="CONSULTA 7",command=con7).place(x=150, y=50)
    btnIniciar = Button(ventanacon, text="CONSULTA 8",command=con8).place(x=150, y=90)
    btnIniciar = Button(ventanacon, text="CONSULTA 9",command=con9).place(x=150, y=130)
    btnIniciar = Button(ventanacon, text="CONSULTA 10",command=con10).place(x=150, y=170)
    


"""Una disculpa si no use herencia para las pruebas... pero no pude :'v """
def con1():
    import prueba

def con2():
    import prueba2
    
def con3():
    import prueba3

def con4():
    import prueba4

def con5():
    import prueba5

def con6():
    import prueba6

def con7():
    import prueba7

def con8():
    import prueba8

def con9():
    import prueba9

def con10():
    import prueba10

#----------------------------------------------UNICA Y EXCLUSIVAMENTE PARA EL INICIO Y REGISTRO-------------------------------------------------------------------------------------------------
#LIsta para el cifrado cesar xd
alfabeto = list(string.ascii_lowercase.upper())
alfabeto2 = list(string.ascii_lowercase)
numeros=["0","1","2","3","4","5","6","7","8","9","0"]
alfabeto+=numeros+alfabeto2

        
def ventana_inicio():
    global ventana2
    ventana2=Tk()
    ventana2.geometry("300x250")
    ventana2.config(bg="pink")
    ventana2.title("Bienvenidaaaaa")
    Label(text="Escoja su opción", bg="pink", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Acceder", height="2", width="30", bg="plum", command=login).pack()
    Label(text="").pack()
    Button(text="Registrarse", height="2", width="30", bg="plum", command=registro2).pack()
    Label(text="").pack()
    ventana2.mainloop()

def registro2():
    global registro2
    registro2= Toplevel(ventana2)
    registro2.title("Registro de Usuario")
    registro2.geometry("300x250")
    global nombre_usuario
    global clave
    global entrada_nombre
    global entrada_clave
    nombre_usuario = StringVar()
    clave = StringVar()
    Label(registro2, text="Introduzca datos", bg="pink").pack()
    Label(registro2, text="").pack()
    etiqueta_nombre = Label(registro2, text="Nombre de usuario * ")
    etiqueta_nombre.pack()
    entrada_nombre = Entry(registro2, textvariable=nombre_usuario)
    entrada_nombre.pack()
    etiqueta_clave = Label(registro2, text="Contraseña * ")
    etiqueta_clave.pack()
    entrada_clave = Entry(registro2, textvariable=clave, show='*')
    entrada_clave.pack()
    Label(registro2, text="").pack()
    Button(registro2, text="Registrarse", width=10, height=1, bg="Pink", command = registro_usuario).pack()
#VENTANA PARA LOGIN.

def login():
    global ventana_login
    ventana_login = Toplevel(ventana2)
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("300x250")
    Label(ventana_login, text="Introduzca nombre de usuario y contraseña").pack()
    Label(ventana_login, text="").pack()
    global verifica_usuario
    global verifica_clave
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
    global entrada_login_usuario
    global entrada_login_clave
    Label(ventana_login, text="Nombre usuario * ").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_login, text="").pack()
    Label(ventana_login, text="Contraseña * ").pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*')
    entrada_login_clave.pack()
    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Acceder", width=10, height=1, command =ingresar).pack()
    #verifica_login

def  registro_usuario():
    #Lo del Cesar xdddddddddddddddddddd
    usuariox=nombre_usuario.get()
    clavex=clave.get()
    if usuariox=="" or clavex=="":
        MessageBox.showinfo("ERROR", "Ingresa datosxd?")

    else: 
        username_info=""
        n=2
        for letra in usuariox:
            suma=alfabeto.index(letra)+n
            mod=int(suma)%len(alfabeto)
            username_info=username_info+str(alfabeto[mod])  
        print(username_info,"\t", clavex)

    file = open("user.txt", "a")
    file2=open("contraseñas.txt","a")
    file.write(username_info)
    file.write("\n")
    file.close()
    file2.write(clavex)
    file2.write("\n")
    file2.close()
 
    entrada_nombre.delete(0, END)
    entrada_clave.delete(0, END)
            
inicia_sesion1=0
inicia_sesion2=0
posicion1=0
posicion2=1
lista_usuarios=[]
lista_contrasenas=[]



usuarios='user.txt'
with open(usuarios) as obj1:

    for line in obj1:
        texto=line.rstrip('\n')
        textocifrado=""
        for letra in texto:
            suma=alfabeto.index(letra)-2 
            mod=int(suma)%len(alfabeto)
            textocifrado=textocifrado+str(alfabeto[mod])
            if(len(textocifrado)==len(texto)):
                lista_usuarios.append(textocifrado)


contraseñas="contraseñas.txt"          
with open(contraseñas) as obj2:
    for line in obj2:
        line=line.rstrip('\n')
        lista_contrasenas.append(line)
        
print(lista_usuarios)
print(lista_contrasenas)




def datos():
    user2=verifica_usuario.get()
    return user2

def datos2():
    pas2=verifica_clave.get()
    return pas2



def validarcontrasena1():    
    for usuario in lista_usuarios:
        if datos()==usuario:
            inicia_sesion1=1
            return inicia_sesion1

        
        
def validarcontrasena2():
    for contraseña in lista_contrasenas:
        if datos2()==contraseña:
            inicia_sesion2=1
            return inicia_sesion2 
        
        
def posicion1():
    posicion1=lista_usuarios.index(datos())
    return posicion1

def posicion2():
    posicion2=lista_contrasenas.index(datos2()) 
    return posicion2


def posiciones():
    if(posicion1()==posicion2()):
        return True
    else:
        return False
    
    
def ingresar():

    if validarcontrasena1()==1 and validarcontrasena2()==1 and posiciones()==True:
        MessageBox.showinfo("Holaa", "Bienvenido, amigue")
        borrar_exito_login()
        #Llamamos a la ventana xd
        ventanaconsultas(1)

    else:
        MessageBox.showinfo("¿Quien eres?", "Te conozco?")
    
#cerrar las ventanas
def borrar_exito_login():
    ventana2.destroy()
    
def borrar_no_clave():
    ventana_no_clave.destroy()
def borrar_no_usuario():
    ventana_no_usuario.destroy()
    
ventana_inicio()

