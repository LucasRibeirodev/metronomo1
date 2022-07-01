import tkinter
from tkinter import *
from tkinter import ttk
import time
from playsound import playsound

janela = tkinter.Tk()
janela.title ('Metrônomo')
janela.geometry ('640x360+408+200')
janela.configure (bg ='white')

compasso = [4, 3, 2]
opcao = 0
ligaDesliga = False

def play_metronomo():
    global ligaDesliga
    ligaDesliga = not ligaDesliga

    opcao = selecionar.get()

    batidas_por_minutos = 60/int(velocidade_metronomo.get())

    while ligaDesliga:
        for contagem in range (0, int(opcao)):
            print(contagem)
            playsound('C:/Users/gesta/Desktop/Projetos/metronomo1/2.wav')
            time.sleep(batidas_por_minutos - 0.255)
        break


#botão iniciar
iniciarButton = Button(janela, text='Iniciar', width=6, command=play_metronomo)
iniciarButton.place(x=100, y=100)

#botão sair
stopButton = Button(janela, text='Parar', width=6, command=play_metronomo)
stopButton.pack(pady=100, padx=300)

#labels
Label(janela, text='Tempo', font=('Calibri', 11)).place(x=50, y=200)
Label(janela, text='Compasso', font=('Calibri', 11)).place(x= 50, y= 275)

#combobox
selecionar = ttk.Combobox(janela, values=compasso)
selecionar.place(x= 120, y= 275)

#Velocidade Metronomo
velocidade_metronomo = Entry(janela, width=10, font=('Calibri', 15))
velocidade_metronomo.place(x=100, y=200)

#titulo
title = Label(janela, text='Metrônomo', font=('Calibri', 24))
title.place(x=250, y=0)







#iniciar loop
janela.mainloop()