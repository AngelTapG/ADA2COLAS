class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return None

def sumar_colas(cola_a, cola_b):
    cola_resultado = Cola()
    
    while not cola_a.esta_vacia() and not cola_b.esta_vacia():
        suma = cola_a.desencolar() + cola_b.desencolar()
        cola_resultado.encolar(suma)
    
    return cola_resultado

def llenar_cola(nombre_cola):
    cola = Cola()
    while True:
        try:
            valor = int(input(f"Ingrese un valor para la {nombre_cola} (o cualquier letra para terminar): "))
            cola.encolar(valor)
        except ValueError:
            break
    return cola

def main():
    print("Bienvenido al programa de suma de colas.")
    
    print("\nIngrese los valores para la Cola A:")
    cola_a = llenar_cola("Cola A")
    
    print("\nIngrese los valores para la Cola B:")
    cola_b = llenar_cola("Cola B")

    cola_resultado = sumar_colas(cola_a, cola_b)

    print("\nCola Resultado:")
    while not cola_resultado.esta_vacia():
        print(cola_resultado.desencolar())

if __name__ == "__main__":
    main()
