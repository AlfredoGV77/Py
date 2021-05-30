
from Persona import Persona
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
import re
from io import open
import string



class Registro:
    def __init__(self, master):
        self.master = master
        master.title("Registro Profesores y Alumnos con herencia")
        master.geometry('800x573')
        #el titulo y su estilo
        self.titulo = Label()
        self.titulo.pack(anchor = CENTER)
        self.titulo.config(text="REGISTRO PROFESOR Y ALUMNO", fg = "white", bg = "deep pink",font = ("Arial", 25))
        #el css de las instrucciones y pues rosita todo por que se ve bonitoo
        self.ins = Label()
        self.ins.pack(anchor = CENTER)
        self.ins.config(text="Por fa, presione un boton para proseguir con el registro de un alumno o un profesor", fg = "white", bg = "deep pink",font = (" Fantasque Sans Mono", 15))

        self.estu = Button(master, text = "Alumnno", command = self.ac_es)
        self.estu.place(x= 580, y = 90, width = 140, height = 60)
        self.estu.config(fg = "white", font = ("Verdana", 17), bg ="deep pink")

        self.pro = Button(master, text = "Profesor", command = self.ac_pr)
        self.pro.place(x = 70, y = 90, width= 140, height=60)
        self.pro.config(fg = "white", font = ("Verdana", 17), bg ="deep pink")
        #Dejo esto aquí por que no sé por que me marca error si lo quiero poner con los otros ):, atyuda
        self.nombre = Label()
        self.nombre.place(x = 90, y= 200)
        self.nombre.config(text = "Nombre:", fg = "white", bg = "deep pink",font = ("Verdana", 17))
        #Y este otro es para que guarde o "registre" los datos
        self.reg = Button(master, text="Registrar", command=self.ac_re)
        self.reg.place(x=70, y = 430, width= 160, height=72)
        self.reg.config(fg = "white", font = ("Verdana", 17), bg ="deep pink")
        #Esto es para consultar los datos que metiste en los campos, los de un profesor o alumno
        self.cam = Button(master, text = "Consulta", command = self.ac_co)
        self.cam.place(x = 580, y=430, width = 160, height = 72)
        self.cam.config(fg = "white", font = ("Verdana", 17), bg ="deep pink")
        #declaracion de variables para etiquetas
        self.uno = StringVar()
        self.uno.set("Boleta: ")
        
        self.dos = StringVar()
        self.dos.set("Grupo: ")

        self.tres = StringVar()
        self.tres.set("Edad: ")

        #esto para el diseño de los botones de datos 
        self.boleta = Label()
        self.boleta.place(x = 90, y= 250)
        self.boleta.config(textvariable = self.uno, fg = "white", bg = "deep pink",font = ("Verdana", 17))

        self.grupo = Label()
        self.grupo.place(x = 90, y = 300)
        self.grupo.config(textvariable = self.dos, fg = "white", bg = "deep pink",font = ("Verdana", 17))

        self.edad = Label()
        self.edad.place(x=90, y=350)
        self.edad.config(textvariable = self.tres, fg = "white", bg = "deep pink",font = ("Verdana", 17))
        #hay que declarar variables 
        self.n = StringVar()
        self.b = StringVar()
        self.g = StringVar()
        self.e = StringVar()

        self.primero = Entry(textvariable = self.n)
        self.primero.place(x= 520, y = 200, width = 250, height = 30)

        self.segundo = Entry(textvariable = self.b)
        self.segundo.place(x = 520, y = 250, width = 250, height = 30)

        self.tercero = Entry(textvariable = self.g)
        self.tercero.place(x = 520, y = 300, width = 250, height = 30)

        self.cuarto = Entry(textvariable = self.e)
        self.cuarto.place(x=520, y = 350, width=250, height=30)

        #Estas son las variables de control para los botonesxd
        self.Un = True
        self.Do = False
    def ac_es(self):
        self.uno.set("Boleta: "); self.dos.set("Grupo"); self.tres.set("Edad")
        self.Un = True
        self.Do = False
    def ac_pr(self):
        self.uno.set("Materia: "); self.dos.set("Grupos"); self.tres.set("Horas")
        self.Un = False
        self.Do = True
    def ac_re(self):
        self.vari =self.n.get()
        self.va = self.b.get()
        self.v = self.g.get()
        self.u = self.e.get()
        patron1 = re.compile(r'\D{3,30}')
        patron2 = re.compile(r'\d{1,3}')
        patron3 = re.compile(r'\w{4,15}')
        
        self.numero = 0
        if(patron1.match(self.vari)):
            self.numero += 1
        else:
            MessageBox.showinfo("Uy, advertencia ):", "Ingrese un nombre válido, porfa")
            self.numero=0
        if(patron3.match(self.va)):
            self.numero += 1
        else:
            MessageBox.showinfo("Uy, advertencia ):", "Ingrese un dato válido en el campo 2, porfa")
            self.numero=0
        if(patron3.match(self.v)):
            self.numero +=1
        else:
            MessageBox.showinfo("Uy,advertencia ):", "Ingrese un grupo válido, porfa ")
            self.numero=0
        if(patron2.match(self.u)):
            self.numero +=1
        else:
            MessageBox.showinfo("Uy, advertencia ):", "Ingrese un dato válido en el campo 4, porfa")
            self.numero=0

        if(self.numero == 4):
            if(self.Un == True):
                self.guard = Persona(self.vari, self.va, self.v, self.u)
                self.guard.guarEstu()
            if(self.Do == True):
                self.guard2 = Persona(self.vari, self.va, self.v, self.u)
                self.guard2.guarProf()
        
    def ac_co(self):
        self.mostrar = Toplevel()
        self.mostrar.geometry('500x500')
        self.mostrar.configure(background = "#ff7c7c")
        self.mostrar.etiqueta = Label(self.mostrar)
        self.mostrar.etiqueta.place(x = 20, y = 20)
        self.mostrar.etiqueta.config(text = "Alumnos (arriba) y Profesores (abajo)", fg = "black", bg = "#ff7c7c",font = ("Verdana", 17))
        
        self.etiq = Label(self.mostrar)
        self.etiq.place(x=10, y = 250)
        self.etiq.config(text = "Profesores", fg = "black", bg = "#ff7c7c",font = ("Verdana", 17))

        self.le = Text(self.mostrar)
        self.le.place(x=10, y = 60)
        self.le.config(fg = "black", bg = "#ff7c7c",font = ("Verdana", 17))

        fichero = open("file.txt", 'r+')
        contenido = fichero.read()
        self.le.delete(1.0,'end')
        self.le.insert('insert', contenido)
        fichero.close()

        self.le2 = Text(self.mostrar)
        self.le2.place(x=10, y = 320)
        self.le2.config(fg = "black", bg = "#ff7c7c", font = ("Verdana", 17))
        
        fichero2 = open("file2.txt", 'r+')
        contenido2 = fichero2.read()
        self.le2.delete(1.0,'end')
        self.le2.insert('insert', contenido2)
        fichero2.close()

        self.mostrar.resizable(False, False)
 
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
        root = Tk()
        root.resizable(width=False, height=False)
        root.configure(background = "#ba55d3")
        miVentana = Registro(root)
        root.mainloop()
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

