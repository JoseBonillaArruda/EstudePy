#Pacote nativos
import sys
import os
#pacotes terceiros
from PySide6.QtWidgets import *
#pacotes do projeto
from EstudePy import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Lista_Disciplina()
        self.ui.GeralpushButton.clicked.connect(self.geral_page)
        self.ui.novadiscipushButton.clicked.connect(self.novdisci_page)


    
    def geral_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)


    def novdisci_page(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    
    def retornar(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    

    def Lista_Disciplina(self):
        self.ui.listDiscicomboBox.clear()
        self.ui.listDiscicomboBox.addItem('Disciplinas...')
        #TODO disci_list a partir do banco de dados
        #self.ui.listDiscicomboBox.addItems(disci_list)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())