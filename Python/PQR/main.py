from collections import deque, Counter, defaultdict

cola = deque([
    ["queja 1", "San Javier", 13, "Queja"], 
    ["reclamo 1", "Manrique", 7, "Reclamo"],
    ["peti 3", "Poblado", 1, "Peticion"],
    ["suge 2", "Laureles", 8, "Sugerencia"],
    ["queja 1", "", 13, "Queja"],
    ["queja 1", "El socorro", 13, "Queja"],
    ["peti 1", "Nariño", 13, "Peticion"],
    ["queja 1", "Divino niño", 13, "Queja"],
    ["suge 1", "Aurora", 13, "Sugerencia"],
    ["peti 1", "Belen", 10, "Peticion"]
])

option = 99;


while(option != 0):
    print("BIENVENIDO AL SISTEMA DE GESTIÓN DE PQRS")
    print("1. Ingresar una PQR.")
    print("2. Ver los comunes.")
    print("3. Agrupar por comuna.")
    print("0. Salir.")

    option = int(input())
    if(option == 1):
        texto = input("Ingrese el motivo\n")
        barrio = input("Ingrese el Barrio\n")
        comuna = int(input("Ingrese la comuna\n"))
        tipo = input("Ingrese el tipo (Queja, Peticion, Reclamo, Sugerencia)").capitalize()

        cola.append([texto, barrio, comuna, tipo])
    if(option == 2):
        tipos = []

        for registro in cola:
            tipo = registro[3]
            tipos.append(tipo)

        conteo = Counter(tipos)
        print(conteo.most_common(2))
    if(option == 3):
        agrupados = defaultdict(list)

        for registro in cola:
            tipo = registro[2]
            agrupados[tipo].append(registro)

        # Ejemplo: mostrar todos los agrupados
        for tipo, items in agrupados.items():
            print(f"\n{tipo}:")
            for item in items:
                print(item)

print("Hasta luego :D")