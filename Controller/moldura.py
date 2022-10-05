
coluna = ('-')
nc = 120
linha =('|')
nl = 50
v=' '*118

def Coluna():
    for c in range(0, nc):
        print(coluna, end='')
Coluna()

def Linha():
    for l in range(0,nl):
        print(linha + v + linha)
    print()
Linha()

def Coluna():
    for c in range(0, nc):
        print(coluna, end='')
Coluna()


# def matriz():
#     print(Coluna() + Linha())
#     print(Coluna())
# matriz()
