import pyautogui as bot
import time 

import mouseinfo

posicao = []

def funcaoStartMouseInfo():
    mouseinfo.mouseInfo()



funcaoStartMouseInfo()


while True:
    x,y = bot.position()
    if bot.hotkey("f6"):
        bot.write(bot.position())
        print(bot.position()) 
    else:
        time.sleep(5) 
        print(bot.position())
        print("  deu errado  ") 
        ## Atencao metodo pra entrar no arquivo E escrever o index relativo ao arquivo csv :
        with open('resultoDosindexPosicao2.txt','a') as arquivoExportado:
            print("Estou escrevendo o arquivo externo")
            print("Atencao vou pro proximo index")
          
            arquivoExportado.write(bot.position())
            time.sleep(1) 
            bot.hotkey('enter')
            bot.hotkey(bot.position())
            print(x)
            print("atencao Vou pro proximo index  Ass BOT   :   ")
