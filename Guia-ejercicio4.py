# Importar la librería tkinter
import tkinter as tk

# Definir la función para verificar si un número es primo
def es_primo(n):
    # Verificar si el número es menor que 2 (no es primo)
    if n < 2:
        return False
    # Verificar si el número es divisible por algún número entre 2 y n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    # Si no se encontró ningún divisor, el número es primo
    return True

# Definir la función para verificar si el número ingresado es primo
def verificar_primo():
    # Obtener el número ingresado en el cuadro de texto
    numero = int(cuadro_texto.get())
    # Verificar si el número es primo utilizando la función es_primo()
    if es_primo(numero):
        etiqueta_primo.config(text=str(numero) + " es primo")
    else:
        etiqueta_primo.config(text=str(numero) + " no es primo")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Verificar si un número es primo")

# Crear las etiquetas, el cuadro de texto y el botón
etiqueta_ingreso = tk.Label(ventana, text="Ingrese un número:")
etiqueta_primo = tk.Label(ventana, text="")
cuadro_texto = tk.Entry(ventana)
boton_verificar = tk.Button(ventana, text="Verificar", command=verificar_primo)

# Añadir los elementos a la ventana principal
etiqueta_ingreso.pack(pady=10)
cuadro_texto.pack(pady=5)
boton_verificar.pack(pady=5)
etiqueta_primo.pack(pady=10)

# Iniciar el loop de la ventana principal
ventana.mainloop()
