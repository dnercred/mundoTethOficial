import pyautogui as bot
import time 


#Lista de Cordenadas

naoLancados = 71,264
lancados = 87,323 
implantado =  105,375
emAndamentoAnalise = 106,457
pendeneteEmSistema =105,516
pendeneteDeAssinatura = 107,589
cancelados = 86,672
finalizados = 88,72
botaoDeVoltar= 24,65


#Lista de Funcoes De clicar 

def funcaoDeVoltar():
    time.sleep(2) 
    bot.click(botaoDeVoltar, duration=0.25)
    time.sleep(2)


def funcaoClicarNaoLancados():
    bot.click(naoLancados, duration=0.25)
    time.sleep(2)
#    funcaoDeVoltar()
#funcaoClicarNaoLancados()



def funcaoClicarLancados():
    bot.click(lancados)
    time.sleep(2)
    #funcaoDeVoltar()
#funcaoClicarLancados()

def funcaoClicarImplantado():
    bot.click(implantado, duration=0.25)
    time.sleep(2)
    #funcaoDeVoltar()
#funcaoClicarImplantado()


def funcaoClicarEmAndamentoAnalise():
    bot.click(emAndamentoAnalise,duration=0.25)
    time.sleep(2)
    #funcaoDeVoltar()
#funcaoClicarEmAndamentoAnalise()


def funcaoClicarPendetesEmSistema():
    bot.click(pendeneteEmSistema,duration=0.25)
    time.sleep(2)
    #funcaoDeVoltar()
#funcaoClicarPendetesEmSistema()


def funcaoClicarCancelados():
    bot.click(cancelados)
    time.sleep(2)
    #funcaoDeVoltar()

#funcaoClicarCancelados()


