import os
import time
import random
tabela = [1,0,0,0,0,0,0,0,2]
cabeca=0
corpo=0
q_corpo=[0]
nova_posicao=0
pontuacao=2
comida = 8
def comer():
    global corpo
    global cabeca
    global q_corpo
    q_corpo.append(1)
    corpo = cabeca
    tabela [cabeca] = tabela [nova_posicao]
    tabela[corpo]=pontuacao-1
    cabeca = nova_posicao 

def andar():
    global cabeca
    global corpo
    if q_corpo[0] == 0:
        tabela[cabeca],tabela[nova_posicao]= 0,tabela[cabeca]
        cabeca=nova_posicao
    if q_corpo[0] >= 1:
        tabela[nova_posicao],tabela[cabeca],tabela[corpo]=tabela[cabeca],tabela[corpo],0
        corpo=cabeca
        cabeca=nova_posicao

while True:
    posicao=0
    os.system('cls')
    for x in range(3):
        for y in range(3):
            print(tabela[posicao], end=" ")
            posicao = posicao + 1
        print()
    movimento = input("movimentos w,a,s,d: ")
    if movimento =='s':
        if nova_posicao<6:
            nova_posicao = nova_posicao + 3
            if nova_posicao == comida:
                comer()           
            else:
                andar()
    if movimento =='w':
        if nova_posicao>=3:
            nova_posicao = nova_posicao - 3
            if nova_posicao == comida:
                comer()           
            else:
                andar()
    if movimento =='d':
        if nova_posicao not in [2,5,8]:
            nova_posicao = nova_posicao + 1
            if nova_posicao == comida:
             comer()           
            else:
             andar() 
    if movimento =='a':
        if nova_posicao not in [0,3,6]:
            nova_posicao = nova_posicao - 1
            if nova_posicao == comida:
              comer()           
            else:
                andar()
    if cabeca == comida:
        tabela[cabeca] = pontuacao
        tabela[corpo] = pontuacao - 1
        pontuacao = pontuacao+1
        comida = random.randint(0, 8)
        while comida == cabeca or comida == corpo:
            comida = random.randint(0, 8)
        tabela[comida]=pontuacao