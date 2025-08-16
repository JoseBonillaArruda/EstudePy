#Pacote nativos
import sys
import os
#pacotes terceiros
from PySide6.QtWidgets import *
from PySide6.QtCore import QTime
#pacotes do projeto
from EstudePy import Ui_MainWindow
from db_sqlite import DB_connect

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Lista_Disciplina()
        self.lista_ID = db.listarDisciplinas()
        self.disci_id_atual = 0
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
        self.ui.listDiscicomboBox.currentIndexChanged.connect(self.disci_page)
        self.ui.marcpressalvapushButton.clicked.connect(self.MarcarPresenca)
        self.ui.editdiscisalvapushButton.clicked.connect(self.EditarDisciplina)
        self.ui.novnotasalvapushButton.clicked.connect(self.addNotas)
        self.ui.editnotsalvapushButton.clicked.connect(self.EditarNota)
        self.ui.editnotadeletepushButton.clicked.connect(self.RemoverNota)

        daylist = ['Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sábado']
        self.ui.novdiscidiacomboBox.addItems(daylist)
        self.ui.editdiscidiacomboBox.addItems(daylist)
        tipomedialist = ['Aritmética','Ponderada']
        self.ui.novdiscitipomediacomboBox.addItems(tipomedialist)
        self.ui.editdiscitipomediacomboBox.addItems(tipomedialist)
        self.geral_page()

    
    def reg_nova_disciplina(self):
        disciplina = self.ui.novdiscinomelineEdit.text()
        carga = self.ui.novdiscicargahoraspinBox.value()
        horario = f'{self.ui.novdiscidiacomboBox.currentText()} {self.ui.novdiscihorariotimeEdit.time().toString('hh:mm')}'
        local = self.ui.novdiscilocallineEdit.text()
        tipomedia = self.ui.novdiscitipomediacomboBox.currentText()
        db.novaDisciplina(disciplina,tipomedia,carga,horario,local)
        self.Lista_Disciplina()
        self.lista_ID = db.listarDisciplinas()
        self.ui.listDiscicomboBox.setCurrentIndex(self.ui.listDiscicomboBox.count() - 1)
        self.disci_id_atual = self.lista_ID[self.ui.listDiscicomboBox.currentIndex()-1][0]


    def geral_page(self):
        self.ui.listDiscicomboBox.setCurrentIndex(0)
        disci = []
        for i in range(self.ui.listDiscicomboBox.count()):
            disci.append(db.getDisciplinaPorId(i))
        disci.pop(0)
        num_disci = sum(isinstance(item, dict) for item in disci)
        self.ui.geraldiscitableWidget.setRowCount(num_disci)
        self.ui.geraldiscitableWidget.setColumnCount(8)
        self.ui.geraldiscitableWidget.setHorizontalHeaderLabels(['ID', 'Disciplina', 'Média', 'Tipo Média', 'Carga Horária', 'Qtd Presença', 'Local', 'Horário'])
        keylist = ['id', 'disciplina', 'media', 'tipo_media', 'carga_horaria', 'qtd_presenca', 'local', 'horario']
        for i in range(num_disci):
            for j in range(8):
                item = QTableWidgetItem(str(disci[i].get(keylist[j])))
                self.ui.geraldiscitableWidget.setItem(i, j, item)
        self.ui.stackedWidget.setCurrentIndex(0)

    def disci_page(self):
        self.disci_id_atual = self.lista_ID[self.ui.listDiscicomboBox.currentIndex()-1][0]
        disci = db.getDisciplinaPorId(self.disci_id_atual)
        disci_pres = [disci.get('carga_horaria'),disci.get('qtd_presenca'),f'{(disci.get('qtd_presenca')/disci.get('carga_horaria')*100):.2f}%']
        self.ui.discipresencatableWidget.setRowCount(1)
        self.ui.discipresencatableWidget.setColumnCount(3)
        self.ui.discipresencatableWidget.setVerticalHeaderLabels([''])
        self.ui.discipresencatableWidget.setHorizontalHeaderLabels(['Carga Horária', 'Presenças', 'Precentual'])
        for i in range(3):
            item = QTableWidgetItem(str(disci_pres[i]))
            self.ui.discipresencatableWidget.setItem(0, i, item)

        disci_notas = db.getNotasPorId(self.disci_id_atual)
        num_notas = sum(isinstance(item, tuple) for item in disci_notas)
        if disci['tipo_media'] == 'Aritmética':
            media = sum(disci_notas[i][2] for i in range(num_notas)) / num_notas if num_notas > 0 else 0
        elif disci['tipo_media'] == 'Ponderada':
            total_peso = sum(disci_notas[i][3] for i in range(num_notas))
            if total_peso > 0:
                media = sum(disci_notas[i][2] * disci_notas[i][3] for i in range(num_notas)) / total_peso
            else:
                media = 0
        db.RegMedia(self.disci_id_atual,media)
        self.ui.discinotatableWidget.setRowCount(num_notas+1)
        self.ui.discinotatableWidget.setColumnCount(2)
        self.ui.discinotatableWidget.setHorizontalHeaderLabels(['Nota', 'Peso'])
        for i in range(num_notas):
            for j in range(2):
                item = QTableWidgetItem(str(disci_notas[i][j+2]))
                self.ui.discinotatableWidget.setItem(i, j, item)
        
        self.ui.discinotatableWidget.setItem(num_notas, 0, QTableWidgetItem('Média'))
        self.ui.discinotatableWidget.setItem(num_notas, 1, QTableWidgetItem(str(f'{media:.2f}')))
        disci_info = [disci.get('disciplina'),disci.get('horario'),disci.get('local')]
        self.ui.discihorariotableWidget.setRowCount(1)
        self.ui.discihorariotableWidget.setColumnCount(3)
        self.ui.discihorariotableWidget.setHorizontalHeaderLabels(['Disciplina', 'Horário', 'Local'])
        for j in range(3):
            item = QTableWidgetItem(str(disci_info[j]))
            self.ui.discihorariotableWidget.setItem(0, j, item)
        self.ui.stackedWidget.setCurrentIndex(1)

    def novnota_page(self):
        disci_notas = db.getNotasPorId(self.disci_id_atual)
        num_notas = sum(isinstance(item, tuple) for item in disci_notas)
        self.ui.novnotatableWidget.setRowCount(num_notas)
        self.ui.novnotatableWidget.setColumnCount(2)
        self.ui.novnotatableWidget.setHorizontalHeaderLabels(['Nota', 'Peso'])
        for i in range(num_notas):
            for j in range(2):
                item = QTableWidgetItem(str(disci_notas[i][j+2]))
                self.ui.novnotatableWidget.setItem(i, j, item)
        
        self.ui.stackedWidget.setCurrentIndex(2)

    def novdisci_page(self):
        disci = []
        for i in range(self.ui.listDiscicomboBox.count()):
            disci.append(db.getDisciplinaPorId(i))
        disci.pop(0)
        num_disci = sum(isinstance(item, dict) for item in disci)
        self.ui.novdiscitableWidget.setRowCount(num_disci)
        self.ui.novdiscitableWidget.setColumnCount(8)
        self.ui.novdiscitableWidget.setHorizontalHeaderLabels(['ID', 'Disciplina', 'Média', 'Tipo Média', 'Carga Horária', 'Qtd Presença', 'Local', 'Horário'])
        keylist = ['id', 'disciplina', 'media', 'tipo_media', 'carga_horaria', 'qtd_presenca', 'local', 'horario']
        for i in range(num_disci):
            for j in range(8):
                item = QTableWidgetItem(str(disci[i].get(keylist[j])))
                self.ui.novdiscitableWidget.setItem(i, j, item)

        self.ui.stackedWidget.setCurrentIndex(3)
    
    def editnota_page(self):
        disci_notas = db.getNotasPorId(self.disci_id_atual)
        num_notas = sum(isinstance(item, tuple) for item in disci_notas)
        notas_id =[str(disci_notas[i][0]) for i in range(num_notas)]
        self.ui.editnotatableWidget.setRowCount(num_notas)
        self.ui.editnotatableWidget.setColumnCount(3)
        self.ui.editnotatableWidget.setHorizontalHeaderLabels(['ID','Nota', 'Peso'])
        for i in range(num_notas):
            for j in range(3):
                if j== 0:
                    item = QTableWidgetItem(str(disci_notas[i][0]))
                else:
                    item = QTableWidgetItem(str(disci_notas[i][j+1]))
                self.ui.editnotatableWidget.setItem(i, j, item)
        self.ui.editnotaselectcomboBox.clear()
        self.ui.editnotaselectcomboBox.addItem('Notas...')
        self.ui.editnotaselectcomboBox.addItems(notas_id)

        self.ui.stackedWidget.setCurrentIndex(4)
    
    def editdisci_page(self):
        disci = db.getDisciplinaPorId(self.disci_id_atual)
        self.ui.editdiscitableWidget.setRowCount(1)
        self.ui.editdiscitableWidget.setColumnCount(8)
        self.ui.editdiscitableWidget.setHorizontalHeaderLabels(['ID', 'Disciplina', 'Média', 'Tipo Média', 'Carga Horária', 'Qtd Presença', 'Local', 'Horário'])
        keylist = ['id', 'disciplina', 'media', 'tipo_media', 'carga_horaria', 'qtd_presenca', 'local', 'horario']
        for j in range(8):
            item = QTableWidgetItem(str(disci.get(keylist[j])))
            self.ui.editdiscitableWidget.setItem(0, j, item)
            self.ui.editdiscicargahoraspinBox_4.setValue(disci['carga_horaria'])

        self.ui.editdiscinomelineEdit.setText(disci['disciplina'])
        self.ui.editdiscilocallineEdit.setText(disci['local'])
        self.ui.editdiscitipomediacomboBox.setCurrentText(disci['tipo_media'])
        dia, hora = disci['horario'].split(' ')
        self.ui.editdiscidiacomboBox.setCurrentText(dia)
        self.ui.editdiscihorariotimeEdit.setTime(QTime.fromString(hora, 'hh:mm'))
        
    
        self.ui.stackedWidget.setCurrentIndex(5)


    def marcpres_page(self):
        disci = db.getDisciplinaPorId(self.disci_id_atual)
        disci_pres = [disci.get('carga_horaria'),disci.get('qtd_presenca'),f'{(disci.get('qtd_presenca')/disci.get('carga_horaria')*100):.2f}%']
        self.ui.marcprestableWidget.setRowCount(1)
        self.ui.marcprestableWidget.setColumnCount(3)
        self.ui.marcprestableWidget.setHorizontalHeaderLabels(['Carga Horária', 'Presenças', 'Precentual'])
        for j in range(3):
            item = QTableWidgetItem(str(disci_pres[j]))
            self.ui.marcprestableWidget.setItem(0, j, item)
        self.ui.marcpresspinBox.setMaximum(disci.get('carga_horaria') - disci.get('qtd_presenca'))
        self.ui.marcpresspinBox.setMinimum(-disci.get('qtd_presenca'))
        self.ui.stackedWidget.setCurrentIndex(6)


    def Lista_Disciplina(self):
        self.ui.listDiscicomboBox.clear()
        self.ui.listDiscicomboBox.addItem('Disciplinas...')
        disciplinas = db.listarDisciplinas()
        for disciplina in disciplinas:
            self.ui.listDiscicomboBox.addItem(f"{disciplina[0]} - {disciplina[1]}")
    

    def MarcarPresenca(self):
        disciplina_id = self.disci_id_atual
        qtd_presenca = self.ui.marcpresspinBox.value()
        db.marcarPresenca(disciplina_id,qtd_presenca)
        self.disci_page()
    

    def EditarDisciplina(self):
        disciNome = self.ui.editdiscinomelineEdit.text()
        carga = self.ui.editdiscicargahoraspinBox_4.value()
        presenca = self.ui.editdiscipresencaspinBox.value()
        tipo_media = self.ui.editdiscitipomediacomboBox.currentText()
        local = self.ui.editdiscilocallineEdit.text()
        horario = f'{self.ui.editdiscidiacomboBox.currentText()} {self.ui.editdiscihorariotimeEdit.text()}'
        db.editarDisciplina(self.disci_id_atual, disciNome, tipo_media, carga, presenca, local, horario)
        self.disci_page()
    

    def addNotas(self):
        nota = self.ui.novnotadoubleSpinBox.value()
        peso = self.ui.novnotapesospinBox.value()
        db.addNotas(self.disci_id_atual, nota, peso)
        self.disci_page()
    

    def EditarNota(self):
        nota = self.ui.editnotadoubleSpinBox.value()
        peso = self.ui.editnotaspinBox.value()
        nota_id = int(self.ui.editnotaselectcomboBox.currentText())
        db.editarNota(nota_id, nota, peso)
        self.editnota_page()
    

    def RemoverNota(self):
        nota_id = int(self.ui.editnotaselectcomboBox.currentText())
        db.removerNota(nota_id)
        self.editnota_page()


    def ApagarDisciplina(self, ID):
        db.removerDisciplina(ID)
        self.geral_page()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = DB_connect()
    db.iniciarBD()
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())