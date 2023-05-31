from collections import deque

class Cola:
    def __init__(self):
        self.items = deque()

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if self.esta_vacia():
            return None
        return self.items.popleft()

# Crear una instancia de la Cola
cola = Cola()

# Encolar elementos en la Cola
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)

# Desencolar elementos de la Cola y mostrarlos
while not cola.esta_vacia():
    elemento = cola.desencolar()
    print("Desencolado:", elemento)
