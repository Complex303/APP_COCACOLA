import tkinter as tk
from tkcalendar import Calendar

def mostrar_fecha():
    fecha_seleccionada = calendario.get_date()
    label_fecha.config(text=f"Fecha seleccionada: {fecha_seleccionada}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Seleccionar Fecha")
ventana.geometry("400x400")

# Crear el calendario
calendario = Calendar(ventana, selectmode='day', year=2024, month=8, day=15)
calendario.pack(pady=20)

# Crear un botón para obtener la fecha seleccionada
btn_mostrar_fecha = tk.Button(ventana, text="Mostrar Fecha", command=mostrar_fecha)
btn_mostrar_fecha.pack(pady=10)

# Crear una etiqueta para mostrar la fecha seleccionada
label_fecha = tk.Label(ventana, text="")
label_fecha.pack(pady=10)

# Ejecutar la ventana principal
ventana.mainloop()
