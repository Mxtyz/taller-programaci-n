import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QDialog, QLineEdit

class Objeto:
    def __init__(self, nombre, valor1, valor2):
        self.nombre = nombre
        self.valor1 = valor1
        self.valor2 = valor2
    
    def calcular_valor(self):
        return self.valor1 * self.valor2

class IngresoDatosDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.nombre_edit = QLineEdit()
        self.valor1_edit = QLineEdit()
        self.valor2_edit = QLineEdit()
        
        guardar_button = QPushButton("Guardar")
        guardar_button.clicked.connect(self.guardar)
        
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Ingrese los datos del objeto"))
        layout.addWidget(QLabel("Nombre:"))
        layout.addWidget(self.nombre_edit)
        layout.addWidget(QLabel("Valor 1:"))
        layout.addWidget(self.valor1_edit)
        layout.addWidget(QLabel("Valor 2:"))
        layout.addWidget(self.valor2_edit)
        layout.addWidget(guardar_button)
        
        self.setLayout(layout)
        
    def guardar(self):
        self.accept()

class ComparacionWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.izquierda_obj = None
        self.derecha_obj = None
        
        self.izquierda_label = QLabel("Objeto Izquierda")
        self.derecha_label = QLabel("Objeto Derecha")
        self.comparacion_label = QLabel()
        
        agregar_izq_button = QPushButton("Agregar Datos")
        agregar_izq_button.clicked.connect(self.agregar_datos_izquierda)
        agregar_der_button = QPushButton("Agregar Datos")
        agregar_der_button.clicked.connect(self.agregar_datos_derecha)
        comparar_button = QPushButton("Comparar")
        comparar_button.clicked.connect(self.comparar)
        
        izquierda_layout = QVBoxLayout()
        izquierda_layout.addWidget(self.izquierda_label)
        izquierda_layout.addWidget(agregar_izq_button)
        derecha_layout = QVBoxLayout()
        derecha_layout.addWidget(self.derecha_label)
        derecha_layout.addWidget(agregar_der_button)
        comparacion_layout = QHBoxLayout()
        comparacion_layout.addLayout(izquierda_layout)
        comparacion_layout.addWidget(self.comparacion_label)
        comparacion_layout.addLayout(derecha_layout)
        
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Bienvenido a la aplicación de comparación de objetos"))
        layout.addWidget(QLabel("Ingrese los datos de los dos objetos y haga clic en 'Comparar'"))
        layout.addLayout(comparacion_layout)
        layout.addWidget(comparar_button)
        
        self.setLayout(layout)
        
    def agregar_datos_izquierda(self):
        dialog = IngresoDatosDialog(self)
        dialog.setWindowTitle("Agregar Datos - Objeto Izquierda")
        if dialog.exec() == QDialog.Accepted:
            nombre  = dialog.nombre_edit.text()


if __name__ == "__main__":
    app = QApplication([])
    ventana = ComparacionWidget()
    sys.exit(app.exec())

