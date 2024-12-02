# implementação de uma pilha usando a técnica sequencial
import numpy as np

class Pilha:
    def __init__(self, tamanho:int = 3):
        self.__dados = np.full(tamanho, None)
        self.__topo = 0

    def vazia(self):
        return self.__topo == 0
    
    def cheia(self):
        return self.__topo == len(self.__dados)
    
    def empilha(self, carga:any):
        if self.cheia():
            raise Exception('Pilha cheia')
        self.__dados[self.__topo] = carga
        self.__topo += 1



pilha = Pilha(5)
if pilha.vazia():
    print('A pilha está vazia')

if pilha.cheia():
    print('A pilha está cheia')

for i in range(1, 50):
    pilha.empilha(i)
    print(f'Empilhando {i}')
