from pilha_sequencial import Pilha

pilha = Pilha(5)
if pilha.vazia():
    print('A pilha está vazia')

if pilha.cheia():
    print('A pilha está cheia')

for i in range(1, 50):
    pilha.empilha(i)
    print(f'Empilhando {i}')