import sys
from PyQt6.QtWidgets import QApplication , QWidget , QLabel , QLineEdit , QPushButton , QMessageBox , QCheckBox     #QApplication sirve para realizar los eventos que ocurran en la ventana
from PyQt6.QtGui import QFont , QPixmap                                                                             #Qlabel sirve para mostrar texto o imagenes dentro de la ventana
                                                                                                                    #QWidget permite generar la ventana que tendra los componentes
class Login(QWidget):                                                                                               #QLineEdit permite ingresar informacion
                                                                                                                    #QPushButton permite generar botones en la app o ventana
    def __init__(self):                                                                                             #QMessageBox sirve para mostrar mensajes a traves de ventanas emergentes
        super().__init__()                                                                                          #QCheckBox sirve para ver el contenido de los Qlabel
        self.inicializarui()                                                                                        #QPixmap sirve para agregar imagenes

    def inicializarui(self):
        self.setGeometry(100,100,350,250)
        self.setWindowTitle("login")
        self.informacion()
        self.show()

    def informacion(self):

        self.is_logged = False     #is_logged hace que el usuario inicie como que no esta ingresado

        user_label = QLabel(self)              #crea un label
        user_label.setText("Usuario:")
        user_label.setFont(QFont("Arial",10))  #setFont(QFont()) sirve para agregar un estilo de texto y tamaño de letra
        user_label.move(20,54)                 #move indica la posicion del label
        
        self.user_input = QLineEdit(self)           #QLineEdit() permite al usuario escribir su informacion
        self.user_input.resize(250,24)              #resixe permite agrandar o achicar el lugar donde va la informacio
        self.user_input.move(90,50)

        password_label = QLabel(self)              
        password_label.setText("Password:")
        password_label.setFont(QFont("Arial",10))  
        password_label.move(20,86)                 
        
        self.password_input = QLineEdit(self)           
        self.password_input.resize(250,24)              
        self.password_input.move(90,82)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)   #setEchoMode(QLineEdit.EchoMode.password)permite escrivir la contraseña de manera oculta(mas segura)

        self.check_ver_contraseña = QCheckBox(self)
        self.check_ver_contraseña.setText("ver contraseña")
        self.check_ver_contraseña.move(90,110)
        self.check_ver_contraseña.clicked.connect(self.mostrarcontraseña)

        ingresar_button = QPushButton(self)    #QPushButton permite generar botones
        ingresar_button.setText("ingresa")
        ingresar_button.resize(320,24)
        ingresar_button.move(20,140)
        ingresar_button.clicked.connect(self.iniciarventanaprincipal)

        registarse_button = QPushButton(self)    
        registarse_button.setText("registrate")
        registarse_button.resize(320,24)
        registarse_button.move(20,180)
        registarse_button.clicked.connect(self.iniciarventanaderegistro)

    def mostrarcontraseña(self):
        pass

    def iniciarventanaprincipal(self):
        pass

    def iniciarventanaderegistro(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Login()       #login es el objeto
    sys.exit(app.exec())
