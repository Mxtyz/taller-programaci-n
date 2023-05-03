import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextBrowser

class MarvelWikiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Marvel Wiki App')
        self.setGeometry(100, 100, 600, 400)

        label_nombre = QLabel('Nombre del personaje:', self)
        label_nombre.move(10, 20)
        label_nombre.resize(200,20)

        self.input_nombre = QLineEdit(self)
        self.input_nombre.move(150, 20)
        self.input_nombre.resize(200, 20)

        btn_buscar = QPushButton('Buscar', self)
        btn_buscar.move(370, 20)
        btn_buscar.clicked.connect(self.buscar_personaje)

        self.text_resultado = QTextBrowser(self)
        self.text_resultado.move(20, 60)
        self.text_resultado.resize(550, 320)
        self.show()

    def buscar_personaje(self):
        url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/comic-characters/marvel-wikia-data.csv'
        df = pd.read_csv(url)

        nombre = self.input_nombre.text().strip()
        personaje = df[df['name'].str.lower() == nombre.lower()]

        if len(personaje) > 0:
            self.text_resultado.setText(f"Nombre: {personaje.iloc[0]['name']}\n"
                                         f"ID: {personaje.iloc[0]['page_id']}\n"
                                         f"URL: {personaje.iloc[0]['urlslug']}\n"
                                         f"Sexo: {personaje.iloc[0]['sex']}\n"
                                         f"Tipo de personaje: {personaje.iloc[0]['gsm']}\n"
                                         f"Alias: {personaje.iloc[0]['aliases']}\n"
                                         f"Apariciones: {personaje.iloc[0]['appearances']}\n"
                                         f"Año de primera aparición: {personaje.iloc[0]['first_appearance']}\n"
                                         f"Año de última aparición: {personaje.iloc[0]['last_appearance']}\n"
                                         f"Origen: {personaje.iloc[0]['origin']}\n"
                                         f"Organización: {personaje.iloc[0]['publisher']}\n"
                                         f"Vivo: {personaje.iloc[0]['alive']}")
        else:
            self.text_resultado.setText("El personaje no fue encontrado en la base de datos.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    marvel_wiki_app = MarvelWikiApp()
    sys.exit(app.exec())
