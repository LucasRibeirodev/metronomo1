import tkinter
from tkinter import *
import time

contagens = [1, 2, 3, 4]

janela = tkinter.Tk()
janela.title ('Metrônomo')
janela.geometry ('640x360+408+200')
janela.configure (bg ='white')

def play_metronomo():
    batidas_por_segundos = 60/int(velocidade_metronomo.get())
    while True:
        for contagem in contagens:
            print(contagem)
            contagem = contagem + 1
            time.sleep(batidas_por_segundos)

#botão iniciar
button = Button(janela, text='Iniciar', width=6, command=play_metronomo)
button.place(x=100, y=100)

#botão sair
button = Button(janela, text='Sair', width=6, command=janela.quit())
button.place(x=300, y=100)

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