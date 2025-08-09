from sqlite3 import connect

#Funções auxiliares:
def IsTable(table_name: str):
          con = connect("SoftwareDB.db")
          cur = con.cursor()
          res = cur.execute(f"SELECT * FROM Sqlite_master WHERE type='table' AND name='{table_name}'")
          table = res.fetchone()

          return table
         


#Classe principal:
class DB_connect():
          def __init__(self) -> None:
                  self.con = connect("teste.db")
                  #self.con = connect("SoftwareDB.db")
                  self.cursor = self.con.cursor()


          def iniciarBD(self)-> None:
                # self.cursor.execute("DROP TABLE Disciplinas")
                # self.con.commit()
                # self.cursor.execute("DROP TABLE anotacoes")
                # self.con.commit()

                #Cria a Tabela de Disciplinas:
                Table = IsTable("disciplinas")
                if Table == None:
                        self.cursor.execute("""
                                CREATE TABLE disciplinas (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        disciplina TEXT NOT NULL UNIQUE,
                                        media REAL,
                                        tipo_media TEXT NOT NULL,
                                        carga_horaria TEXT NOT NULL,
                                        qtd_presenca INTEGER NOT NULL,
                                        local TEXT NOT NULL,
                                        horario TEXT NOT NULL
                                );
                        """)
                        #self.con.commit()

                #Cria a Tabela de Notas:
                Table = IsTable("notas")
                if Table == None:
                        self.cursor.execute("""
                                CREATE TABLE notas (
                                        id_notas INTEGER PRIMARY KEY AUTOINCREMENT,
                                        notas REAL NOT NULL,
                                        id_disciplina INTEGER NOT NULL,
                                        FOREING KEY id_disciplina REFERENCES disciplinas(id)
                                );"""
                        )

                #Cria a Tabela de Anotaçõess
                Table = IsTable("anotacoes")
                if Table == None:
                        self.cursor.execute("""
                                CREATE TABLE anotacoes (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        anotacao TEXT NOT NULL,
                                        id_disciplina INTEGER NOT NULL,
                                        FOREING KEY id_disciplina REFERENCES disciplinas(id)
                                );"""
                        )
                        self.con.commit()
                

          def novaDisciplina(self, disciplina: str, tipoMedia: str, cargaHoraria: int, horario: str, local="não Informado", qtdPresenca=0, media=0.0) -> None:
                self.cursor.execute(f"INSERT INTO disciplinas(disciplina, media, tipo_media, carga_horaria, qtd_presenca, local, horario) VALUES (?, ?, ?, ?, ?, ?, ?)", (disciplina, media, tipoMedia, cargaHoraria, qtdPresenca, local, horario))
                self.con.commit()

          def marcarPresenca(self) -> None:
                  pass
          

          def novaAnotacao(self) -> None:
                  pass

if __name__ == "__main__":
          db = DB_connect()
          
          #Area de Teste:
          db.iniciarBD()
          db.novaDisciplina(disciplina="Matematica", tipoMedia="aritmetica", cargaHoraria=25, horario="07:00")
