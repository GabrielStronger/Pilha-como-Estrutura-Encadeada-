# TPilha.py

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

# Função TPilha que manipula pares e ímpares
def TPilha(vetor):
    pilha = Pilha()
    for numero in vetor:
        if numero % 2 == 0:
            pilha.empilhar(numero)
        else:
            if not pilha.vazia():
                pilha.desempilhar()
    while not pilha.vazia():
        print(pilha.desempilhar())

# Testando a função
if __name__ == "__main__":
    TPilha([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Deve empilhar pares e desempilhar conforme encontra ímpares
