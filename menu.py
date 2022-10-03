import os
from time import sleep
import app.vue


with open('..\vue\menuPrincipal.txt','r') as aquivoMainMenu:
    print(aquivoMainMenu)

tipo = ''
concurso = 0

apiURL = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/'
resuladostURL = 'resultados?modalidade='

tipos = { 'megasena': 'Mega-Sena', 'lotofacil': 'Lotofacil', 'quina': 'Quina',
        'lotomania': 'Lotomania', 'timemania': 'Timemania', 'duplasena': 'Dupla-Sena',
        'supersete': 'Super-Sete', 'diadesorte': 'Dia de Sorte'
        }


#------------------------------------------------------------------------------
# MENU DOS JOGOS
#------------------------------------------------------------------------------


menuPrincipal=True
while menuPrincipal == True:
# Menu
    print(f'='*40)
    print(f'Tipos de jogo')
    print(f'='*40)

# opcoes do menu principal   
    print('_'*40)
    print('1- Jogo 1')
    print('2- Jogo 2')
    print('3- Voltar')
    print('4- Sair')
    print('_'*40)

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

            def menuSecundario():
                print(f'='*40)
                print('Jogo escolhido: {} '.format(opcao))
                print(f'='*40)
            #opcoes do segundo menu
                print('_'*40)
                print('1- Ultimo jogo')
                print('2- Jogo especifico')
                print('3- Todos os jogos')
                print('4- Voltar')
                print('5- Sair')
                print('_'*40)

            menuSecundario()#fim da funcão menuSecundario
            opcao2 = input('Escolha uma outra opção de jogo: ')
            os.system("cls")
            match opcao2:
                case '4':
                    print('Voltando...')
                    sleep(2)
                    menuPrincipal
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

            def menuSecundario():
                print(f'='*40)
                print('Jogo escolhido: {} '.format(opcao))
                print(f'='*40)
            #opcoes do segundo menu
                print('_'*40)
                print('1- Ultimo jogo')
                print('2- Jogo especifico')
                print('3- Todos os jogos')
                print('4- Voltar')
                print('5- Sair')
                print('_'*40)
            menuSecundario()
            opcao2 = input('Escolha uma outra opção de jogo: ')
            os.system("cls")
            match opcao2:
                case '4':
                    print('Voltando...')
                    sleep(2)
                    menuPrincipal
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
            print('Voltando...')
            sleep(2)
            menuPrincipal
        case '4':
            print('Saindo...')
            sleep(2)
            exit()
        case other:
            print('Escolhendo opção...')
            sleep(2)
            print(f'Opção invalida.Tente novamente')
            sleep(2)









    # def menuSecundario():
    #     jescolhido = opcao
    #     print(f'='*40)
    #     print('Jogo escolhido: {jescolhido} ')
    #     print(f'='*40)

    #     print('_'*40)
    #     print('Ultimo jogo')
    #     print('Jogo especifico')
    #     print('Todos os jogos')
    #     print('_'*40)

