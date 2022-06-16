#import directories
from calendar import c
from urllib.parse import _NetlocResultMixinStr
import numpy as np
import matplotlib as mpl
from tkinter import *
from PIL import ImageTk,Image
import diffusionprofile as dp
import consumption as cons
import pandas as pd
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

def printDeffVal():

    if e_temper.get() == '':
        deffText.set("Error: Input a number")
        raise ValueError("Invalid input")

    temp = float(e_temper.get())
    dab = dp.Deff(temp)
    deffText.set(f'{dab:.4f} cm^2/s')
    return None

globalHold = np.zeros(3)


def plantZ():

    if ((e_ac.get() or e_cin.get() or e_area.get() or e_height.get() or e_con.get()) == ''):
        plerrorText.set('Please fill in all fields')
        raise ValueError("Invalid input")

    Cin = float(e_cin.get())
    area = float(e_area.get())
    height = float(e_height.get())
    intake = float(e_con.get())
    airchanges = float(e_ac.get())

    plantParams = cons.C_plants(Cin, area, height, airchanges, intake)
    cplText.set(f'{plantParams[0]:.4f} ppm')
    volText.set(f'{plantParams[1]:.4f} m^3')
    velText.set(f'{plantParams[2]:.4f} m/s')
    for i in range(0,3):
        globalHold[i] = plantParams[i]
    plerrorText.set('')
    return None

def plot():
    fig = mpl.figure.Figure(figsize=(5,4))
    Cplant = float(e_plh.get())
    Cins = float(e_cin.get())
    ht = float(e_height.get())
    xs1 = np.linspace(0,Cplant,int(Cplant*100+1))
    ys1 = np.linspace(Cins, globalHold[0], (len(xs1)))
    
    xs2 = np.linspace(Cplant+0.001, ht, 100)
    ys2 = np.linspace(globalHold[0]-0.001, 440, 100)

    xs = np.append(xs1,xs2)
    ys = np.append(ys1,ys2)
    plot1 = fig.add_subplot(111)
    plot1.plot(xs,ys)
    plot1.set_xlabel('Height (m)')
    plot1.set_ylabel('ppm CO2')
    plot1.set_title('Stationary Media Approximation')
    
    canvas = FigureCanvasTkAgg(fig, master = root)
    canvas.draw()
    canvas.get_tk_widget().place(x=250,y=40)
    return None

#init
root = Tk()
root.geometry("800x550")

#temp label
tempText=StringVar()
tempText.set("Temperature (K): ")
labelTemp=Label(root, textvariable=tempText)
labelTemp.place(x=0,y=0)

#temp entry
e_temper = Entry(root, width=8, bg="white", fg="black")
e_temper.place(x=100,y=0)

#deff button
but_Deff = Button(root, text="Get D_ab", command=printDeffVal)
but_Deff.place(x=0,y=20)

#deff output
deffText = StringVar()
deffText.set("0.0000 cm^2/s")
labelDeff = Label(root, textvariable=deffText)
labelDeff.place(x=42,y=60)

#deff text label
deffLab = Label(root, text='D_eff =')
deffLab.place(x=0,y=60)

#plant button
but_2 = Button(root, text="Calculate Plant-zone parameters", command=plantZ)
but_2.place(x=0, y=250)

#plant height entry
e_plh = Entry(root, width=5, bg="white", fg="black")
e_plh.place(x=100,y=120)

#plant height label
plhText=StringVar()
plhText.set("Plants (m): ")
labelPlh=Label(root, textvariable=plhText)
labelPlh.place(x=0,y=120)

#area entry
e_area = Entry(root, width=5, bg="white", fg="black")
e_area.place(x=100,y=140)

#area label
areaText=StringVar()
areaText.set("Area (m^2): ")
labelArea=Label(root, textvariable=areaText)
labelArea.place(x=0,y=140)

#height entry
e_height = Entry(root, width=5, bg="white", fg="black")
e_height.place(x=100,y=160)

#height label
heiText=StringVar()
heiText.set("Height (m): ")
labelHei=Label(root, textvariable=heiText)
labelHei.place(x=0,y=160)

#airchanges entry
e_ac = Entry(root, width=5, bg="white", fg="black")
e_ac.place(x=100,y=180)

#airchanges label
acText=StringVar()
acText.set("Air Changes/hr: ")
labelac=Label(root, textvariable=acText)
labelac.place(x=0,y=180)

#consumption entry
e_con = Entry(root, width=5, bg="white", fg="black")
e_con.place(x=100,y=200)

#consumption label
consText=StringVar()
consText.set("Cons (g/m2-hr): ")
labelCons=Label(root, textvariable=consText)
labelCons.place(x=0,y=200)

#concentration entry
e_cin = Entry(root, width=5, bg="white", fg="black")
e_cin.place(x=100,y=220)

#concentration label
cinsText=StringVar()
cinsText.set("Inlet Con (ppm): ")
labelCins=Label(root, textvariable=cinsText)
labelCins.place(x=0,y=220)

#vol output
volText = StringVar()
volText.set("0.0000 m^3")
labelVol= Label(root, textvariable=volText)
labelVol.place(x=60,y=280)

#vol text label
volLab = Label(root, text='Vol =')
volLab.place(x=0,y=280)

#Cplant output
cplText = StringVar()
cplText.set("0.0000 ppm")
labelCpl= Label(root, textvariable=cplText)
labelCpl.place(x=60,y=300)

#Cplant label
cplLab = Label(root, text='C_plant =')
cplLab.place(x=0,y=300)

#velocity output
velText = StringVar()
velText.set("0.0000 m/s")
labelVel= Label(root, textvariable=velText)
labelVel.place(x=60,y=320)

#velocitylabel
velLab = Label(root, text='Velocity =')
velLab.place(x=0,y=320)

#plant param error label

plerrorText = StringVar()
plerrorText.set('')
labelPLError = Label(root, textvariable=plerrorText)
labelPLError.place(x=0,y=340)
#graph button
but_Graph = Button(root, text="Stn Media Approx", command=plot)
but_Graph.place(x=200,y=20)

root.mainloop()

