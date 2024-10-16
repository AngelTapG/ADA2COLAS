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

    def tamanio(self):
        return len(self.items)

class SistemaColas:
    def __init__(self):
        self.colas = {}
        self.ultimo_numero = 0

    def llegada_cliente(self, servicio):
        if servicio not in self.colas:
            self.colas[servicio] = Cola()
        
        self.ultimo_numero += 1
        numero_atencion = f"{servicio}-{self.ultimo_numero}"
        self.colas[servicio].encolar(numero_atencion)
        return numero_atencion

    def atender_cliente(self, servicio):
        if servicio in self.colas and not self.colas[servicio].esta_vacia():
            return self.colas[servicio].desencolar()
        return None

def main():
    sistema = SistemaColas()

    while True:
        entrada = input("Ingrese comando (C para cliente, A para atender, Q para salir): ").strip().upper()
        
        if entrada == 'Q':
            break
        
        if len(entrada) < 2:
            print("Comando inválido. Intente nuevamente.")
            continue
        
        comando = entrada[0]
        servicio = entrada[1:]
        
        if comando == 'C':
            numero = sistema.llegada_cliente(servicio)
            print(f"Cliente agregado. Número de atención: {numero}")
        elif comando == 'A':
            numero = sistema.atender_cliente(servicio)
            if numero:
                print(f"Atendiendo al cliente: {numero}")
            else:
                print(f"No hay clientes en espera para el servicio {servicio}")
        else:
            print("Comando inválido. Intente nuevamente.")

if __name__ == "__main__":
    main()
