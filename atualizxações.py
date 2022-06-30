import tkinter
from tkinter.ttk import *
import time

    janela = tkinter.Tk()
    janela.title ('Metrônomo')
    janela.geometry ('640x360+408+200')
    janela.configure (bg ='ececec')

    # botão iniciar
    button = Button(janela, text='Iniciar', width=6, command=play_metronomo)
    buton.place(x=100, y=100)

    # botão sair
    button = Button(janela, text='Sair', width=6, command=janela.destroy)
    buton.place(x=300, y=100)

    # labels
    Label(janela, text='Tempo', font=('Calibri', 15)).place(x50, y=200)

    # Velocidade Metronomo
    velocidade_metronomo = Entry(janela, width=10, font=('Calibri', 15))
    velocidade_metronomo.place(x=100, y=200)

    # titulo
    title = Label(janela, text='Metronomo', font=('Calibri', 24))
    title.place(x=250, y=0)

def play_metronomo():
    batidas_por_segundos = 60/int(velocidade_metronomo.get())
    i = 0
    while True:
        print(i)
        i = i + 1
        time.sleep(batidas_por_segundos)



#iniciar loop
janela.mainloop()