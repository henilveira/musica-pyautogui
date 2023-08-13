import pyautogui
import time

p = pyautogui

p.PAUSE = 1

def gods_chrome():
    p.press('win')
    p.write('chrome')
    p.press('enter')
    p.click(1072,594, duration=1) #Selecionar perfil
    p.click(146,101, duration=1) #Selecionar o Youtube
    p.click(635,166, duration=1) # Selecionar a barra de pesquisa
    p.write('Godspeed - Frank Ocean')
    p.press('enter')
    p.click(579,411, duration=1) # entrar no vídeo

def gods_edge():
    p.press('win')
    p.write('edge')
    p.press('enter')
    p.write('youtube.com')
    p.press('enter')
    p.click(635,166, duration=1)
    p.write('Godspeed - Frank Ocean')
    p.press('enter')
    p.click(579,411, duration=1)

def wf_edge():
    p.press('win')
    p.write('edge')
    p.press('enter')
    p.write('youtube.com')
    p.press('enter')
    p.click(635,166, duration=1)
    p.write('White Ferrari - Frank Ocean')
    p.press('enter')
    p.click(579,411, duration=1)

def wf_chrome():
    p.press('win')
    p.write('chrome')
    p.press('enter')
    p.click(1072,594, duration=1) #Selecionar perfil
    p.click(146,101, duration=1) #Selecionar o Youtube
    p.click(635,166, duration=1) # Selecionar a barra de pesquisa
    p.write('White Ferrari - Frank Ocean')
    p.press('enter')
    p.click(579,411, duration=1) # entrar no vídeo

def main():
    print('-=='*12)
    print('BOT de Música')
    print('-=='*12)



    while True:
        print('1. White Ferrari - Frank Ocean')
        print('2. Godspeed - Frank Ocean')
        print('3. Sair')

        menu = int(input('Escolha uma das opções: '))

        print('1. Microsoft Edge')
        print('2. Google Chrome')
        print('3. Voltar')
        navegador = int(input('Em que plataforma deseja escutar? '))


        if menu == 1 and navegador == 1:
            wf_edge()
            print('Tocando White Ferrari no Microsoft Edge!')
        elif menu == 1 and navegador == 2:
            wf_chrome()
            print('Tocando White Ferrari no Google Chrome!')
        elif menu == 2 and navegador == 2:
            gods_chrome()
            print('Tocando Godspeed - Frank Ocean no Google Chrome!')
        elif menu == 2 and navegador == 1:
            gods_edge()
            print('Tocando Godspeed - Frank Ocean no Microsoft Edge!')
        elif navegador == 3:
            main()
        elif menu == 3:
            print('Você escolheu sair ;(')
            break
        else:
            print('Você digitou uma opção inválida.')
        
if __name__ == "__main__":
    main()