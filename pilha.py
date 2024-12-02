class Pilha:
    def __init__(self):
        self.pilha = []
    
    def topo(self) -> None:
            if not self.isEmpty():
                return self.pilha[-1]
            return None

    def isEmpty(self) -> bool:
        return len(self.pilha) == 0

    def Empilhar(self, valor) -> None:
            if len(self.pilha) < 10:
                if isinstance(valor, int):
                    self.pilha.append(valor)
                else:
                    print("Apenas números inteiros podem ser empilhados.")
            else:
                 print("A pilha já atingiu o número máximo de elementos.")
    
    def Desempilhar(self) -> None:
        if not self.isEmpty():
            self.pilha.pop()
        else:
             print("Não foi possível desempilhar. A pilha está vazia.")

    def Tamanho(self) -> int:
        return len(self.pilha)
    
