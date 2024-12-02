from pilha import*
entrada=input('''Editor de Pilha v1.2
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
Digite sua opção: [ _ ]''')

while True:
    if entrada=='e':
        minha_pilha.empilhar(valor)
    if entrada=='d':
        minha_pilha.Desempilhar()
    if entrada=='t':
        minha_pilha.tamanho()
    if entrada=='o':
        minha_pilha.topo()
    if entrada=='v':
        minha_pilha.vazia()
    if entrada=='p':
        Pilha_2=Pilha()
    if entrada=='c':
        colado=pilha2+minha_pilha
        print(colado)











    if entrada=='s':
        break
