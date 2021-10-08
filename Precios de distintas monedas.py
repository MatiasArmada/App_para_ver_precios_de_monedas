from tkinter import *
from tkinter import ttk, font
import tkinter as tk
import requests
from datetime import datetime
class Aplicacion(tk.Tk):
    __ventana=None

    def __init__(self):
        super().__init__()
        
        label_a = tk.Label(self, text="Moneda", bg="Green", fg="White")
        label_b = tk.Label(self, text="Compra \t\t Venta", bg="Green", fg="White")

        opts = { 'ipadx': 10, 'ipady': 10 , 'sticky': 'nswe' }
        optsM = { 'ipadx': 0.5, 'ipady': 0.5 , 'sticky': 'nswe' }
        label_a.grid(row=0, column=0, **opts)
        label_b.grid(row=0, column=1,  **opts)
        
        
        complete_url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
        r = requests.get(complete_url)
        dic= r.json()
        print(dic)
        print(len(dic))
        
        compra=dic[7]['casa']['compra']
        venta=dic[7]['casa']['venta']
        nombre=dic[7]['casa']['nombre']
        nombredolar3 = tk.Label(self, text=f"{nombre}", bg="Lightgreen")
        nombredolar3.grid(row=1, column=0,  **opts)
        compraventa3= tk.Label(self, text=f"  {compra} \t {venta}", bg="Lightgreen")
        compraventa3.grid(row=1, column=1, **opts)
        barraverde3 = tk.Label(self, bg="Green")
        barraverde3.grid(row=2, column=0,**optsM, columnspan=2)
        
        
        compra=dic[1]['casa']['compra']
        venta=dic[1]['casa']['venta']
        nombre=dic[1]['casa']['nombre']
        nombredolar1 = tk.Label(self, text=f"{nombre}", bg="Lightgreen")
        nombredolar1.grid(row=3, column=0,  **opts)
        compraventa1= tk.Label(self, text=f"  {compra} \t {venta}", bg="Lightgreen")
        compraventa1.grid(row=3, column=1, **opts)
        barraverde1 = tk.Label(self, bg="Green")
        barraverde1.grid(row=4, column=0,**optsM, columnspan=2)
        
        compra=dic[3]['casa']['compra']
        venta=dic[3]['casa']['venta']
        nombre=dic[3]['casa']['nombre']
        nombredolar2 = tk.Label(self, text=f"{nombre}", bg="Lightgreen")
        nombredolar2.grid(row=5, column=0,  **opts)
        compraventa2= tk.Label(self, text=f"  {compra} \t {venta}", bg="Lightgreen")
        compraventa2.grid(row=5, column=1, **opts)
        barraverde2 = tk.Label(self, bg="Green")
        barraverde2.grid(row=6, column=0,**optsM, columnspan=2)
        
        compra=dic[4]['casa']['compra']
        venta=dic[4]['casa']['venta']
        nombre=dic[4]['casa']['nombre']
        nombredolar2 = tk.Label(self, text=f"{nombre}", bg="Lightgreen")
        nombredolar2.grid(row=7, column=0,  **opts)
        compraventa2= tk.Label(self, text=f"  {compra} \t {venta}", bg="Lightgreen")
        compraventa2.grid(row=7, column=1, **opts)
        barraverde2 = tk.Label(self, bg="Green")
        barraverde2.grid(row=8, column=0,**optsM, columnspan=2)
        
        compra=dic[0]['casa']['compra']
        venta=dic[0]['casa']['venta']
        nombre=dic[0]['casa']['nombre']
        label_c = tk.Label(self, text=f"{nombre}", bg="Lightgreen")
        label_c.grid(row=9, column=0, **opts)
        compraventa0= tk.Label(self, text=f"  {compra} \t\t {venta}", bg="Lightgreen")
        compraventa0.grid(row=9, column=1,  **opts)
        label_d = tk.Label(self, bg="Green")
        label_d.grid(row=10, column=0,**optsM, columnspan=2)
        fondo=tk.Label(self, bg="Lightgreen")
        fondo.grid(row=11, column=0,**optsM, columnspan=2)
        boton1 = tk.Button(self, text="Actualizar", fg='white', bg='green', command=self.actualizar,width=18, height=1)
        boton1.grid(column=0, row=11, ipadx= 0.5, ipady= 0.5)
        fecha=datetime.now()
        
        
        label_actualizar = tk.Label(self, text=f"Actualizado {fecha.day}/{fecha.month}/{fecha.year} {fecha.hour}:{fecha.minute}", bg="Lightgreen")
        label_actualizar.grid(column=1, row=11,**opts)
    def actualizar(self):
        label_a = tk.Label(self, text="Moneda", bg="Green", fg="White")
        label_b = tk.Label(self, text="Compra \t\t Venta", bg="Green", fg="White")

        opts = { 'ipadx': 10, 'ipady': 10 , 'sticky': 'nswe' }
        optsM = { 'ipadx': 0.5, 'ipady': 0.5 , 'sticky': 'nswe' }
        label_a.grid(row=0, column=0, **opts)
        label_b.grid(row=0, column=1,  **opts)
        
        
        complete_url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
        r = requests.get(complete_url)
        dic= r.json()
        print(dic)
        print(len(dic))
        
        compra=dic[7]['casa']['compra']
        venta=dic[7]['casa']['venta']
        nombre=dic[7]['casa']['nombre']
        nombredolar3 = tk.Label(self, text=f"{nombre}", bg="Lightgreen")
        nombredolar3.grid(row=1, column=0,  **opts)
        compraventa3= tk.Label(self, text=f"  {compra} \t {venta}", bg="Lightgreen")
        compraventa3.grid(row=1, column=1, **opts)
        barraverde3 = tk.Label(self, bg="Green")
        barraverde3.grid(row=2, column=0,**optsM, columnspan=2)
        
        
        compra=dic[1]['casa']['compra']
        venta=dic[1]['casa']['venta']
        nombre=dic[1]['casa']['nombre']
        nombredolar1 = tk.Label(self, text=f"{nombre}", bg="Lightgreen")
        nombredolar1.grid(row=3, column=0,  **opts)
        compraventa1= tk.Label(self, text=f"  {compra} \t {venta}", bg="Lightgreen")
        compraventa1.grid(row=3, column=1, **opts)
        barraverde1 = tk.Label(self, bg="Green")
        barraverde1.grid(row=4, column=0,**optsM, columnspan=2)
        
        compra=dic[3]['casa']['compra']
        venta=dic[3]['casa']['venta']
        nombre=dic[3]['casa']['nombre']
        nombredolar2 = tk.Label(self, text=f"{nombre}", bg="Lightgreen")
        nombredolar2.grid(row=5, column=0,  **opts)
        compraventa2= tk.Label(self, text=f"  {compra} \t {venta}", bg="Lightgreen")
        compraventa2.grid(row=5, column=1, **opts)
        barraverde2 = tk.Label(self, bg="Green")
        barraverde2.grid(row=6, column=0,**optsM, columnspan=2)
        
        compra=dic[4]['casa']['compra']
        venta=dic[4]['casa']['venta']
        nombre=dic[4]['casa']['nombre']
        nombredolar2 = tk.Label(self, text=f"{nombre}", bg="Lightgreen")
        nombredolar2.grid(row=7, column=0,  **opts)
        compraventa2= tk.Label(self, text=f"  {compra} \t {venta}", bg="Lightgreen")
        compraventa2.grid(row=7, column=1, **opts)
        barraverde2 = tk.Label(self, bg="Green")
        barraverde2.grid(row=8, column=0,**optsM, columnspan=2)
        
        compra=dic[0]['casa']['compra']
        venta=dic[0]['casa']['venta']
        nombre=dic[0]['casa']['nombre']
        label_c = tk.Label(self, text=f"{nombre}", bg="Lightgreen")
        label_c.grid(row=9, column=0, **opts)
        compraventa0= tk.Label(self, text=f"  {compra} \t\t {venta}", bg="Lightgreen")
        compraventa0.grid(row=9, column=1,  **opts)
        label_d = tk.Label(self, bg="Green")
        label_d.grid(row=10, column=0,**optsM, columnspan=2)
        fondo=tk.Label(self, bg="Lightgreen")
        fondo.grid(row=11, column=0,**optsM, columnspan=2)
        boton1 = tk.Button(self, text="Actualizar",command=self.actualizar, fg='white', bg='green', width=18, height=1)
        boton1.grid(column=0, row=11, ipadx= 0.5, ipady= 0.5)
        fecha=datetime.now()
        
        
        label_actualizar = tk.Label(self, text=f"Actualizado {fecha.day}/{fecha.month}/{fecha.year} {fecha.hour}:{fecha.minute}", bg="Lightgreen")
        label_actualizar.grid(column=1, row=11,**opts)
        

        
        
if __name__=='__main__':
    app = Aplicacion()
    app.mainloop()