import requests
import json

#------------------------------------------------------------------------------
#Função delay de aleatoriamente 10s podendo ser alterado
#------------------------------------------------------------------------------
def delay(t = 10):
    import random
    import time
    if t < 2:
        t=10
    delays = list(range(1, t))
    random.shuffle(delays)
    num_of_secs = random.choice(delays)
    print(f'Aguarde {num_of_secs}s ', end='')
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:2d}'.format(s)
        if (s > 1 and s < num_of_secs):
            print(min_sec_format, end='s... ')
        time.sleep(1)
        num_of_secs -= 1
        if (num_of_secs != 0):
            print(f'{num_of_secs}s ', end='')
    print('FIM!')

delay(3)#pode alterar o tempo aleatoriamente
#------------------------------------------------------------------------------

url = "https://maps.googleapis.com/maps/api/geocode/json?address=140+Rua+Cica,Curitiba%C3%AD,+PR&key=AIzaSyBKP7Lndi1G9-O1NpCwV7y_QV5i7tMBx9o"
requisicao = requests.get(url)
t=requisicao.json()
# print(requisicao)
# print(t)

#lista usando dicionario
lista=dict(t)

#Mostrando os resultados
result = json.dumps(t)
# print (lista)
print(lista.values)
print(lista.keys)