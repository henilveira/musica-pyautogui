import pyautogui
import time

p = pyautogui

p.PAUSE = 1

def edge(main):
    p.press('win') # Pressionar a tecla WINDOWS
    p.write('edge') # 
    p.press('enter')
    p.write('youtube.com')
    p.press('enter')
    p.click(635,166, duration=1)
    p.write(main)
    p.press('enter')
    p.click(579,411, duration=1)

def chrome(main):
    p.press('win')
    p.write('chrome')
    p.press('enter')
    p.click(1072,594, duration=1) #Selecionar perfil
    p.click(146,101, duration=1) #Selecionar o Youtube
    p.click(635,166, duration=1) # Selecionar a barra de pesquisa
    p.write(main)
    p.press('enter')
    p.click(579,411, duration=1) # entrar no vídeo

def main():
    print('-=='*12)
    print('BOT de Música')
    print('-=='*12)



    while True:
        menu = input('Digite a música que quer ouvir: ')

        print('1. Microsoft Edge')
        print('2. Google Chrome')
        print('3. Voltar')
        navegador = int(input('Em que plataforma deseja escutar? '))


        if navegador == 1:
            edge(menu)
            print('Tocando {} no Microsoft Edge!'.format(menu))
        elif navegador == 2:
            chrome(menu)
            print('Tocando {} no Google Chrome!'.format(menu))
        elif navegador == 3:
            main()
        elif menu == 3:
            print('Você escolheu sair ;(')
            break
        else:
            print('Você digitou uma opção inválida.')
        
if __name__ == "__main__":
    main()

            
    
# time.sleep(3) #espera 3 segundos para executar o comando
# pos = p.position() #guarda a posição do mouse no momento
# p.click(pos, duration=1) #clica na posição em que meu mouse está apontado