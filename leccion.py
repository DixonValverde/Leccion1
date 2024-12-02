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

import tkinter as tk
from tkinter import messagebox

# Lista para almacenar los alumnos
alumnos = []

# Funcion para calcular la calificacion a partir de la nota
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
            messagebox.showerror("Error", "Ya existe un alumno con esa cedula.")
        else:
            alumnos.append({
                "cedula": cedula,
                "apellidos": apellidos,
                "nombre": nombre,
                "nota": nota,
                "calificacion": calificacion(nota)
            })
            messagebox.showinfo("Exito", "Alumno agregado correctamente.")
            limpiar_campos()
            mostrar_alumnos()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese una nota valida o llene todos los datos correctamente.")

# Función para eliminar un alumno por cédula
def eliminar_alumno():
    cedula = entry_cedula.get()
    global alumnos
    alumnos = [alumno for alumno in alumnos if alumno["cedula"] != cedula]
    messagebox.showinfo("Exito", "Alumno eliminado, si existia en el registro.")
    limpiar_campos()
    mostrar_alumnos()

# Función para mostrar alumnos
def mostrar_alumnos():
    text_resultado.delete(1.0, tk.END)
    if not alumnos:
        text_resultado.insert(tk.END, "No hay alumnos registrados.\n")
    else:
        text_resultado.insert(tk.END, "CEDULA\tAPELLIDOS\tNOMBRE\tNOTA\tCALIFICACION\n")
        for alumno in alumnos:
            text_resultado.insert(tk.END, f"{alumno['cedula']}\t{alumno['apellidos']}\t{alumno['nombre']}\t{alumno['nota']}\t{alumno['calificacion']}\n")

# Función para consultar un alumno por cédula
def consultar_alumno():
    cedula = entry_cedula.get()
    for alumno in alumnos:
        if alumno['cedula'] == cedula:
            messagebox.showinfo("Resultado", f"Nota: {alumno['nota']}, Calificación: {alumno['calificacion']}")
            return
    messagebox.showerror("Error", "Alumno no encontrado.")

# Función para modificar la nota de un alumno
def nota():
    cedula = entry_cedula.get()
    try:
        nueva_nota = float(entry_nota.get())
        for alumno in alumnos:
            if alumno["cedula"] == cedula:
                alumno["nota"] = nueva_nota
                alumno["calificacion"] = calificacion(nueva_nota)
                messagebox.showinfo("Exito", "Nota modificada correctamente.")
                limpiar_campos()
                mostrar_alumnos()
                return
        messagebox.showerror("Error", "Alumno no encontrado.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese una nota valida.")

# Función para limpiar los campos de entrada
def limpiar_campos():
    entry_cedula.delete(0, tk.END)
    entry_apellidos.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_nota.delete(0, tk.END)

# Función para mostrar los suspensos
def suspendidos():
    text_resultado.delete(1.0, tk.END)
    if not any(alumno["nota"] < 5 for alumno in alumnos):
        text_resultado.insert(tk.END, "No hay alumnos suspensos.\n")
    else:
        text_resultado.insert(tk.END, "CEDULA\tAPELLIDOS\tNOMBRE\tNOTA\tCALIFICACION\n")
        for alumno in alumnos:
            if alumno["nota"] < 5:
                text_resultado.insert(tk.END, f"{alumno["cedula"]}\t{alumno["apellidos"]}\t{alumno["nombre"]}\t{alumno["nota"]}\t{alumno["calificacion"]}\n")

# Función para mostrar los aprobados
def aprobados():
    text_resultado.delete(1.0, tk.END)
    if not any(alumno["nota"] >= 5 for alumno in alumnos):
        text_resultado.insert(tk.END, "No hay alumnos aprobados.\n")
    else:
        text_resultado.insert(tk.END, "CEDULA\tAPELLIDOS\tNOMBRE\tNOTA\tCALIFICACION\n")
        for alumno in alumnos:
            if alumno["nota"] >= 5:
                text_resultado.insert(tk.END, f"{alumno["cedula"]}\t{alumno["apellidos"]}\t{alumno["nombre"]}\t{alumno["nota"]}\t{alumno["calificacion"]}\n")

# Función para mostrar los candidatos a matrícula de honor (MH)
def mostrar_mh():
    text_resultado.delete(1.0, tk.END)
    if not any(alumno["nota"] == 10 for alumno in alumnos):
        text_resultado.insert(tk.END, "No hay candidatos a matrícula de honor.\n")
    else:
        text_resultado.insert(tk.END, "CEDULA\tAPELLIDOS\tNOMBRE\tNOTA\tCALIFICACION\n")
        for alumno in alumnos:
            if alumno["nota"] == 10:
                text_resultado.insert(tk.END, f"{alumno["cedula"]}\t{alumno["apellidos"]}\t{alumno["nombre"]}\t{alumno["nota"]}\t{alumno["calificacion"]}\n")

# Ventana principal
root = tk.Tk()
root.title("Gestor de Alumnos")

# Crear los widgets
frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Cedula:").grid(row=0, column=0, padx=5, pady=5)
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

btn_eliminar = tk.Button(frame_buttons, text="2-Eliminar Alumno", command=eliminar_alumno, bg="#FFC0CB", fg="black")
btn_eliminar.grid(row=0, column=1, padx=5, pady=5)

btn_consultar = tk.Button(frame_buttons, text="3-Consultar Alumno", command=consultar_alumno, bg="#ADD8E6", fg="black")
btn_consultar.grid(row=0, column=2, padx=5, pady=5)

btn_modificar = tk.Button(frame_buttons, text="4-Modificar Nota", command=nota, bg="#FFFFE0", fg="black")
btn_modificar.grid(row=0, column=3, padx=5, pady=5)

btn_mostrar = tk.Button(frame_buttons, text="5-Mostrar Alumnos", command=mostrar_alumnos, bg="#FFFFE0", fg="black")
btn_mostrar.grid(row=0, column=4, padx=5, pady=5)

btn_suspensos = tk.Button(frame_buttons, text="6-Suspendidos", command=suspendidos, bg="#FF6347", fg="white")
btn_suspensos.grid(row=0, column=5, padx=5, pady=5)

btn_aprobados = tk.Button(frame_buttons, text="7-Aprobados", command=aprobados, bg="#90EE90", fg="black")
btn_aprobados.grid(row=0, column=6, padx=5, pady=5)

btn_mh = tk.Button(frame_buttons, text="8-Cuadro de Honor", command=mostrar_mh, bg="#FFD700", fg="black")
btn_mh.grid(row=0, column=7, padx=5, pady=5)

text_resultado = tk.Text(root, height=15, width=100)
text_resultado.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
