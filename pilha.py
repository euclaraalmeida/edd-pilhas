'''Editor de Pilha v1.2
=====================================
Pilha Selecionada: 3 de 10
[ ] <- topo
=====================================
(e) Empilhar
(d) Desempilhar
(t) Tamanho
(o) Obter elemento do topo
(v) Teste de pilha vazia
(r) Criar nova Pilha
(n) Inverter os elementos da pilha
(z) Esvaziar a pilha
(c) Concatenar duas pilhas
(m) Escolher outra pilha
(n) Conversão dec/bin
(s) Sair
=====================================
Digite sua opção: [ _ ]

'''
import numpy as np

class Pilha:
    def __init__(self, tamanho:int = 3):
        self.dados = np.full(tamanho, None)
        self.topo = 0

    def vazia(self):
        return self.topo == 0
      
    def cheia(self):
        return self.topo == (len(self.dados))

    def empilhar(self,valor):
        if self.cheia():
            ('a pilha esta cheia')
        self.dados[self.topo] = valor 
        self.topo+=1

    def Desempilhar(self,valor):
        if self.vazia():
            print(' a pilha esta vazia')

        self.topo-=1
        valor = self.dados[self.topo]
        self.dados[self.topo] = None
        return valor 

    def tamanho(self):
        return len(self.dados)

    def NovaPilha(self, tamanho:int = 10):
        self.novapilha = np.full(tamanho, None)
        self.novotopo = 0
    
    def inverter(self):
        while not minha_pilha.vazia():
            pilha_2.empilhar(minha_pilha)

    def __str__(self):
        if self.vazia():
            return "Pilha vazia"
        return "Topo -> " + " -> ".join(map(str, reversed(self.pilha_2))) + " -> Base"
    def topo(self):
        return self.dados[self.topo-1]
    def contanear(self):
        sel
        return 


minha_pilha=Pilha()
pilha_2= Pilha()
minha_pilha.empilhar(2)
minha_pilha.empilhar(3)
minha_pilha.empilhar(5)
pilha_2.inverter()

