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
              self.cursor.execute("""
                      CREATE TABLE IF NOT EXISTS disciplinas (
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
              self.cursor.execute("""
                      CREATE TABLE IF NOT EXISTS notas (
                              id_notas INTEGER PRIMARY KEY AUTOINCREMENT,
                              notas REAL NOT NULL,
                              id_disciplina INTEGER NOT NULL,
                              FOREING KEY id_disciplina REFERENCES disciplinas(id)
                      );"""
              )
              #Cria a Tabela de Anotaçõess
              Table = IsTable("anotacoes")
              self.cursor.execute("""
                      CREATE TABLE IF NOT EXISTS anotacoes (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              anotacao TEXT NOT NULL,
                              id_disciplina INTEGER NOT NULL,
                              FOREING KEY id_disciplina REFERENCES disciplinas(id)
                      );"""
              )
              self.con.commit()
              

        def novaDisciplina(self, disciplina: str, tipoMedia: str, cargaHoraria: int, horario: str, local="não Informado", qtdPresenca=0, media=0.0) -> None:
              self.cursor.execute(f"INSERT INTO disciplinas(disciplina, media, tipo_media, carga_horaria, qtd_presenca, local, horario) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (disciplina, media, tipoMedia, cargaHoraria, qtdPresenca, local, horario))
              self.con.commit()


        def listarDisciplinas(self):
              #Retorna uma lista de tuplas (id, disciplina) da tabela disciplinas.
              self.cursor.execute("SELECT id, disciplina FROM disciplinas")
              return self.cursor.fetchall()
        

        def marcarPresenca(self, id_disciplina: int, qtdPresenca: int) -> None:
              #Atualiza a quantidade de presença para uma disciplina específica.
              self.cursor.execute(
                  "UPDATE disciplinas SET qtd_presenca = ? WHERE id = ?",(qtdPresenca, id_disciplina)
              )
              self.con.commit()
        

        def novaAnotacao(self, anotacao: str, id_disciplina: int) -> None:
              #Insere uma nova anotação vinculada a uma disciplina.
              self.cursor.execute(
                  "INSERT INTO anotacoes(anotacao, id_disciplina) VALUES (?, ?)",
                  (anotacao, id_disciplina)
              )
              self.con.commit()


        def getDisciplinaPorId(self, id_disciplina: int) -> dict:
                #Retorna as informações da disciplina em formato de dicionário.
                self.cursor.execute(
                    "SELECT * FROM disciplinas WHERE id = ?", (id_disciplina))
                row = self.cursor.fetchone()
                if row:
                    columns = [desc[0] for desc in self.cursor.description]
                    return dict(zip(columns, row))
                return {}


if __name__ == "__main__":
          db = DB_connect()
          
          #Area de Teste:
          db.iniciarBD()
          db.novaDisciplina(disciplina="Matematica", tipoMedia="aritmetica", cargaHoraria=25, horario="07:00")
