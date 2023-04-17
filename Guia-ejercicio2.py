# Importar la librería tkinter
import tkinter as tk

# Definir la función para invertir la palabra
def invertir_palabra():
    # Obtener la palabra ingresada en el cuadro de texto
    palabra = cuadro_texto.get()
    # Invertir la palabra utilizando slicing
    palabra_invertida = palabra[::-1]
    # Mostrar la palabra invertida en la etiqueta correspondiente
    etiqueta_palabra.config(text=palabra_invertida)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Invertir palabra")

# Crear las etiquetas, el cuadro de texto y el botón
etiqueta_ingreso = tk.Label(ventana, text="Ingrese una palabra:")
etiqueta_palabra = tk.Label(ventana, text="")
cuadro_texto = tk.Entry(ventana)
boton_invertir = tk.Button(ventana, text="Invertir", command=invertir_palabra)

# Añadir los elementos a la ventana principal
etiqueta_ingreso.pack(pady=10)
cuadro_texto.pack(pady=5)
boton_invertir.pack(pady=5)
etiqueta_palabra.pack(pady=10)

# Iniciar el loop de la ventana principal
ventana.mainloop()
