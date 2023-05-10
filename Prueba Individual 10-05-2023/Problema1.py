import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QWidget

class Interfaz(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bienvenido")
        self.setGeometry(100, 100, 800, 400)
        layout = QHBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        left_layout = QVBoxLayout()
        username_label = QLabel("Nombre de usuario:")
        left_layout.addWidget(username_label)
        username_input = QLineEdit()
        left_layout.addWidget(username_input)
        
        image_label = QLabel("Imagen")
        left_layout.addWidget(image_label)
        
        description_label = QLabel("Descripción del usuario:")
        left_layout.addWidget(description_label)
        
        description_text = QTextEdit()
        left_layout.addWidget(description_text)
        layout.addLayout(left_layout)
        right_layout = QVBoxLayout()
        
        atributos = ["Atributo 1:", "Atributo 2:", "Atributo 3:", "Atributo 4:", "Atributo 5:", "Atributo 6:"]
        valores = ["Valor 1", "Valor 2", "Valor 3", "Valor 4", "Valor 5", "Valor 6"]
        
        for attribute, values in zip(atributos, valores):
            attribute_label = QLabel(attribute)
            right_layout.addWidget(attribute_label)
            value_input = QLineEdit()
            right_layout.addWidget(value_input)
        
        layout.addLayout(right_layout) 
        button = QPushButton("Aceptar")
        layout.addWidget(button)
        button.clicked.connect(self.on_button_clicked)
    
    def on_button_clicked(self):
        print("¡Botón clickeado!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Interfaz()
    ventana.show()
    sys.exit(app.exec())
