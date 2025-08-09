#Pacote nativos
import sys
import os
#pacotes terceiros
from PySide6.QtWidgets import *
#pacotes do projeto
from EstudePy import Ui_MainWindow
from db_sqlite import DB_connect

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Lista_Disciplina()

        geralpagebutton = [
            self.ui.GeralpushButton,
            self.ui.novdisciretornapushButton
        ]
        for but in geralpagebutton:
            but.clicked.connect(self.geral_page)
        discipagebutton = [
            self.ui.novnotaretornapushButton,
            self.ui.editnotaretornapushButton,
            self.ui.editdisciretornapushButton,
            self.ui.marcpresretornapushButton
        ]
        for but in discipagebutton:
            but.clicked.connect(self.disci_page)
        
        self.ui.novadiscipushButton.clicked.connect(self.novdisci_page)
        self.ui.discimarcaprespushButton.clicked.connect(self.marcpres_page)
        self.ui.discinovanotapushButton.clicked.connect(self.novnota_page)
        self.ui.discieditnotapushButton.clicked.connect(self.editnota_page)
        self.ui.discieditardidscipushButton.clicked.connect(self.editdisci_page)
        self.ui.novdiscisalvapushButton.clicked.connect(self.reg_nova_disciplina)

        daylist = ['Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sábado']
        self.ui.novdiscidiacomboBox.addItems(daylist)
        tipomedialist = ['Aritmética','Ponderada']
        self.ui.novdiscitipomediacomboBox.addItems(tipomedialist)

    
    def reg_nova_disciplina(self):
        disciplina = self.ui.novdiscinomelineEdit.text()
        carga = self.ui.novdiscicargahoraspinBox.value()
        horario = f'{self.ui.novdiscidiacomboBox.currentText()} {self.ui.novdiscihorariotimeEdit.time().toString('hh:mm')}'
        local = self.ui.novdiscilocallineEdit.text()
        tipomedia = self.ui.novdiscitipomediacomboBox.currentText()
        db.novaDisciplina(disciplina,tipomedia,carga,horario,local)
        self.disci_page()


    def geral_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def disci_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def novnota_page(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def novdisci_page(self):
        self.ui.stackedWidget.setCurrentIndex(3)
    
    def editnota_page(self):
        self.ui.stackedWidget.setCurrentIndex(4)
    
    def editdisci_page(self):
        self.ui.stackedWidget.setCurrentIndex(5)
    
    def marcpres_page(self):
        self.ui.stackedWidget.setCurrentIndex(6)


    def Lista_Disciplina(self):
        self.ui.listDiscicomboBox.clear()
        self.ui.listDiscicomboBox.addItem('Disciplinas...')
        #TODO disci_list a partir do banco de dados
        #self.ui.listDiscicomboBox.addItems(disci_list)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = DB_connect()
    db.iniciarBD()
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())