import os

def imprimeMoldura(w = 'cmd'):
     
     cMax = 120
     lMax = 30
     mLat = '|'
     mSup = '-'
     
     if w == 'pshell':
          lMax = 50
     
     for i in range(cMax):
          print(mSup, end='')

     for i in range(lMax - 2):
          print(mLat, end='')
          for j in range(cMax - 2):
               print(' ', end='')
          print(mLat)

     for i in range(cMax):
          print(mSup, end='')
          
     os.system('pause >> null')

imprimeMoldura('cmd')
imprimeMoldura('pshell')