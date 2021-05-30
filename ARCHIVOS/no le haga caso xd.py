from tkinter import *
import string 
from tkinter import messagebox as MessageBox


alfabeto = list(string.ascii_lowercase.upper())
alfabeto2 = list(string.ascii_lowercase)
numeros=["0","1","2","3","4","5","6","7","8","9","0"]
alfabeto+=numeros+ alfabeto2


def send_data():
  user = username.get().upper()
  password_info = password.get()
  
  if user=="" or password_info=="":
        MessageBox.showinfo("ERROR", "Ingresa datosxd?")
  else:
    username_info=""
    n=2
    for letra in user:
      suma=alfabeto.index(letra)+n
      mod=int(suma)%len(alfabeto)
      username_info=username_info+str(alfabeto[mod])  
    print(username_info,"\t", password_info)
  

  file = open("user.txt", "a")
  file2=open("contraseñas.txt","a")
  file.write(username_info)
  file.write("\n")
  file.close()
  file2.write(password_info)
  file2.write("\n")
  file2.close()
 
  username_entry.delete(0, END)
  password_entry.delete(0, END)


mywindow = Tk()
mywindow.geometry("250x280")
mywindow.title("Registroxd")
mywindow.resizable(False,False)
mywindow.config(background = "#ff1493")
main_title = Label(text = "Registro", font = ("Cambria", 14), bg = "#ba55d3", fg = "white", width = "500", height = "2")
main_title.pack()


username_label = Label(text = "Nombre(Solo letras y sin espacios)", bg = "#ba55d3", fg="white")
username_label.place(x = 22, y = 70)
password_label = Label(text = "Password", bg = "#ba55d3", fg="white")
password_label.place(x = 22, y = 130)


 

username = StringVar()
password = StringVar()
fullname = StringVar()
age = StringVar()
 
username_entry = Entry(textvariable = username, width = "40")
password_entry = Entry(textvariable = password, width = "40",  show = "*")

 
username_entry.place(x = 22, y = 100)
password_entry.place(x = 22, y = 160)
 

submit_btn = Button(mywindow,text = "Registrar", width = "30", height = "2", command = send_data, bg = "#9370db", fg="white")
submit_btn.place(x = 22, y = 200)

def regreso():
    import iniciarsesion
    

reg=Button(mywindow,text="Regresar",width="30", height="2", command=regreso ,bg = "#9370db", fg="white")
reg.place(x=22, y=250)

mywindow.mainloop()