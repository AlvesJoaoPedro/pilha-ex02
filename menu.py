from pilha import Pilha
from random import randint

class Menu(Pilha):
    def __init__(self):
        self.ListaPilhas = []
        for x in range(10):
            self.ListaPilhas.append(Pilha())
        
        for pilha in self.ListaPilhas:
            for _ in range(8):
                pilha.Empilhar(randint(0, 100))

        self.pilha_selecionada = 0

    def menu(self):
        while True:
            pilha_atual = self.ListaPilhas[self.pilha_selecionada]
            
            print(
                f"""
                Editor de Pilha v1.2
                ==============================
                Pilha Selecionada: {self.pilha_selecionada + 1} de {len(self.ListaPilhas)}
                {pilha_atual.topo()} <- topo
                ==============================
                (e) Empilhar
                (d) Desempilhar
                (t) Tamanho
                (o) Obter Topo da pilha
                (v) Teste de pilha vazia
                (m) Escolher outra pilha
                (s) Sair
                ==============================
                """
            )

            resposta = input("Digite sua opção: ")

            match resposta:
                case "e":
                    valor = int(input("Digite o valor inteiro que será empilhado: "))
                    pilha_atual.Empilhar(valor)
                case "d":
                    pilha_atual.Desempilhar()
                case "t":
                    print(f"Tamanho da pilha: {pilha_atual.Tamanho()}")
                case "o":
                        print(pilha_atual.topo())
                case "v":
                    if pilha_atual.isEmpty():
                        print("A pilha está vazia.")
                    else:
                        print("A pilha não está vazia.")
                case "m":
                    nova_pilha = int(input(f"Escolha a pilha de 1 a {len(self.ListaPilhas)}: ")) - 1
                    if 0 <= nova_pilha < len(self.ListaPilhas):
                        self.pilha_selecionada = nova_pilha  # Atualizando o índice da pilha selecionada
                    else:
                        print("Número de pilha inválido.")
                case "s":
                    print("Saindo...")
                    break  # Encerra o loop e sai do menu
                case _:
                    print("Opção inválida. Tente novamente.")