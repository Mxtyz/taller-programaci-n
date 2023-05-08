import sys
from PyQt6.QtWidgets import QWidget , QApplication , QLabel , QLineEdit , QPushButton 
from PyQt6.QtGui import QFont

class divisa(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializarui()
    
    def inicializarui(self):

        self.setGeometry(100,100,400,350)
        self.setWindowTitle("Ejercicio Taller Grupal")
        self.datos()
        self.show()

    def datos(self):
        self.texto = QLabel(self)
        self.texto.setText("Dolar Neozelandes vs shequel Israeli")
        self.texto.setFont(QFont("arial",30))
        self.texto.move(20,0)
        
        self.instrucciones = QLabel(self)
        self.instrucciones.setText("ingrese los datos del objeto")
        self.instrucciones.setFont(QFont("arial",10))
        self.instrucciones.move(20,50)

        self.dato = QLabel(self)
        self.dato.setText("dolar Neozelandes:\n"
                          "atributo 1\n"
                          "atributo 2\n"
                          "atributo 3\n")
        self.dato.move(10,80)

        self.dato1_input=QLineEdit(self)
        self.dato1_input.resize(250,15)
        self.dato1_input.move(100,100)

        self.dato2_input=QLineEdit(self)
        self.dato2_input.resize(250,15)
        self.dato2_input.move(100,115)

        self.dato3_input=QLineEdit(self)
        self.dato3_input.resize(250,15)
        self.dato3_input.move(100,130)

    def datos23(self):
        self.dato_ = QLabel(self)
        self.dato_.setText("Shequel Israeli:\n"
                          "atributo 1\n"
                          "atributo 2\n"
                          "atributo 3\n")
        self.dato.move(50,80)

        self.dato1__input=QLineEdit(self)
        self.dato1__input.resize(250,15)
        self.dato1__input.move(800,100)

        self.dato2__input=QLineEdit(self)
        self.dato2__input.resize(250,15)
        self.dato2__input.move(800,115)

        self.dato3__input=QLineEdit(self)
        self.dato3__input.resize(250,15)
        self.dato3__input.move(800,130)

       



        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = divisa()
    sys.exit(app.exec())


     

