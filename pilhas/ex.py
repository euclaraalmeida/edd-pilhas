class PilhaException(Exception):
    def __init__(self,mesagem):
        super().__init__(mensagem)
class PilhaSequencial:
    def __init__(self):
        self.__dados=[]

    def vazia(self):
        return len(self.__dados)==0

    def tamanho(self):
        return len(self__.dados)

    def topo(self):
        # erro caso a lista esta vazia
        if self.vazia():
            raise PilhaException('A pilha esta vazia')
        
        return self.__dados[0]

    def inserir(self):
        self.__dados.insert[0,dado]

    def remover(self):
        return self.__dados.pop[0]

    def __str__(self):
        return self.__dados.__str__()
    
    def imprimir(self):
        print(self.__str__())

if __name__ == '__main__':
    # criando uma instancia, p para acessar os métodos e atributos definidos na classe.

    p = PilhaSequencial()
    for i in range(1,6):
        p.inserir(i * 10)

    print(p)