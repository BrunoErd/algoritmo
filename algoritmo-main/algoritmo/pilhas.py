class Stack:
    def __init__(self):
        self.itens = []

    def isEmpty(self):
        self.itens == []

    def push(self, itens):
        self.itens.append(itens)

    def pop(self):
        return self.itens.pop()

    def peak(self):
        return self.itens[len(self.itens)-1]

    def size(self):
        return len(self.itens)
    
pilha = Stack()
pilha.push('A')
pilha.push('B')
pilha.push('C')
pilha.push('D')
pilha.push('E')
pilha.push('F')
print(pilha.itens)
print(pilha.peck())
print(pilha.itens)
pilha.pop()
print(pilha.itens)