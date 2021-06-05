'''
Created on Mar 4, 2021

@author: Bryan Valdez
'''

import tkinter as tk
from tkinter import messagebox as msg


ventana_principal = tk.Tk()
ventana_principal.title("Ventana Principal")
ventana_principal.geometry("400x400")

txtTitulo = tk.Label(ventana_principal, text="Calculadora sencilla")
txtTitulo.pack()

txtPrimerNumero = tk.Label(ventana_principal, text="Ingresa un numero").pack()
cajaPrimerNumero = tk.Entry(ventana_principal)
cajaPrimerNumero.pack()

txtSegundoNumero = tk.Label(ventana_principal, text="Ingresa otro numero").pack()
cajaSegundoNumero = tk.Entry(ventana_principal)
cajaSegundoNumero.pack()

txtResultado = tk.Label(ventana_principal, text="Resultado").pack()
cajaResultado = tk.Entry(ventana_principal)

def sumar():
    cajaResultado.delete(0, 'end')
    n1 = float(cajaPrimerNumero.get())
    n2 = float(cajaSegundoNumero.get())
    res = n1+n2
    cajaResultado.insert(0,res)
    #msg.showinfo("Resultado: ", n1)
def restar():
    cajaResultado.delete(0, 'end')
    n1 = float(cajaPrimerNumero.get())
    n2 = float(cajaSegundoNumero.get())
    res = n1-n2
    cajaResultado.insert(0,res)
def multiplicar():
    cajaResultado.delete(0, 'end')
    n1 = float(cajaPrimerNumero.get())
    n2 = float(cajaSegundoNumero.get())
    res = n1*n2
    cajaResultado.insert(0,res)
def dividir():
    cajaResultado.delete(0, 'end')
    n1 = float(cajaPrimerNumero.get())
    n2 = float(cajaSegundoNumero.get())
    res = n1/n2
    cajaResultado.insert(0,res)

btnSumar        = tk.Button(ventana_principal, text=" + ",width=10,command=sumar).pack(fill=tk.X)
btnRestar       = tk.Button(ventana_principal, text=" - ",width=10,command=restar).pack(side=tk.RIGHT)
btnMultiplicar  = tk.Button(ventana_principal, text=" x ",width=10,command=multiplicar).pack()
btnDividir      = tk.Button(ventana_principal, text=" / ",width=10,command=dividir).pack()


cajaResultado.pack()


ventana_principal.mainloop()