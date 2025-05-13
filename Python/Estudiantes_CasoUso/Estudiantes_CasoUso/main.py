from estudiantes.estudiante import CrearEstudiante
from estudiantes.nota import CrearNotas, ConsultarNotas
from collections import deque

listaEstudiantes = []
listaNotas = []

print("BIENVENIDO A NUESTRO SISTEMA DE GESTIÓN DE ESTUDIANTES")
option = 99;

while(option != 0):
    print("¿Que deseas hacer?\n")
    print("1. Insertar nuevo estudiante con sus notas\n2. Consultar notas por el id del estudiante.\n.3. Consultar promedio.\n")
    option = int(input())

    if(option == 1):
        print("\n==== REGISTRAR NUEVO ESTUDIANTE ===\n")
        id = input("Ingrese el ID del estudiante: ")
        nombre = input("Ingrese el nombre del estudiante: ")
        apellido = input("Ingrese el apellido del estudiante: ")
        estudiante = CrearEstudiante(id, nombre, apellido)
        listaEstudiantes.append(estudiante)
        print("El estudiante que se va a guardar será: ", estudiante)


        print("\n==== REGISTRAR NOTAS A ESTUDIANTE ===\n")

        mate = int(input("Ingrese la nota de Matematicas: "))
        ingles = int(input("Ingrese la nota de ingles: "))
        espa = int(input("Ingrese la nota de español: "))

        nota = CrearNotas(id, mate, ingles, espa)
        listaNotas.append(nota)
    elif(option == 2):
        print("\n==== CONSULTAR NOTAS DE UN ESTUDIANTE ===\n")
        id = input("Ingrese el ID del estudiante: ")
        notas = ConsultarNotas(id, listaNotas)
        print(notas)
    elif(option == 3):
        print("\n==== OBTENER PROMEDIO DE NOTAS DE UN ESTUDIANTE ===\n")
        id = input("Ingrese el ID del estudiante: ")
        notas = ConsultarNotas(id, listaNotas)
        res = 0
        for nota in notas:
            res += int(nota)
            print("RES = ", res)
        print("El promedio total es de: ",  (  (res - int(id))  /(len(notas)-1))  )
