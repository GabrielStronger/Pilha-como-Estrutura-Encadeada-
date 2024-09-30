# inverter_sequencia.py

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

# Função para inverter a sequência de números
def inverter_sequencia(numeros):
    pilha = Pilha()
    for numero in numeros:
        pilha.empilhar(numero)
    while not pilha.vazia():
        print(pilha.desempilhar())

# Testando a função
if __name__ == "__main__":
    print("Sequência inversa:")
    inverter_sequencia([1, 2, 3, 4, 5])  # Deve imprimir 5, 4, 3, 2, 1
