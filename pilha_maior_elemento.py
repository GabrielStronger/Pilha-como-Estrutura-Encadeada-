# pilha_maior_elemento.py

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

    def tamanho(self):
        return len(self.elementos)

# Função para encontrar o maior elemento da pilha
def maior_elemento(pilha):
    maior = None
    temp = []
    while not pilha.vazia():
        elemento = pilha.desempilhar()
        temp.append(elemento)
        if maior is None or elemento > maior:
            maior = elemento
    for elemento in temp:
        pilha.empilhar(elemento)  # Restaura a pilha
    return maior

# Testando a função
if __name__ == "__main__":
    p = Pilha()
    for i in [3, 5, 1, 4, 2]:
        p.empilhar(i)
    print("Maior elemento:", maior_elemento(p))  # Deve imprimir 5
