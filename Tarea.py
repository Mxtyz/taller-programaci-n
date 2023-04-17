# Importar las librerías necesarias
import tkinter as tk
import random

# Definir la función para generar el número aleatorio
def generar_numero():
    numero = random.randint(1, 100) # Generar el número aleatorio
    etiqueta_numero.config(text=str(numero)) # Mostrar el número en la GUI

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de números aleatorios")

# Crear las etiquetas y el botón
etiqueta_instruccion = tk.Label(ventana, text="Presione el botón para generar un número aleatorio del 1 al 100")
etiqueta_numero = tk.Label(ventana, text="")
boton_generar = tk.Button(ventana, text="Generar número", command=generar_numero)

# Añadir los elementos a la ventana principal
etiqueta_instruccion.pack(pady=10)
boton_generar.pack(pady=10)
etiqueta_numero.pack(pady=10)

# Iniciar el loop de la ventana principal
ventana.mainloop()
