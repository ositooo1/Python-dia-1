from concurrent.interpreters import create
import os

os.system("cls")
# 6- Administrador de tareas:
# Permite al usuario agregar tareas con una descripción y una fecha de vencimiento.
# Muestra la lista de tareas agregadas.
# Permite al usuario marcar una tarea como completada y eliminar tareas de la lista.


class Task:
    def __init__(self, desc, fecha):
        self.desc = desc
        self.fecha = fecha
        self.completado = False


tareas = []

while True:
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Marcar como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        desc = input("Describe la tarea: ")
        fecha = input("Fecha de vencimiento: ")
        tareas.append(Task(desc, fecha))
        print("Tarea agregada.")

    elif opcion == "2":
        if not tareas:
            print("No hay tareas.")
        else:
            for i, t in enumerate(tareas, 1):
                estado = "✓" if t.completado else " "
                print(f"{i}. [{estado}] {t.desc} - {t.fecha}")

    elif opcion == "3":
        if not tareas:
            print("No hay tareas.")
            continue
        for i, t in enumerate(tareas, 1):
            print(f"{i}. {t.desc}")
        num = int(input("Número de tarea a completar: "))
        if 1 <= num <= len(tareas):
            tareas[num - 1].completado = True
            print("Tarea completada.")

    elif opcion == "4":
        if not tareas:
            print("No hay tareas.")
            continue
        for i, t in enumerate(tareas, 1):
            print(f"{i}. {t.desc}")
        num = int(input("Número de tarea a eliminar: "))
        if 1 <= num <= len(tareas):
            del tareas[num - 1]
            print("Tarea eliminada.")

    elif opcion == "5":
        break
    else:
        print("Opción inválida.")
