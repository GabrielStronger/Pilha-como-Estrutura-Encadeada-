# sequencia_retirada_carros.py

class Pilha:
    def __init__(self):
        self.elementos = []

    def empilhar(self, elemento):
        self.elementos.append(elemento)

    def desempilhar(self):
        if not self.vazia():
            return self.elementos.pop()
        raise IndexError("Pilha vazia!")

    def vazia(self):
        return len(self.elementos) == 0

# Função para determinar a sequência de retirada de carros
def sequencia_retirada(placas, placa_desejada):
    pilha = Pilha()
    for placa in placas:
        pilha.empilhar(placa)
    sequencia = []
    while not pilha.vazia():
        placa_atual = pilha.desempilhar()
        sequencia.append(placa_atual)
        if placa_atual == placa_desejada:
            break
    return sequencia[::-1]

# Testando a função
if __name__ == "__main__":
    placas = ["ABC1", "DEF2", "GHI3"]
    print("Sequência de retirada:", sequencia_retirada(placas, "DEF2"))  # Deve imprimir a sequência para liberar o carro DEF2
