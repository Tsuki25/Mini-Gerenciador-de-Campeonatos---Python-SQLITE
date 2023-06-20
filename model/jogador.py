from model.func_gerais import exist, deseja_continuar, exibir_tabela
import cores

class Jogador:
  
  import sqlite3 
  import time
  import datetime
  
#MÉTODO CONSTRUTOR
  def __init__ (self, conn):
    self.id_jogador = ""
    self.conn = conn
    self.cursor = self.conn.cursor()

# ------------------------------------------------------------------
  def get_idade(self, str_data_nasc):
    data_nasc = self.datetime.datetime.strptime(str_data_nasc, '%d/%m/%Y').date()
    idade = self.datetime.date.today().year - data_nasc.year
    return idade

# ------------------------------------------------------------------
  def get_time(self, id_jogador):
    self.cursor.execute("SELECT tag_time FROM jogador WHERE id_jogador = ?", (id_jogador,))
    res = self.cursor.fetchall()
    return res[0][0]
      
# --------------------------------------------------------------------------------------------
#INSERIR OS VALORES EM JOGADOR 
  
  def inserir_jogador(self, nome, data_nasc, elo, tag_time):
    try:
      if self.get_idade(data_nasc) < 13 :# O usuário é menor de 13 anos
        return (cores.RED + "ERRO: Permitido apenas para maiores de 13 anos.\n" + cores.RESET)
        
      else:
        self.cursor.execute("INSERT INTO jogador VALUES (?,?,?,?,?)", (None ,nome, data_nasc, elo, tag_time))
        self.conn.commit()
        return(cores.GREEN + "Jogador inserido com sucesso!" + cores.RESET)

    except ValueError:
      return (cores.RED + "ERRO: Formato de data inválido, tente utilizar dia/mês/ano.\n" + cores.RESET)
      
    except Exception:   
      return(cores.RED + "ERRO: Nome de usuário já utilizado." + cores.RESET)

# ----------------------------------------------------------------------------------------------
#EXIBIR TODOS OS JOGADORES:
  
  def exibir_jogador(self):
    self.cursor.execute("SELECT id_jogador as 'ID', nome as 'Nome', data_nasc as 'Data de nascimento', elo as 'Rank', tag_time as 'Time' FROM jogador;")
    
    exibir_tabela(self.cursor) # Exibe a tabela de consulta
    print("\n")
    return "Consulta realizada"

# ----------------------------------------------------------------------------------------------
#EXCLUIR JOGADOR

  def excluir_jogador(self, id):
    if exist(self.cursor, id, "jogador", "id_jogador") == False:
      return (cores.RED + "\nERRO: Jogador não encontrado!" + cores.RESET)
      
    else:
      while True:
        print(cores.GOLD + "\nALERT: Os dados serão perdidos permanentemente." + cores.RESET)
        resp = deseja_continuar() #Função de apresenta e análisa continuidade
        if resp == True:
          self.cursor.execute("DELETE FROM jogador WHERE id_jogador = (?);", (id,))
          self.conn.commit()
          return (cores.GREEN + f"\nJogador {id} excluído com sucesso" + cores.RESET)
          
        elif resp == False:
          return (cores.PINK + "\nOperação cancelada!" + cores.RESET)
          
        else:
          print(cores.RED + "\nERRO: Valor inválido!" + cores.RESET)
      
#----------------------------------------------------------------------------------------------
#ATUALIZA OS DADOS DO JOGADOR
  def atualizar_jogador(self, id, dado_att, op_att):
    try:
      if exist(self.cursor, id, "jogador", "id_jogador") == False:
        return (cores.RED + "\nERRO: Jogador não encontrado." + cores.RESET)
  
      else:
        if dado_att == None or dado_att == "" or op_att == None: return(cores.GOLD + "\nALERT: Todos os campos devem ser preenchidos" + cores.RESET)# INSCRICAO NÃO INFORMADO
          
        else: # Todos os valores foram inseridos
          opcoes = {1:"nome", 2:"data_nasc", 3:"elo"}
          
          if op_att == 2: # ATUALIZAR DATA DE NASCIMENTO
            if self.get_idade(dado_att) < 13 :# O usuário é menor de 13 ano
              return (cores.RED + "\nERRO: Permitido apenas para maiores de 13 anos" + cores.RESET) 

          self.cursor.execute(f"UPDATE jogador SET {opcoes[op_att]} = ? WHERE id_jogador = ?", (dado_att, id))
          self.conn.commit()
          return(cores.GREEN + "\nValores atualizados com sucesso!" + cores.RESET)
    
    except ValueError:
      return (cores.GOLD + "\nALERT: Formato de data inválido, tente utilizar dia/mês/ano." + cores.RESET)

    except KeyError:
      return (cores.RED + "\nErro: Informe apenas opções válidas" + cores.RESET)
    
    except Exception: 
      return(cores.RED + "\nNome de usuário já utilizado.\n" + cores.RESET)