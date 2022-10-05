import app

def menuPrincipal():
    opcao=""
    print(f'='*40)
    print(f'Tipos de jogo')
    print(f'='*40)

    # opcoes do menu principal   
    print('_'*40)
    print('1- Jogo 1')
    print('2- Jogo 2')
    print('3- Sair')
    print('_'*40)

def menuSecundario():
    opcao=''
    print(f'='*40)
    print('Jogo escolhido: {} '.format(opcao))
    print(f'='*40)
    #opcoes do segundo menu
    print('_'*40)
    print('1- Ultimo jogo')
    print('2- Jogo especifico')
    print('3- Todos os concursos')
    print('4- Voltar')
    print('5- Sair')
    print('_'*40)