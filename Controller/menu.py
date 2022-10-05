import os
from time import sleep
import app.vue.interface
from app.vue.menus import menuPrincipal, menuSecundario, teste
from rich.markdown import Markdown
from rich.console import Console

console = Console()

# Markdown
with open(".\\menu.md", encoding='UTF-8') as md:
    markdown = Markdown(md.read())
    console.print(markdown)


#------------------------------------------------------------------------------
# MENU DOS JOGOS
#------------------------------------------------------------------------------
while True:
    menuPrincipal()

    #input para guardar valor escolhido
    opcao = input('Escolha uma opção de jogo: ')
    os.system("cls")
    match opcao:
        case '1':
            #Menu segundario
            print('Escolhendo opção...')
            sleep(2)
            print('Opção {} selecioanda! Aguarde...'.format(opcao))
            sleep(2)

            menuSecundario()#chamando a função de opcoes do menu secundario

            opcao2 = input('Escolha uma outra opção de jogo: ')
            os.system("cls")
            match opcao2:
                case '4':
                    print('Voltando...')
                    sleep(2)
                    menuPrincipal()
                case '5':
                    print('Saindo...')
                    sleep(2)
                    exit()
                case other:
                    print('Escolhendo opção...')
                    sleep(2)
                    print(f'Opção invalida.Tente novamente')
                    sleep(2)
            
        case '2':
            #Menu segundario
            print('Escolhendo opção...')
            sleep(2)
            print('Opção {} selecionada! Aguarde...'.format(opcao))
            sleep(2)

            menuSecundario()

            opcao2 = input('Escolha uma outra opção de jogo: ')
            os.system("cls")
            match opcao2:
                case '4':
                    print('Voltando...')
                    sleep(2)
                    menuPrincipal()
                case '5':
                    print('Saindo...')
                    sleep(2)
                    exit()
                case other:
                    print('Escolhendo opção...')
                    sleep(2)
                    print(f'Opção invalida.Tente novamente')
                    sleep(2)
        case '3':
            print('Saindo...')
            sleep(2)
            exit()
        case other:
            print('Escolhendo opção...')
            sleep(2)
            print(f'Opção invalida.Tente novamente')
            sleep(2)

