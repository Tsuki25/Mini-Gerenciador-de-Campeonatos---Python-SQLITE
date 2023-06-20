from model.func_gerais import exist, deseja_continuar, exibir_tabela
import cores

class Administradores:

  import sqlite3
  
  #método construtor
  def __init__(self, conn):
    self.nome_administradores = ""
    self.conn = conn
    self.cursor = self.conn.cursor()

  def get_nome_administradores(self):
    return self.nome_administradores

#----------------------------------------------------------------------------------------------
#INSERIR OS ADMINISTRADORES NO SISTEMA
  
  def inserir_administradores(self, nome, email):
    try: 
      if nome != "" and email != "":
        self.cursor.execute("INSERT INTO administrador (nome, email) VALUES (?, ?)", (nome, email))
        self.conn.commit()
        return (cores.GREEN + "Administrador inserido com sucesso!" + cores.RESET)

      else:
        return (cores.GOLD + "ALERT: Insira todos os dados!" + cores.RESET)
    except Exception:   
      return(cores.RED + "ERRO: E-mail já cadastrado." + cores.RESET)
    
#----------------------------------------------------------------------------------------------
#EXIBIR OS ADMINISTRADORES DO SISTEMA
  
  def exibir_administrador(self):
    self.cursor.execute("SELECT id_adm as 'ID', nome as 'Nome', email as 'Email' FROM administrador;")
    
    exibir_tabela(self.cursor)
    print("\n")
    return (cores.CYAN + "Consulta realizada" + cores.RESET)

#----------------------------------------------------------------------------------------------
#EXCLUIR OS ADMINISTRADORES DO SISTEMA

  def excluir_administrador(self, id):
    if exist(self.cursor, id, "administrador", "id_adm") == False:
      return (cores.RED + "Erro: Registro não encontrado!" + cores.RESET)
      
    else:
      print(cores.GOLD + "\nALERT: Os dados serão perdidos permanentemente." + cores.RESET)
      while True:
        resp = deseja_continuar()
        if resp == True:
          self.cursor.execute("DELETE FROM administrador WHERE id_adm = (?);", (id,))
          self.conn.commit()
          return (cores.GREEN + "Administrador excluído com sucesso" + cores.RESET)
          
        elif resp == False:
          return (cores.PINK + "Operação cancelada!" + cores.RESET)
          
        else:
          print(cores.RED + "ERRO: Valor inválido!" + cores.RESET)

#---------------------------------------------------------------------
#ATUALIZA OS DADOS DO ADMINISTRADOR
  def atualizar_administrador(self, id, dado_att):
    try:
      if exist(self.cursor, id, "administrador", "id_adm") == False:
        return (cores.RED + "ERRO: Admnistrador não encontrado." + cores.RESET)
  
      else:
        if dado_att == None or dado_att == "": return(cores.GOLD + "ALERT: Todos os campos devem ser preenchidos" + cores.RESET)# INSCRICAO NÃO INFORMADO
          
        else: # Todos os valores foram inseridos
          self.cursor.execute("UPDATE administrador SET nome = ? WHERE id_adm = ?", (dado_att, id))
          self.conn.commit()
          return(cores.GREEN + "Valores atualizados com sucesso!" + cores.RESET)
    
    except Exception: 
      return(cores.RED + "ERRO.\n" + cores.RESET)