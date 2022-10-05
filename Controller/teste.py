import json
import requests


apiURL = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/'
resuladostURL = 'resultados?modalidade='

tipos = { 'megasena': 'Mega-Sena', 'lotofacil': 'Lotofacil', 'quina': 'Quina',
        'lotomania': 'Lotomania', 'timemania': 'Timemania', 'duplasena': 'Dupla-Sena',
        'supersete': 'Super-Sete', 'diadesorte': 'Dia de Sorte'
        }
# novaUrl = ('{}megasena'.format(apiURL))
# print(novaUrl)

print('======================')
print(tipos)
print('======================')

escolha = input(str('Escolha uma das opções: '))

if escolha == escolha:
    novaUrl = ('{}{}'.format(apiURL, escolha))
    print(novaUrl)


    

