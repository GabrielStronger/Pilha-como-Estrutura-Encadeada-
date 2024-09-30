# pilhas_iguais.py

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

# Função para verificar se duas pilhas são iguais
def pilhas_iguais(pilha1, pilha2):
    if pilha1.tamanho() != pilha2.tamanho():
        return False
    temp1, temp2 = [], []
    while not pilha1.vazia():
        temp1.append(pilha1.desempilhar())
    while not pilha2.vazia():
        temp2.append(pilha2.desempilhar())
    
    iguais = temp1 == temp2
    for elemento in temp1:
        pilha1.empilhar(elemento)  # Restaura a pilha
    for elemento in temp2:
        pilha2.empilhar(elemento)  # Restaura a pilha
    return iguais

# Testando a função
if __name__ == "__main__":
    p1 = Pilha()
    p2 = Pilha()
    for i in [1, 2, 3]:
        p1.empilhar(i)
        p2.empilhar(i)
    print("Pilhas iguais:", pilhas_iguais(p1, p2))  # Deve retornar True
