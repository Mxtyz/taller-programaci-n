import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget
from VentanaSecundaria import VentanaSecundaria
from mascota import Mascota

class VentanaP(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Principal")
        
        layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        self.nombre_input = QLineEdit()
        layout.addWidget(QLabel("Nombre:"))
        layout.addWidget(self.nombre_input)
        
        self.especie_input = QLineEdit()
        layout.addWidget(QLabel("Especie:"))
        layout.addWidget(self.especie_input)
        
        self.edad_input = QLineEdit()
        layout.addWidget(QLabel("Edad:"))
        layout.addWidget(self.edad_input)
        
        self.peso_input = QLineEdit()
        layout.addWidget(QLabel("Peso:"))
        layout.addWidget(self.peso_input)
        
        guardar_button = QPushButton("Guardar Mascota")
        layout.addWidget(guardar_button)
        guardar_button.clicked.connect(self.guardar_mascota)
    
    def guardar_mascota(self):
        nombre = self.nombre_input.text()
        especie = self.especie_input.text()
        edad = int(self.edad_input.text())
        peso = float(self.peso_input.text())
        
        mascota = Mascota(nombre, especie, edad, peso)
        
        ventana_secundaria = VentanaSecundaria(mascota)
        ventana_secundaria.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_principal = VentanaP()
    ventana_principal.show()
    sys.exit(app.exec())
