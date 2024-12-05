# Sin tkinder la prueba inicial 
# Lista para almacenar los alumnos
alumnos = []

#funciones para mejor estructuracion por cada funcion
# Funcion para calcular la calificación a partir de la nota
def calificacion(nota):
    if nota < 5:
        return "SS"
    elif 5 <= nota < 6.99:
        return "AP"
    elif 7 <= nota < 9:
        return "NT"
    else:
        return "SB"

# Función para mostrar todos los alumnos
def mostrar_alumnos():
    if not alumnos:
        print("No hay alumnos registrados.")
    else:
        print("CEDULA APELLIDOS NOMBRE NOTA CALIFICACION")
        for alumno in alumnos:
            print(f"{alumno["cedula"]} {alumno["apellidos"]} {alumno["nombre"]} {alumno["nota"]} {alumno["calificacion"]}")

# Función para agregar un alumno
def agregar_alumno():
    cedula = input("Ingrese la cedula: ")
    if any(alumno["cedula"] == cedula for alumno in alumnos):
        print("Ya existe un alumno con esa cedula.")
    else:
        apellidos = input("Ingrese los apellidos: ")
        nombre = input("Ingrese el nombre: ")
        nota = float(input("Ingrese la nota: "))
        alumnos.append({
            "cedula": cedula,
            "apellidos": apellidos,
            "nombre": nombre,
            "nota": nota,
            "calificacion": calificacion(nota)
        })
        print("Alumno agregado correctamente.")

# Función para eliminar un alumno por cedula
def eliminar_alumno():
    cedula = input("Ingrese la cedula del alumno a eliminar: ")
    global alumnos
    alumnos = [alumno for alumno in alumnos if alumno["cedula"] != cedula]
    print("Alumno eliminado, si estaba en el registro.")

# Función para consultar un alumno por numero de  cedula
def consultar_alumno():
    cedula = input("Ingrese la cedula del alumno a consultar: ")
    for alumno in alumnos:
        if alumno["cedula"] == cedula:
            print(f"Nota: {alumno["nota"]}, Calificacion: {alumno["calificacion"]}")
            return
    print("Alumno no encontrado en la lista")

# Funcion para modificar la nota de un alumno por cédula
def nota():
    cedula = input("Ingrese la cedula del alumno a modificar: ")
    for alumno in alumnos:
        if alumno["cedula"] == cedula:
            nueva_nota = float(input("Ingrese la nueva nota: "))
            alumno["nota"] = nueva_nota
            alumno["calificacion"] = calificacion(nueva_nota)
            print("Nota modificada correctamente.")
            return
    print("Alumno no encontrado.")

# Funcion para mostrar alumnos suspensos
def suspendidos():
    print("Alumnos suspensos:")
    for alumno in alumnos:
        if alumno["nota"] < 5:
            print(f"{alumno["cedula"]} {alumno["apellidos"]} {alumno["nombre"]} {alumno["nota"]} {alumno["calificacion"]}")

# Funcion para mostrar alumnos aprobados
def aprobados():
    print("Alumnos aprobados:")
    for alumno in alumnos:
        if alumno["nota"] >= 5:
            print(f"{alumno["cedula"]} {alumno["apellidos"]} {alumno["nombre"]} {alumno["nota"]} {alumno["calificacion"]}")
# Función para mostrar candidatos a Cuadro de honor
def mostrar_mh():
    print("Candidatos a cuadro de honor:")
    for alumno in alumnos:
        if alumno["nota"]==10:
            print(f"{alumno["cedula"]} {alumno["apellidos"]} {alumno["nombre"]} {alumno["nota"]} {alumno["calificacion"]}")

#menu 
def menu():
    while True:
        print("\nGestor de alumnos")
        print("1- Mostrar alumnos")
        print("2- Agregar alumno")
        print("3- Eliminar alumno")
        print("4- Consultar nota y calificación")
        print("5- Modificar nota")
        print("6- Mostrar suspendidos")
        print("7- Mostrar aprobados")
        print("8- Mostrar candidatos a cuadro de honor")
        print("9- Salir")

        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            mostrar_alumnos()
        elif opcion == "2":
            agregar_alumno()
        elif opcion == "3":
            eliminar_alumno()
        elif opcion == "4":
            consultar_alumno()
        elif opcion == "5":
            nota()
        elif opcion == "6":
            suspendidos()
        elif opcion == "7":
            aprobados()
        elif opcion == "8":
            mostrar_mh()
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Intentelo nuevamente")
menu()