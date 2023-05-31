class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.items.pop()

# Crear una instancia de la Pila
pila = Pila()

# Apilar elementos en la Pila
pila.apilar(100)
pila.apilar(200)
pila.apilar(300)
pila.apilar(400)
pila.apilar(500)


# Desapilar elementos de la Pila y mostrarlos
while not pila.esta_vacia():
    elemento = pila.desapilar()
    print("Desapilado:", elemento)