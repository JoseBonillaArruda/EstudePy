from sqlite3 import connect

#Area de Teste:


#Manipulação do Banco de Dados:

#Funções auxiliares:
def IsTable(table_name: str) -> bool:
          con = connect("SoftwareDB.db")
          cur = con.cursor()
          res = cur.execute(f"SELEC * FROM Sqlite_master WHERE type='table' AND name='{table_name}'")
          is_table = res.fetchone()[0]

          if is_table:
                  return True
          else:
                  return False


#Classe principal:
class DB_connect():
          def __init__(self) -> None:
                  self.con = connect("SoftwareDB.db")
                  self.cursor = self.con.cursor()


          def username(self, name) -> None:
                    if not IsTable("userProfile"):
                          self.cursor.execute("""CREATE TABLE  userProfile ("
                              "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                              "name TEXT NOT NULL);"""
                          )
                    else:
                          self.cursor.execute(f"SELECT * FROM userProfile WHERE name='{name}'")
                    
                    self.con.close()


if __name__ == "__main__":
          db = DB_connect()
          
          nome = input("Digite o nome: ")
          db.username(nome)