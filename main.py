#import directories
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from PIL import ImageTk,Image

'''
num = np.exp(3)
print(num)
xs = np.linspace(0,100,101)
ys = xs**2
plt.plot(xs,ys)
plt.show()
'''

def graph():
    price = np.random.normal(200000, 25000,1000)
    plt.hist(price, 20)
    plt.show()

def recalVals():
    return 0


root = Tk()
root.geometry("600x600")


labelText=StringVar()
labelText.set("Temperature (K): ")
labelDir=Label(root, textvariable=labelText,heigh=4)
labelDir.pack(side="left")

e1 = Entry(root, width=8, bg="white", fg="black")
e1.pack(side="left")


but1 = Button(root, text="graph me", command=graph)
but1.place(anchor=CENTER)
but1.pack()


root.mainloop()

