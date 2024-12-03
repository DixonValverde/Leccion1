#Escriba un programa para la gestión de las calificaciones de un grupo de alumnos. 
#Los alumnos se caracterizan por: DNI, Apellidos, Nombre, Nota y Calificación, donde Nota 
#es la calificación numérica (un número real) dada por el profesor, mientras que la Calificación 
#se calculará automáticamente a partir de la nota (siempre que se introduzca o actualice ésta), 
#de la siguiente forma: SS si Nota<5, AP si 5≤ Nota<7 NT si 7≤ Nota<9 y SB si Nota≥9
# Las funciones que ha de realizar el programa son las siguientes. Mostrar los alumnos con toda su información,
#de la siguiente forma: DNI APELLIDOS, NOMBRE NOTA CALIFICACIÓN; 33245 García Pérez, Carlos 7,8 NT; 128676 Romero Rodríguez, 
#Luisa 9 SB; Introducir alumno, donde se pide DNI, apellidos, nombre y nota del alumno. No pueden existir dos alumnos con el mismo DNI.
#3. Eliminar alumno a partir del DNI. 4. Consultar la nota y la calificación de un alumno a partir del DNI 
# 5. Modificar la nota de un alumno a partir del DNI. 6. Mostrar alumnos suspensos 7. Mostrar alumno aprobados 8. Mostrar candidatos a M
#MH (los que tengan un 10 de nota) 9. Modificar calificación: permite modificar la calificación calculada automáticamente



#Tkinder para interfaz grafica con messagebox para ingresar datos y ver y ttk para ordenar los datos

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Lista para almacenar los alumnos
alumnos = []

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

# Funcion para agregar un alumno
def agregar_alumno():
    cedula = entry_cedula.get()
    apellidos = entry_apellidos.get()
    nombre = entry_nombre.get()
    try:
        nota = float(entry_nota.get())
        if any(alumno["cedula"] == cedula for alumno in alumnos):
            messagebox.showerror("Error", "Ya existe un alumno con esa cédula.")
        else:
            alumnos.append({
                "cedula": cedula,
                "apellidos": apellidos,
                "nombre": nombre,
                "nota": nota,
                "calificacion": calificacion(nota)
            })
            limpiar_campos()
            actualizar_tabla()
            messagebox.showinfo("Éxito", "Alumno agregado correctamente.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese una nota válida.")

# Funcion para eliminar un alumno
def eliminar_alumno():
    cedula = entry_cedula.get()
    global alumnos
    alumnos = [alumno for alumno in alumnos if alumno["cedula"] != cedula]
    limpiar_campos()
    actualizar_tabla()
    messagebox.showinfo("Éxito", "Alumno eliminado, si existía en el registro.")

# Función para consultar un alumno
def consultar_alumno():
    cedula = entry_cedula.get()
    for alumno in alumnos:
        if alumno["cedula"] == cedula:
            messagebox.showinfo("Consulta", f"Apellidos: {alumno['apellidos']}\nNombre: {alumno['nombre']}\nNota: {alumno['nota']}\nCalificación: {alumno['calificacion']}")
            return
    messagebox.showerror("Error", "No se encontró un alumno con esa cedula.")

# Funcion para modificar la nota de un alumno
def modificar_nota():
    cedula = entry_cedula.get()
    try:
        nueva_nota = float(entry_nota.get())
        for alumno in alumnos:
            if alumno["cedula"] == cedula:
                alumno["nota"] = nueva_nota
                alumno["calificacion"] = calificacion(nueva_nota)
                limpiar_campos()
                actualizar_tabla()
                messagebox.showinfo("Éxito", "Nota modificada correctamente.")
                return
        messagebox.showerror("Error", "No se encontró un alumno con esa cédula.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese una nota válida.")

# Funcion para mostrar todos los alumnos
def mostrar_alumnos():
    actualizar_tabla()
    messagebox.showinfo("Alumnos", f"Se han mostrado {len(alumnos)} alumnos en la tabla.")

# Funcion para mostrar los alumnos suspendidos (nota < 5)
def suspendidos():
    actualizar_tabla([alumno for alumno in alumnos if alumno["nota"] < 5])

# Funcion para mostrar los alumnos aprobados (nota >= 5)
def aprobados():
    actualizar_tabla([alumno for alumno in alumnos if alumno["nota"] >= 5])

# Funcion para mostrar el cuadro de honor (nota >= 9)
def cuadro_de_honor():
    actualizar_tabla([alumno for alumno in alumnos if alumno["nota"] >= 9])

# Funcion para actualizar la tabla (Treeview)
def actualizar_tabla(filtrar=None):
    # Limpiar la tabla
    for row in tabla.get_children():
        tabla.delete(row)
    # Insertar datos actualizados
    lista = filtrar if filtrar is not None else alumnos
    for alumno in lista:
        tabla.insert("", tk.END, values=(alumno["cedula"], alumno["apellidos"], alumno["nombre"], alumno["nota"], alumno["calificacion"]))

# Funcion para limpiar los campos de entrada
def limpiar_campos():
    entry_cedula.delete(0, tk.END)
    entry_apellidos.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_nota.delete(0, tk.END)

# Ventana principal
root = tk.Tk()
root.title("Gestor de Alumnos")

# Crear los widgets y botones
frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Cédula:").grid(row=0, column=0, padx=5, pady=5)
entry_cedula = tk.Entry(frame_inputs)
entry_cedula.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Apellidos:").grid(row=1, column=0, padx=5, pady=5)
entry_apellidos = tk.Entry(frame_inputs)
entry_apellidos.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Nombre:").grid(row=2, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(frame_inputs)
entry_nombre.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Nota:").grid(row=3, column=0, padx=5, pady=5)
entry_nota = tk.Entry(frame_inputs)
entry_nota.grid(row=3, column=1, padx=5, pady=5)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_agregar = tk.Button(frame_buttons, text="1-Agregar Alumno", command=agregar_alumno, bg="#FFC0CB", fg="black")
btn_agregar.grid(row=0, column=0, padx=5, pady=5)

btn_eliminar = tk.Button(frame_buttons, text="2-Eliminar Alumno", command=eliminar_alumno, bg="#FFB6C1", fg="black")
btn_eliminar.grid(row=0, column=1, padx=5, pady=5)

btn_consultar = tk.Button(frame_buttons, text="3-Consultar Alumno", command=consultar_alumno, bg="#ADD8E6", fg="black")
btn_consultar.grid(row=0, column=2, padx=5, pady=5)

btn_modificar = tk.Button(frame_buttons, text="4-Modificar Nota", command=modificar_nota, bg="#FFFFE0", fg="black")
btn_modificar.grid(row=0, column=3, padx=5, pady=5)

btn_mostrar = tk.Button(frame_buttons, text="5-Mostrar Alumnos", command=mostrar_alumnos, bg="#F5F5F5", fg="black")
btn_mostrar.grid(row=0, column=4, padx=5, pady=5)

btn_suspendidos = tk.Button(frame_buttons, text="6-Suspendidos", command=suspendidos, bg="#FF6347", fg="black")
btn_suspendidos.grid(row=0, column=5, padx=5, pady=5)

btn_aprobados = tk.Button(frame_buttons, text="7-Aprobados", command=aprobados, bg="#90EE90", fg="black")
btn_aprobados.grid(row=0, column=6, padx=5, pady=5)

btn_cuadro = tk.Button(frame_buttons, text="8-Cuadro de Honor", command=cuadro_de_honor, bg="#FFD700", fg="black")
btn_cuadro.grid(row=0, column=7, padx=5, pady=5)

frame_tabla = tk.Frame(root)
frame_tabla.pack(pady=10)
#Que vaya la informacion en orden separados
columnas = ("Cédula", "Apellidos", "Nombre", "Nota", "Calificacion")
tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=10)
#distancia
for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, width=150, anchor="center")

tabla.pack(fill="both", expand=True)

# Programa principal
root.mainloop()
