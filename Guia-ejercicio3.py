# Importar la librería tkinter
import tkinter as tk

# Definir la función para contar las letras de la palabra
def contar_letras():
    # Obtener la palabra ingresada en el cuadro de texto
    palabra = cuadro_texto.get()
    # Contar la cantidad de letras de la palabra
    cantidad_letras = len(palabra)
    # Mostrar la cantidad de letras en la etiqueta correspondiente
    etiqueta_cantidad.config(text="La palabra tiene " + str(cantidad_letras) + " letras")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Contar letras de palabra")

# Crear las etiquetas, el cuadro de texto y el botón
etiqueta_ingreso = tk.Label(ventana, text="Ingrese una palabra:")
etiqueta_cantidad = tk.Label(ventana, text="")
cuadro_texto = tk.Entry(ventana)
boton_contar = tk.Button(ventana, text="Contar letras", command=contar_letras)

# Añadir los elementos a la ventana principal
etiqueta_ingreso.pack(pady=10)
cuadro_texto.pack(pady=5)
boton_contar.pack(pady=5)
etiqueta_cantidad.pack(pady=10)

# Iniciar el loop de la ventana principal
ventana.mainloop()
