import os
import sys

import pandas as pd


class BaseDeDados():
    def __init__(self):
        if os.path.exists('db_disciplinas.csv'):
            self.db_disciplinas = pd.read_csv('db_disciplinas.csv')
        else:
            self.db_disciplinas = pd.DataFrame(columns=('ID','Disciplina','Média','Tipo de Média','Carga Horária','Presença','Local','Horário'))
        if os.path.exists('db_notas.csv'):
            self.db_notas = pd.read_csv('db_notas.csv')
        else:
            self.db_notas = pd.DataFrame(columns=('ID','ID Disciplina','Nota','Peso'))
        if os.path.exists('db_disciplinas.csv'):
            self.db_anotacoes = pd.read_csv('db_anotacoes.csv')
        else:
            self.db_anotacoes = pd.DataFrame(columns=('ID','ID_Disciplina','Anotacao'))
    

    def novaDisciplina(self,disciplina,tipoMedia,cargaHoraria,horario,local,qtPresença,media)