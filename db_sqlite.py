from sqlite3 import connect, IntegrityError

#Classe principal:
class DB_connect():
    def __init__(self) -> None:
        self.con = connect("teste.db")
        #self.con = connect("SoftwareDB.db")
        self.cursor = self.con.cursor()
        
        self.cursor.execute("PRAGMA foreign_keys = ON;")


    def __IsTable(self, table_name: str):
        self.cursor.execute(f"SELECT * FROM Sqlite_master WHERE type='table' AND name='{table_name}'")
        table = self.cursor.fetchone()

        return table

    
     def iniciarBD(self)-> None:
        # self.cursor.execute("DROP TABLE anotacoes;")
        # self.con.commit()
        # self.cursor.execute("DROP TABLE notas;")
        # self.con.commit()
        # self.cursor.execute("DROP TABLE disciplinas;")
        # self.con.commit()

        #Cria a Tabela de Disciplinas:
        Table = self.__IsTable("disciplinas")
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
                );"""
            )

        #Cria a Tabela de Notas:
        Table = self.__IsTable("notas")
        if Table == None:
            self.cursor.execute("""
                CREATE TABLE notas (
                    id_notas INTEGER PRIMARY KEY AUTOINCREMENT,
                    nota REAL NOT NULL,
                    id_disciplina INTEGER NOT NULL,
                    FOREIGN KEY (id_disciplina) REFERENCES disciplinas(id) ON DELETE CASCADE
                );"""
            )

        #Cria a Tabela de Anotaçõess
        Table = self.__IsTable("anotacoes")
        if Table == None:
            self.cursor.execute("""
                CREATE TABLE anotacoes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    anotacao TEXT NOT NULL,
                    id_disciplina INTEGER NOT NULL,
                    FOREIGN KEY (id_disciplina) REFERENCES disciplinas(id) ON DELETE CASCADE
                );"""
            )
        
        self.con.commit()
          

     def novaDisciplina(self, disciplina: str, tipoMedia: str, cargaHoraria: int, horario: str, local="não Informado", qtdPresenca=0, media=0.0) -> str:
        try:
            self.cursor.execute("""
                INSERT INTO disciplinas(disciplina, media, tipo_media, carga_horaria, qtd_presenca, local, horario)
                VALUES (?, ?, ?, ?, ?, ?, ?)""",(disciplina, media, tipoMedia, cargaHoraria, qtdPresenca, local, horario))
            self.con.commit()
        except IntegrityError as e:
            print(f"Disciplina {disciplina} ja existe.\n{e}")

            return f"Disciplina {disciplina} ja existe."
        except Exception as e:
            print(f"Erro Inesperado:\n{e}")

            return f"Houve um erro ao acrecentar a disciplina {disciplina}"
        else:
            return f"Sucesso ao acrecentar {disciplina} nas disciplinas"


     def removerDisciplina(self, disciplina: str) -> str:
        try:
            self.cursor.execute("SELECT id FROM disciplinas WHERE disciplina=?;", (disciplina,))
            id_disciplina = self.cursor.fetchone()[0]

            self.cursor.execute("DELETE FROM disciplinas WHERE id=?;", (id_disciplina,))
        except TypeError as e:
            print(f"Discipliana {disciplina} não encontrado!\nERRO: {e}")

            return f"Disciplina não encontrado"
        except Exception as e:
            print(f"Houve um erro!\nERRO: {e}")

            return "Houve um erro!"
        else:
            print(f"Remoção de {disciplina} concluido com sucesso")

            return f"Remoção de {disciplina} concluido com sucesso"


    def listarDisciplinas(self):
          #Retorna uma lista de tuplas (id, disciplina) da tabela disciplinas.
          self.cursor.execute("SELECT id, disciplina FROM disciplinas")
          return self.cursor.fetchall()
    

    def editarDisciplina(self, disciplina, novoNome=None, novaMedia=None, novoTipoMedia=None, novaCargaHoraria=None, nova_qtd_presenca=None, novoLocal=None, novoHorario=None):
        self.cursor.execute("SELECT id FROM disciplinas WHERE disciplina=?;", (disciplina,))
        id_disciplina = self.cursor.fetchone()[0]
        
        if novoNome:
            self.cursor.execute("UPDATE disciplinas SET disciplina=? WHERE id=?;", (novoNome, id_disciplina))
            self.con.commit()

        if novaMedia:
            self.cursor.execute("UPDATE disciplinas SET media=? WHERE id=?;", (novaMedia, id_disciplina))
            self.con.commit()

        if novoTipoMedia:
            self.cursor.execute("UPDATE disciplinas SET tipo_media=? WHERE id=?;", (novoTipoMedia, id_disciplina))
            self.con.commit()

        if novaCargaHoraria:
            self.cursor.execute("UPDATE disciplinas SET carga_horaria=? WHERE id=?;", (novaCargaHoraria, id_disciplina))
            self.con.commit()

        if nova_qtd_presenca:
            self.cursor.execute("UPDATE disciplinas SET qtd_presenca=? WHERE id=?;", (nova_qtd_presenca, id_disciplina))
            self.con.commit()

        if novoLocal:
            self.cursor.execute("UPDATE disciplinas SET local=? WHERE id=?;", (novoLocal, id_disciplina))
            self.con.commit()

        if novoHorario:
            self.cursor.execute("UPDATE disciplinas SET horario=? WHERE id=?;", (novoHorario, id_disciplina))
            self.con.commit()
            

    def marcarPresenca(self, disciplina: str) -> str:
        #Atualiza a quantidade de presença para uma disciplina específica.
        try:
            self.cursor.execute("SELECT qtd_presenca FROM disciplinas WHERE disciplina=?;", (disciplina,))
            qtd_presença = self.cursor.fetchone()[0]
            qtd_presença += 1
            self.cursor.execute("UPDATE disciplinas SET qtd_presenca=? WHERE disciplina=?;", (qtd_presença, disciplina,))
            self.con.commit()
        except TypeError as e:
            print(f"Disciplina {disciplina} não encontrado\nErro: {e}")

            return f"Disciplina {disciplina} não econtrado"
        except Exception as e:
            print(f"Houve um erro inesperado:\n{e}")

            return "Houve um erro ao marcar presença"
        else:
            return "Presença marcada com sucesso"

   


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
