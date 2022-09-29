from ast import Str
from dataclasses import dataclass


class Data(object):
    def __init__(self,dia,mes,ano):
        self.dia=dia
        self.mes=mes
        self.ano=ano
        # self.validadia=validadia
        # self.dtcompleta=dtcompleta
        print("A data do concurso é ", dia,"/", mes,"/",ano)

    def getdia(self):
        print(self.dia)
    def getmes(self):
        print (self.mes)
    def getano(self):
        print (self.ano)
        
        # def validadia(self):
        #         if self.dia >31 and self.dia <1 :
        #                 self.dia=False
        #                 print("data invalida")


data=Data(2,7,2022)
print(data.getdia)
print(data.getmes)
print(data.getano)


