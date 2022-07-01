import time
from tkinter import ttk
import tkinter
from tkinter import *

janela = tkinter.Tk()
janela.title ('Metrônomo')
janela.geometry ('640x360+408+200')
janela.configure (bg ='white')




compasso = [4,3,2]

print(compasso)



#combobox
selecione = Entry(ttk.Combobox(janela, values=compasso).place(x=150, y= 250)


janela.mainloop()