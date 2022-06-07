#import directories
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from PIL import ImageTk,Image
import diffusionprofile as dp
import pandas as pd

def printDeffVal():
    temp = float(e_1.get())
    dab = dp.Deff(temp)
    deffText.set(f'{dab:.4f} cm^2/s')

root = Tk()
root.geometry("300x300")


labelText=StringVar()
labelText.set("Temperature (K): ")
labelDir=Label(root, textvariable=labelText)
labelDir.place(x=0,y=0)

e_1 = Entry(root, width=8, bg="white", fg="black", textvariable='0')
e_1.place(x=100,y=0)


but_1 = Button(root, text="Get D_ab", command=printDeffVal)
but_1.place(x=0,y=20)

deffText = StringVar()
deffText.set("0.0000 cm^2/s")
labelDeff = Label(root, textvariable=deffText)
labelDeff.place(x=42,y=60)

deffLab = Label(root, text='D_eff =')
deffLab.place(x=0,y=60)

root.mainloop()

