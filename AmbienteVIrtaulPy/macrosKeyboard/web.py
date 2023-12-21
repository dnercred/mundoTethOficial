 # Bibliotecas Importadas 

import webbrowser  as web
import pyautogui as bot
import time
from tkinter import *
from tkinter import ttk



###     Variaveis Gerais 

mensagemDeErro = ("Atenção Usuario Deu Erro  ")
contagem = [1,2,3,4,5 ] 



resposta =int(input(f"Atenção digite o Numero Pra execultar escript    :   "))
#respostas = respostas

### Bloco de Funções
def abestado():
    bot.alert("DEU CERTO ABESTADO")

def tkinter():
     janela = Tk()
     frm = ttk.Frame(janela, padding =0) 
     frm.grid()
     janela.title("🔑PROGRAMA De Automação de Scripts <DIB COD/>🔑")
     ttk.Label (frm,  text="🔫Lista De Scripts🔫 ").grid(column=0, row=0 , padx=10 ,pady=10)
     ttk.Button(frm, text="🆘Sair Do Programa🆘", command=janela.destroy).grid(column=0, row=1,  padx=5 ,pady=5 )
     ttk.Button(frm, text="Abrir pyautogui", command=tkinter).grid(column=2, row=2, padx=5 ,pady=5)
     ttk.Button(frm, text ="Buscar",command=abestado).grid(column=2, row=3, padx=5 ,pady=15)
 
     ttk.Button(frm, text="botao4", command=tkinter).grid(column=2, row=4, padx=5 ,pady=5)
     ttk.Button(frm, text ="botao5",command=abestado).grid(column=2, row=5, padx=5 ,pady=15)
     ttk.Button(frm, text ="botao6",command=abestado).grid(column=3, row=0, padx=5 ,pady=15)
     ttk.Button(frm, text ="botao7",command=abestado).grid(column=3, row=1, padx=5 ,pady=15)
     ttk.Button(frm, text ="botao8",command=abestado).grid(column=2, row=2, padx=5 ,pady=15)
     ttk.Button(frm, text ="botao9",command=abestado).grid(column=2, row=3, padx=5 ,pady=15)
     ttk.Button(frm, text ="botao10",command=abestado).grid(column=2, row=6, padx=5 ,pady=15)
     ttk.Button(frm, text ="botao11",command=abestado).grid(column=2, row=7, padx=5 ,pady=15)
     ttk.Button(frm, text ="botao12",command=abestado).grid(column=2, row=8, padx=5 ,pady=15)
     janela.mainloop()
     


               # Fazendo  o loppe while True:



while True:
    if resposta == 1:
        web.open("http://stackoverflow.com")
    
    elif resposta == 2:
        for i in range(5):
            print('Ver alerta')
            bot.alert("DENNER TESTE")
  

    elif resposta == 3:
        print("Vou sair ")
        

    elif resposta == 4:
        print("Vou Abrir sistemaViverBemSeguros")
        web.open_new('https://www.sistemaviverbemseguros.com/')
    elif resposta ==100 :
        tkinter()




    else:
        print(mensagemDeErro)
        print("Atenção Sera Encerrado O programa")

        time.sleep(5)
        print("Atenção Sera Encerrado O programa")
        for i in range(5):
            print(contagem)
    break
    # Finalizando o Lopper



## Tkinter Interface grafica Do Python



