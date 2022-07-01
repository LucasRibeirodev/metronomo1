import tkinter
from tkinter import *
import time
from playsound import playsound



janela = tkinter.Tk()
janela.title ('Metrônomo')
janela.geometry ('640x360+408+200')
janela.configure (bg ='white')

def play_metronomo():
    batidas_por_minutos = 60/int(velocidade_metronomo.get())
    contagem = 1
    while contagem <= 4:
        print(contagem)
        contagem += 1
        playsound('C:/Users/gesta/Desktop/Projetos/metronomo1/2.wav')
        time.sleep(batidas_por_minutos - 0.255)



#botão iniciar
iniciarButton = Button(janela, text='Iniciar', width=6, command=play_metronomo)
iniciarButton.place(x=100, y=100)

#botão sair
sairButton = Button(janela, text='Sair', width=6, command=janela.destroy).pack(pady=100, padx=300)

#labels
Label(janela, text='Tempo', font=('Calibri', 11)).place(x=50, y=200)

#Velocidade Metronomo
velocidade_metronomo = Entry(janela, width=10, font=('Calibri', 15))
velocidade_metronomo.place(x=100, y=200)

#titulo
title = Label(janela, text='Metrônomo', font=('Calibri', 24))
title.place(x=250, y=0)

#iniciar loop
janela.mainloop()