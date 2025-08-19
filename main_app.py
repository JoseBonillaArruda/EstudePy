#Pacote nativos
import sys
#pacotes terceiros
from PySide6.QtWidgets import *
from PySide6.QtCore import QTime
#pacotes do projeto
from EstudePy import Ui_MainWindow
from db_sqlite import DB_connect


#classe principal da interface
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Lista_Disciplina() # listagem das disciplinas
        self.lista_ID = db.listarDisciplinas() # listagem dos IDs das disciplinas
        self.disci_id_atual = 0 #variável para armazenar o ID da disciplina atual 
        db.novaAnotacao(self.disci_id_atual, 'ESTUDEPY - Anotações') # registro da nota geral no banco de dados
        geralpagebutton = [ # botões que retornam a página geral
            self.ui.GeralpushButton,
            self.ui.novdisciretornapushButton
        ]
        for but in geralpagebutton:
            but.clicked.connect(self.geral_page)
        discipagebutton = [ # botões que retornam a página de disciplina
            self.ui.novnotaretornapushButton,
            self.ui.editnotaretornapushButton,
            self.ui.editdisciretornapushButton,
            self.ui.marcpresretornapushButton
        ]
        for but in discipagebutton:
            but.clicked.connect(self.disci_page)
        
        # Conexão dos botões com as funções
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
        self.ui.editdiscideletepushButton.clicked.connect(self.ApagarDisciplina)
        self.ui.geralanotapushButton.clicked.connect(self.SalvarAnotacao)
        self.ui.discianotapushButton.clicked.connect(self.SalvarAnotacao)

        daylist = ['Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sábado'] # lista de dias da semana para preenchimento dos campos de horário
        self.ui.novdiscidiacomboBox.addItems(daylist)
        self.ui.editdiscidiacomboBox.addItems(daylist)
        tipomedialist = ['Aritmética','Ponderada'] # lista de tipos de média para preenchimento dos campos de tipo de média
        self.ui.novdiscitipomediacomboBox.addItems(tipomedialist)
        self.ui.editdiscitipomediacomboBox.addItems(tipomedialist)
        self.geral_page() # chamada da função que exibe a página geral ao iniciar o programa

    #registro de nova disciplina
    def reg_nova_disciplina(self):
        #coleta os dados do formulário de nova disciplina
        disciplina = self.ui.novdiscinomelineEdit.text()
        carga = self.ui.novdiscicargahoraspinBox.value()
        horario = f"{self.ui.novdiscidiacomboBox.currentText()} {self.ui.novdiscihorariotimeEdit.time().toString('hh:mm')}"
        local = self.ui.novdiscilocallineEdit.text()
        tipomedia = self.ui.novdiscitipomediacomboBox.currentText()
        db.novaDisciplina(disciplina,tipomedia,carga,horario,local) #envio ao banco de dados
        self.Lista_Disciplina() #atualização da lista de disciplinas
        self.lista_ID = db.listarDisciplinas() #atualização da lista de IDs das disciplinas
        db.novaAnotacao(self.lista_ID[-1][0], 'ESTUDEPY - Anotações') #criação de nova anotação para a disciplina recém criada
        self.ui.listDiscicomboBox.setCurrentIndex(self.ui.listDiscicomboBox.count() - 1) # seleciona a disciplina recém criada na lista de disciplinas, muda a pagina para a disciplina e exibe as informações dela


    #função da pagina geral
    def geral_page(self):
        self.ui.listDiscicomboBox.setCurrentIndex(0) # seleciona o índice 0 da lista de disciplinas
        self.disci_id_atual = 0 #ID 0 é o ID geral
        disci = [] #coleta das disciplinas do banco de dados para visualização em tabela
        for i in range(self.ui.listDiscicomboBox.count()-1):
            disci.append(db.getDisciplinaPorId(self.lista_ID[i][0]))
        num_disci = sum(isinstance(item, dict) for item in disci)
        self.ui.geraldiscitableWidget.setRowCount(num_disci)
        self.ui.geraldiscitableWidget.setColumnCount(8)
        self.ui.geraldiscitableWidget.setHorizontalHeaderLabels(['ID', 'Disciplina', 'Média', 'Tipo Média', 'Carga Horária', 'Qtd Presença', 'Local', 'Horário'])
        keylist = ['id', 'disciplina', 'media', 'tipo_media', 'carga_horaria', 'qtd_presenca', 'local', 'horario']
        for i in range(num_disci):
            for j in range(8):
                item = QTableWidgetItem(str(disci[i].get(keylist[j])))
                self.ui.geraldiscitableWidget.setItem(i, j, item)
        self.Anotacao(self.ui.geralanotatextBrowser) #chamada da função que exibe as anotações gerais
        self.ui.stackedWidget.setCurrentIndex(0)


    #função da página de disciplina
    def disci_page(self):
        #index 0 nos retorna a pagina geral
        if self.ui.listDiscicomboBox.currentIndex() == 0:
            self.geral_page()
        else:
            self.disci_id_atual = self.lista_ID[self.ui.listDiscicomboBox.currentIndex()-1][0] #coleta do ID da disciplina
            disci = db.getDisciplinaPorId(self.disci_id_atual) #coleta das informações da disciplina
            disci_pres = [disci.get('carga_horaria'),disci.get('qtd_presenca'),f"{(disci.get('qtd_presenca')/disci.get('carga_horaria')*100):.2f}%"] #coleta das informações de presença da disciplina e calculo do percentual de presença
            self.ui.discipresencatableWidget.setRowCount(1) #configuração da tabela de presença
            self.ui.discipresencatableWidget.setColumnCount(3)
            self.ui.discipresencatableWidget.setVerticalHeaderLabels([''])
            self.ui.discipresencatableWidget.setHorizontalHeaderLabels(['Carga Horária', 'Presenças', 'Precentual'])
            for i in range(3):
                item = QTableWidgetItem(str(disci_pres[i]))
                self.ui.discipresencatableWidget.setItem(0, i, item)

            disci_notas = db.getNotasPorId(self.disci_id_atual) #coleta das notas da disciplina
            num_notas = sum(isinstance(item, tuple) for item in disci_notas) # contagem do número de notas
            if disci['tipo_media'] == 'Aritmética': #calculos da média aritmética ou ponderada
                media = sum(disci_notas[i][2] for i in range(num_notas)) / num_notas if num_notas > 0 else 0
            elif disci['tipo_media'] == 'Ponderada':
                total_peso = sum(disci_notas[i][3] for i in range(num_notas))
                if total_peso > 0:
                    media = sum(disci_notas[i][2] * disci_notas[i][3] for i in range(num_notas)) / total_peso
                else:
                    media = 0
            db.RegMedia(self.disci_id_atual,media) #registro da média da disciplina no banco de dados
            
            self.ui.discinotatableWidget.setRowCount(num_notas+1) #configuração da tabela de notas
            self.ui.discinotatableWidget.setColumnCount(2)
            self.ui.discinotatableWidget.setHorizontalHeaderLabels(['Nota', 'Peso'])
            for i in range(num_notas):
                for j in range(2):
                    item = QTableWidgetItem(str(disci_notas[i][j+2]))
                    self.ui.discinotatableWidget.setItem(i, j, item)
            self.ui.discinotatableWidget.setItem(num_notas, 0, QTableWidgetItem('Média'))
            self.ui.discinotatableWidget.setItem(num_notas, 1, QTableWidgetItem(str(f'{media:.2f}')))
            
            disci_info = [disci.get('disciplina'),disci.get('horario'),disci.get('local')] #coleta das informações da disciplina para exibição
            self.ui.discihorariotableWidget.setRowCount(1) #configuração da tabela de informações
            self.ui.discihorariotableWidget.setColumnCount(3)
            self.ui.discihorariotableWidget.setHorizontalHeaderLabels(['Disciplina', 'Horário', 'Local'])
            for j in range(3):
                item = QTableWidgetItem(str(disci_info[j]))
                self.ui.discihorariotableWidget.setItem(0, j, item)
            self.Anotacao(self.ui.discianotatextBrowser) #exibição das anotações da disciplina
            self.ui.stackedWidget.setCurrentIndex(1) # muda para a página da disciplina

        
    #função que exibe a página de nova nota
    def novnota_page(self):
        disci_notas = db.getNotasPorId(self.disci_id_atual) #coleta das notas da disciplina atual
        num_notas = sum(isinstance(item, tuple) for item in disci_notas) # contagem do número de notas
        self.ui.novnotatableWidget.setRowCount(num_notas) #configuração da tabela de notas
        self.ui.novnotatableWidget.setColumnCount(2)
        self.ui.novnotatableWidget.setHorizontalHeaderLabels(['Nota', 'Peso'])
        for i in range(num_notas):
            for j in range(2):
                item = QTableWidgetItem(str(disci_notas[i][j+2]))
                self.ui.novnotatableWidget.setItem(i, j, item)
        
        self.ui.stackedWidget.setCurrentIndex(2) # muda para a página de nova nota


    #função que exibe a página de nova disciplina
    def novdisci_page(self):
        disci = [] #coleta das disciplinas do banco de dados para visualização em tabela
        for i in range(self.ui.listDiscicomboBox.count()-1): #configuração da tabela de disciplinas
            disci.append(db.getDisciplinaPorId(self.lista_ID[i][0]))
        num_disci = sum(isinstance(item, dict) for item in disci)
        self.ui.novdiscitableWidget.setRowCount(num_disci)
        self.ui.novdiscitableWidget.setColumnCount(8)
        self.ui.novdiscitableWidget.setHorizontalHeaderLabels(['ID', 'Disciplina', 'Média', 'Tipo Média', 'Carga Horária', 'Qtd Presença', 'Local', 'Horário'])
        keylist = ['id', 'disciplina', 'media', 'tipo_media', 'carga_horaria', 'qtd_presenca', 'local', 'horario']
        for i in range(num_disci):
            for j in range(8):
                item = QTableWidgetItem(str(disci[i].get(keylist[j])))
                self.ui.novdiscitableWidget.setItem(i, j, item)
        self.ui.novdiscicargahoraspinBox.setMinimum(1)

        self.ui.stackedWidget.setCurrentIndex(3) # muda para a página de nova disciplina
    
    
    #função que exibe a página de edição de notas
    def editnota_page(self):
        disci_notas = db.getNotasPorId(self.disci_id_atual) #coleta das notas da disciplina atual
        num_notas = sum(isinstance(item, tuple) for item in disci_notas) #configuração da tabela de notas
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
        self.ui.editnotaselectcomboBox.clear()# configuração do combo box de seleção de notas
        self.ui.editnotaselectcomboBox.addItem('Notas...')
        self.ui.editnotaselectcomboBox.addItems(notas_id)

        self.ui.stackedWidget.setCurrentIndex(4) # muda para a página de edição de notas
    
    
    #função que exibe a página de edição de disciplina
    def editdisci_page(self):
        disci = db.getDisciplinaPorId(self.disci_id_atual) #coleta das informações da disciplina atual
        self.ui.editdiscitableWidget.setRowCount(1) # configuração da tabela de disciplina
        self.ui.editdiscitableWidget.setColumnCount(8)
        self.ui.editdiscitableWidget.setHorizontalHeaderLabels(['ID', 'Disciplina', 'Média', 'Tipo Média', 'Carga Horária', 'Qtd Presença', 'Local', 'Horário'])
        keylist = ['id', 'disciplina', 'media', 'tipo_media', 'carga_horaria', 'qtd_presenca', 'local', 'horario']
        for j in range(8):
            item = QTableWidgetItem(str(disci.get(keylist[j])))
            self.ui.editdiscitableWidget.setItem(0, j, item)
        # configuração dos campos de edição de disciplina
        self.ui.editdiscicargahoraspinBox_4.setValue(disci['carga_horaria'])
        self.ui.editdiscinomelineEdit.setText(disci['disciplina'])
        self.ui.editdiscilocallineEdit.setText(disci['local'])
        self.ui.editdiscitipomediacomboBox.setCurrentText(disci['tipo_media'])
        dia, hora = disci['horario'].split(' ')
        self.ui.editdiscidiacomboBox.setCurrentText(dia)
        self.ui.editdiscihorariotimeEdit.setTime(QTime.fromString(hora, 'hh:mm'))
        
        self.ui.stackedWidget.setCurrentIndex(5) # muda para a página de edição de disciplina


    #função que exibe a página de marcação de presença
    def marcpres_page(self):
        disci = db.getDisciplinaPorId(self.disci_id_atual) #coleta das informações da disciplina atual
        disci_pres = [disci.get('carga_horaria'),disci.get('qtd_presenca'),f"{(disci.get('qtd_presenca')/disci.get('carga_horaria')*100):.2f}%"]
        self.ui.marcprestableWidget.setRowCount(1) # configuração da tabela de presença
        self.ui.marcprestableWidget.setColumnCount(3)
        self.ui.marcprestableWidget.setHorizontalHeaderLabels(['Carga Horária', 'Presenças', 'Precentual'])
        for j in range(3):
            item = QTableWidgetItem(str(disci_pres[j]))
            self.ui.marcprestableWidget.setItem(0, j, item)
        self.ui.marcpresspinBox.setMaximum(disci.get('carga_horaria') - disci.get('qtd_presenca')) #configuração dos limites de marcação de presença
        self.ui.marcpresspinBox.setMinimum(-disci.get('qtd_presenca'))
        self.ui.stackedWidget.setCurrentIndex(6) # muda para a página de marcação de presença


    #função que lista as disciplinas no combo box
    def Lista_Disciplina(self):
        self.ui.listDiscicomboBox.clear()
        self.ui.listDiscicomboBox.addItem('Disciplinas...')
        disciplinas = db.listarDisciplinas()
        for disciplina in disciplinas:
            self.ui.listDiscicomboBox.addItem(f"{disciplina[0]} - {disciplina[1]}") # adiciona o ID e o nome da disciplina no combo box
    

    #função de marcação de presença
    def MarcarPresenca(self):
        disciplina_id = self.disci_id_atual
        qtd_presenca = self.ui.marcpresspinBox.value()
        db.marcarPresenca(disciplina_id,qtd_presenca) # atualiza a quantidade de presença da disciplina no banco de dados
        self.disci_page() # retorna à pagina da disciplina
    

    #função de edição de disciplina
    def EditarDisciplina(self): #coleta os dados do formulário de edição de disciplina
        disciNome = self.ui.editdiscinomelineEdit.text()
        carga = self.ui.editdiscicargahoraspinBox_4.value()
        presenca = self.ui.editdiscipresencaspinBox.value()
        tipo_media = self.ui.editdiscitipomediacomboBox.currentText()
        local = self.ui.editdiscilocallineEdit.text()
        horario = f'{self.ui.editdiscidiacomboBox.currentText()} {self.ui.editdiscihorariotimeEdit.text()}' 
        db.editarDisciplina(self.disci_id_atual, disciNome, tipo_media, carga, presenca, local, horario) #envio ao banco de dados
        self.disci_page() #retorna à pagina da disciplina
    

    #função de adição de notas
    def addNotas(self): #coleta os dados do formulário de nova nota
        nota = self.ui.novnotadoubleSpinBox.value()
        peso = self.ui.novnotapesospinBox.value()
        db.addNotas(self.disci_id_atual, nota, peso) #envio ao banco de dados
        self.disci_page() #retorna à pagina da disciplina
    

    #função de edição de notas
    def EditarNota(self): #coleta os dados do formulário de edição de nota
        nota = self.ui.editnotadoubleSpinBox.value()
        peso = self.ui.editnotaspinBox.value()
        nota_id = int(self.ui.editnotaselectcomboBox.currentText())
        db.editarNota(nota_id, nota, peso) #envio ao banco de dados
        self.editnota_page() #atualiza a página de edição de notas
    

    #função de remoção de notas
    def RemoverNota(self): #coleta o ID da nota a ser removida
        nota_id = int(self.ui.editnotaselectcomboBox.currentText())
        db.removerNota(nota_id) #envio ao banco de dados
        self.editnota_page() #atualiza a página de edição de notas


    #função de remoção de disciplina
    def ApagarDisciplina(self): #coleta o ID da disciplina a ser removida
        db.removerDisciplina(self.disci_id_atual) #envio ao banco de dados
        self.Lista_Disciplina() #atualiza a lista de disciplinas
        self.lista_ID = db.listarDisciplinas() #atualiza a lista de IDs das disciplinas
        self.ui.listDiscicomboBox.setCurrentIndex(0) #retorna à página geral


    #função que exibe as anotações
    def Anotacao(self,textbrowser):
        anotacao = db.getAnotacoesPorId(self.disci_id_atual) #coleta as anotações da disciplina atual
        textbrowser.setText(anotacao[0]) #exibe as anotações no text browser correspondente


    #função que salva as anotações
    def SalvarAnotacao(self):
        if self.disci_id_atual == 0: #seleção entre geralanotaTextBrowser e discianotaTextBrowser
            textbrowser = self.ui.geralanotatextBrowser 
        else:
            textbrowser = self.ui.discianotatextBrowser
        anotacao = textbrowser.toPlainText() # coleta o texto do text browser
        db.editarAnotacao(self.disci_id_atual, anotacao) #envio ao banco de dados

if __name__ == '__main__': # bloco principal do programa
    app = QApplication(sys.argv)
    db = DB_connect()
    db.iniciarBD() # inicialização do banco de dados
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())