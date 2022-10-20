
import tkinter
from PIL import Image, ImageTk
from PIL import Image 
from cProfile import label
import tkinter as tk
from tkinter import *
from tokenize import Double
from tkinter import PhotoImage, Tk, Button, Label, IntVar
from PIL import Image as imim


ventana = Tk()
ventana.geometry("600x680")
ventana.title("Cafeteria")
ventana.configure(bg="salmon")

#Se crean los Label para las imagenes 
label1 =Label(ventana, image="")
label2 =Label(ventana, image="")
label3 =Label(ventana, image="")
label4 =Label(ventana, image="")
label5 =Label(ventana, image="")
label6 =Label(ventana, image="")
label7 =Label(ventana, image="")
label8 =Label(ventana, image="")
label9 =Label(ventana, image="")


#Se crean label para las letras 
cafe = tkinter.Label(ventana, text = "Friend's Coffe")
cafe.place(x=250, y=0)
ensa = tkinter.Label(ventana, text = "Ensaladas")
ensa.place(x=40, y=190)
bebi = tkinter.Label(ventana, text = "Bebidas")
bebi.place(x=40, y=400)


#Se suben las imagenes
imagen1 = imim.open(r"C:\Users\ftaya\Desktop\Parcial Program\carne.png")
imagenrezis1 = imagen1.resize((80,100),imim.Resampling.LANCZOS)
render1 =ImageTk.PhotoImage(imagenrezis1)
label1.configure(image=render1)
label1.image_names =render1
label1.place(x=70, y=30)

imagen2 = imim.open(r"C:\Users\ftaya\Desktop\Parcial Program\pollo.png")
imagenrezis2 = imagen2.resize((80,100),imim.Resampling.LANCZOS)
render2 =ImageTk.PhotoImage(imagenrezis2)
label2.configure(image=render2)
label2.image_names =render2
label2.place(x=220, y=30)

imagen3 = imim.open(r"C:\Users\ftaya\Desktop\Parcial Program\Lasagna.png")
imagenrezis3 = imagen3.resize((80,100),imim.Resampling.LANCZOS)
render3 =ImageTk.PhotoImage(imagenrezis3)
label3.configure(image=render3)
label3.image_names =render3
label3.place(x=390, y=30)

imagen4 = imim.open(r"C:\Users\ftaya\Desktop\Parcial Program\ensalada.png")
imagenrezis4 = imagen4.resize((80,100),imim.Resampling.LANCZOS)
render4 =ImageTk.PhotoImage(imagenrezis4)
label4.configure(image=render4)
label4.image_names =render4
label4.place(x=70, y=220)

imagen5 = imim.open(r"C:\Users\ftaya\Desktop\Parcial Program\coditoss.png")
imagenrezis5 = imagen5.resize((100,100),imim.Resampling.LANCZOS)
render5 =ImageTk.PhotoImage(imagenrezis5)
label5.configure(image=render5)
label5.image_names =render5
label5.place(x=220, y=220)

imagen6 = imim.open(r"C:\Users\ftaya\Desktop\Parcial Program\rusa.png")
imagenrezis6 = imagen6.resize((100,100),imim.Resampling.LANCZOS)
render6 =ImageTk.PhotoImage(imagenrezis6)
label6.configure(image=render6)
label6.image_names =render6
label6.place(x=390, y=220)

imagen7 = imim.open(r"C:\Users\ftaya\Desktop\Parcial Program\gaseosa.png")
imagenrezis7 = imagen7.resize((100,100),imim.Resampling.LANCZOS)
render7 =ImageTk.PhotoImage(imagenrezis7)
label7.configure(image=render7)
label7.image_names =render7
label7.place(x=70, y=430)

imagen8 = imim.open(r"C:\Users\ftaya\Desktop\Parcial Program\jugos.png")
imagenrezis8 = imagen8.resize((100,100),imim.Resampling.LANCZOS)
render8 =ImageTk.PhotoImage(imagenrezis8)
label8.configure(image=render8)
label8.image_names =render8
label8.place(x=220, y=430)

imagen9 = imim.open(r"C:\Users\ftaya\Desktop\Parcial Program\cafe.png")
imagenrezis9 = imagen9.resize((100,100),imim.Resampling.LANCZOS)
render9 =ImageTk.PhotoImage(imagenrezis9)
label9.configure(image=render9)
label9.image_names =render9
label9.place(x=390, y=430)

platillo = IntVar()
ensaladas = IntVar()
bebida = IntVar()



#Se crea las funciones que haran que funciones los RadioButtons
def Platofuerte():
    global precomi
    global eleccion
    pla=platillo.get()

    if pla==1:
        precomi=2.50 
        eleccion = "Carne Asada"
    elif pla==2:
        precomi=2.25 
        eleccion = "Pollo Guisado"
    elif pla==3:
        precomi=3.00
        eleccion = "Lazaña"
    else :
        precomi=0
       

def ensalada():
    global tipo
    global ensala
    ens=ensaladas.get()
    if ens==4:
        ensala=0.25
        tipo="Fresca"
    elif ens==5:
        ensala=0.25
        tipo="Coditos"
    elif ens==6:
        ensala=0.25
        tipo="Rusa"
    else :
        ensala=0
       

def bebidas():
    global tipob
    global bebid
    bebid=bebida.get()
    if bebid==7:
        bebid=0.75
        tipob="Gaseosa"
    elif bebid==8:
        bebid=0.50
        tipob="Refresco"
    elif bebid==9:
        bebid=0.65
        tipob="Cafe"
    else :
        bebid=0
        

def total():
    total= precomi + ensala + bebid

    print("Producto          Precio" )
    print(eleccion,"      ","-","  ","$",precomi)
    print(tipo,"      ","-","      ","$",ensala)
    print(tipob,"      ","-","     ","$",bebid)
    print("total                   ","$",total)

#Se crean los radiobutton para las opciones
radiobtn1 = tk.Radiobutton(ventana, text="Carne Asada", value=1, command= Platofuerte, variable=platillo)
radiobtn2 = tk.Radiobutton(ventana, text="Pollo Guisado", value=2, command= Platofuerte, variable=platillo)
radiobtn3 = tk.Radiobutton(ventana, text="Lasaña", value=3, command= Platofuerte, variable=platillo)
radiobtn4 = tk.Radiobutton(ventana, text="Fresca", value=4, command= ensalada, variable=ensaladas)
radiobtn5 = tk.Radiobutton(ventana, text="Coditos", value=5, command= ensalada, variable=ensaladas)
radiobtn6 = tk.Radiobutton(ventana, text="Rusa", value=6,command= ensalada, variable=ensaladas)
radiobtn7 = tk.Radiobutton(ventana, text="Gaseosa", value=7, command= bebidas, variable=bebida)
radiobtn8 = tk.Radiobutton(ventana, text="Refresco", value=8, command= bebidas, variable=bebida)
radiobtn9 = tk.Radiobutton(ventana, text="Cafe", value=9, command=bebidas, variable=bebida)
radiobtn1.place(x=70, y=150)
radiobtn2.place(x=220, y=150)
radiobtn3.place(x=390, y=150)
radiobtn4.place(x=70, y=350)
radiobtn5.place(x=220, y=350)
radiobtn6.place(x=390, y=350)
radiobtn7.place(x=70, y=550)
radiobtn8.place(x=220, y=550)
radiobtn9.place(x=390, y=550)



#Se crea un boton para enviar a la Factura
btn1 =Button(ventana, text="IMPRIMIR FACTURA", command= total)
btn1.configure(bg="thistle")
btn1.place(x=450, y=610)


ventana.mainloop()
