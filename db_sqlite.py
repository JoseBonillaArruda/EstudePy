from sqlite3 import connect, IntegrityError

#Classe principal:
class DB_connect():
    def __init__(self) -> None:
        self.con = connect("teste.db") #Cria o banco de dados para testes
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
                    carga_horaria INTEGER NOT NULL,
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
        #Adiciona uma nova disciplina
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
        #Remove uma disciplina
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
        #Edita as informações necessarias da disciplina

        #Copilot
        campos = {
            "disciplina": novoNome,
            "media": novaMedia,
            "tipo_media": novoTipoMedia,
            "carga_horaria": novaCargaHoraria,
            "qtd_presenca": nova_qtd_presenca,
            "local": novoLocal,
            "horario": novoHorario
        }
        set_clauses = []
        valores = []
        for campo, valor in campos.items():
            if valor is not None and valor != "":
                set_clauses.append(f"{campo}=?")
                valores.append(valor)
        if not set_clauses:
            return "Nenhum campo para atualizar foi fornecido."
        self.cursor.execute("SELECT id FROM disciplinas WHERE disciplina=?;", (disciplina,))
        resultado = self.cursor.fetchone()
        if not resultado:
            return "Disciplina não encontrada."
        id_disciplina = resultado[0]
        sql = "UPDATE disciplinas SET " + ", ".join(set_clauses) + " WHERE id=?;"
        valores.append(id_disciplina)
        self.cursor.execute(sql, valores)
        self.con.commit()
        return f"Disciplina '{disciplina}' atualizada com sucesso."
        #Copilot

        # valores = [novoNome, novaMedia, novoHorario, novoTipoMedia, novaCargaHoraria, nova_qtd_presenca, novoLocal, novoHorario]
        # for valores in valores:
        #     print(valores)

        # self.cursor.execute("SELECT id FROM disciplinas WHERE disciplina=?;", (disciplina,))
        # id_disciplina = self.cursor.fetchone()[0]

        # self.cursor.execute("SELECT * FROM disciplinas WHERE id=?", (id_disciplina,))
        # print(self.cursor.fetchall()[0])

            

    def marcarPresenca(self, id: int, valor: int) -> None:
        #Atualiza a quantidade de presença para uma disciplina específica.
        self.cursor.execute("SELECT qtd_presenca FROM disciplinas WHERE id=?", (id,))
        qtd_presenca = self.cursor.fetchall()[0][0]

        if qtd_presenca + valor >= 0:
            qtd_presenca += valor

        self.cursor.execute("UPDATE disciplinas SET qtd_presenca=? WHERE id=?;", (qtd_presenca, id,))
        self.con.commit()


    def novaAnotacao(self, disciplina: str, anotacao: str, titulo = None) -> None:
        #Adiciona uma nova anotação
        try:
            self.cursor.execute("SELECT id FROM disciplinas WHERE disciplina=?;", (disciplina,))
            id_disciplina = self.cursor.fetchone()[0]

            if not titulo:
                titulo = anotacao[:20].strip().replace("\n", " ")
                titulo = titulo[:22] + "..." if len(anotacao.strip()) > 25 else titulo
            elif len(titulo) > 25:
                titulo = titulo[:22] + "..."

            if anotacao.strip() != "":
                self.cursor.execute("INSERT INTO anotacoes(titulo, anotacao, id_disciplina) VALUES (?, ?, ?);", (titulo ,anotacao, id_disciplina,))
                self.con.commit()
            else:
                print("Anotação está vazia.")
        
        except TypeError as e:
            print(f"Houve um erro ao salvar a anotação\nErro: {e}")
            
            return f"Houve um erro ao salvar"
        except Exception as e:
            print(f"Houve um erro inesperado:\n{e}")

            return f"Houve um erro ao salvar"
        else:
            print("Anotação salva com sucesso")

            return "Anotação salva com sucesso"


    def addNotas(self, disciplina: str, nota: float) -> str:
        #Adiciona nota a disciplina vinculada
        try:
            self.cursor.execute("SELECT id FROM disciplinas WHERE disciplina=?;", (disciplina,))
            id_disciplina = self.cursor.fetchone()[0]
            self.cursor.execute("INSERT INTO notas(nota, id_disciplina) VALUES (?, ?)", (nota, id_disciplina,))
            self.con.commit()
        except TypeError as e:
            print(f"Houve um erro ao adicionar nota\nErro: {e}")
            
            return f"Houve um erro ao adicionar"
        except Exception as e:
            print(f"Houve um erro inesperado:\n{e}")

            return f"Houve um erro ao adicionar nota"
        else:
            print("Nota adicionada com sucesso")

            return "Nota adicionada com sucesso"


    def getDisciplinaPorId(self, id_disciplina: int) -> dict:
            #Retorna as informações da disciplina em formato de dicionário.
            self.cursor.execute(
                "SELECT * FROM disciplinas WHERE id = ?", (id_disciplina,))
            row = self.cursor.fetchone()
            if row:
                columns = [desc[0] for desc in self.cursor.description]
                return dict(zip(columns, row))
            return {}

    
    #para testes
    def resetTable(self, tableName: str) -> None:
        #Apaga todas as informações da tabela
        self.cursor.execute(f"DELETE FROM {tableName};")
        self.con.commit()


if __name__ == "__main__":
    db = DB_connect()
        
    #Area de Teste:
    db.iniciarBD()
    #db.novaDisciplina(disciplina="História", tipoMedia="aritmetica", cargaHoraria=25 , horario="10:00", local="Sala-A1")
    #db.removerDisciplina("História")
    #print(retorno)
    db.marcarPresenca(1, -460)
    #db.novaAnotacao("Matematica", "")
    #db.addNotas("Matematica", 8.5)
    #db.editarDisciplina("Matematica", novaMedia=6.5)

    
    
    #db.resetTable("anotacoes")
