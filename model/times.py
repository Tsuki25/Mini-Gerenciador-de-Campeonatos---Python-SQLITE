from model.func_gerais import exist, deseja_continuar, exibir_tabela
import cores

class Time:
  
  import sqlite3

#MÉTODO CONSTRUTOR
  def __init__ (self, conn):
    self.nome_times = ""
    self.conn = conn
    self.cursor = self.conn.cursor()

  def get_nome_time(self):
    return self.nome_time

# ---------------------------------------------------------------
  def elo_medio(self, tag_time):
    self.cursor.execute("SELECT avg(elo) FROM jogador WHERE tag_time = ?", (tag_time,)) #CALCULA A MEDIA DE ELO DOS JOGADORES
    res = self.cursor.fetchall()
    elo_medio = round(res[0][0])

    self.cursor.execute("UPDATE time SET elo_medio = ? WHERE tag_time = ?", (elo_medio, tag_time)) #SETA O MEDIO ELO DE ACORDO COM OS JOGADORES

  
# ---------------------------------------------------------------------
  def jogadores_time(self, tag_time):
    if exist(self.cursor, tag_time, "time", "tag_time") == False:
      return (cores.RED + "\nERRO: Time ou Jogador não encontrado!" + cores.RESET)
    self.cursor.execute("SELECT count(id_jogador) FROM jogador WHERE tag_time = ?", (tag_time,)) #Conta o número de jogadores em um time
    res = self.cursor.fetchall()
    num_jogadores = res[0][0]
    return num_jogadores

#----------------------------------------------------------------------------------------------
#INSERIR OS VALORES EM TIME
  def inserir_time(self, tag, nome, elo):
    try:
      self.cursor.execute("INSERT INTO time (tag_time, nome_time, elo_medio) VALUES (?,?,?);", (tag, nome, elo))
      self.conn.commit()
      return True #RETORNA TRUE PARA PERMITIR VERIFICAÇÂO E INCLUSÃO DOS JOGADORES
    except Exception:
      return False 

#----------------------------------------------------------------------------------------------
#EXIBIR OS VALORES EM TIME
  
  def exibir_time(self):
    self.cursor.execute("SELECT tag_time as 'TAG', nome_time as 'Nome do Time', elo_medio as 'ELO' FROM time;")
    
    exibir_tabela(self.cursor,)# Exibe a tabela formatada da consulta 
    print("\n")
    return "Consulta realizada"

#----------------------------------------------------------------------------------------------
#EXCLUIR OS VALORES EM TIME
  
  def excluir_time(self, tag):
    if exist(self.cursor, tag, "time", "tag_time") == False:
      return (cores.RED + "\nERRO: Time não encontrado!" + cores.RESET)

    else:
      while True:
        print(cores.GOLD + "\nALERT: Os dados serão apagados permanentemente." + cores.RESET)
        resp = deseja_continuar() #Função de apresenta e análisa continuidade
        if resp == True:
          self.cursor.execute("DELETE FROM time WHERE tag_time = (?);", (tag,))
          self.conn.commit()
          return (cores.GREEN + f"\nTime {tag} excluído com sucesso" + cores.RESET)
          
        elif resp == False:
          return (cores.PINK + "\nOperação cancelada!" + cores.RESET)
          
        else:
          print(cores.RED + "\nERRO: Valor inválido!" +  + cores.RESET)
      

#----------------------------------------------------------------------------------------------
#ATUALIZA OS DADOS DO TIME
  def atualizar_times(self, tag, dado_att, op_att):
    try:
      if exist(self.cursor, tag, "time", "tag_time") == False:
        return (cores.RED + "\nERRO: Registro não encontrado." + cores.RESET)
  
      else:
        if dado_att == None or dado_att == "" or op_att == None: return(cores.GOLD + "\nALERT: Todos os campos devem ser preenchidos" + cores.RESET)# INSCRICAO NÃO INFORMADO
          
        else: # Todos os valores foram inseridos
          opcoes = {1:"nome_time", 2:"elo_medio"}
          
          self.cursor.execute(f"UPDATE time SET {opcoes[op_att]} = ? WHERE tag_time = ?", (dado_att, tag))
          self.conn.commit()
          return(cores.GREEN + "\nValores atualizados com sucesso!" + cores.RESET)
          
    except KeyError:
      return (cores.RED + "\nErro: Informe apenas opções válidas" + cores.RESET)

# -------------------------------------------------------------------
  # ----------------- FUNÇÕES ADICIONAIS ----------------------------
  
  def remover_jogador_time(self, id_jogador, tag_time):
    if exist(self.cursor, tag_time, "time", "tag_time") == False or exist(self.cursor, id_jogador, "jogador", "id_jogador") == False:
      return (cores.RED + "\nERRO: Time ou Jogador não encontrado!" + cores.RESET)

    else: #Todos existem
      self.cursor.execute("UPDATE jogador SET tag_time = ? WHERE id_jogador = ?;",('FA', id_jogador))
      self.conn.commit()
      return (cores.GREEN + "\nJogador removido com sucesso!" + cores.RESET)

# -------------------------------------------------------------
  def free_agent(self, id_jogador):
    self.cursor.execute("UPDATE jogador SET tag_time = ? WHERE id_jogador = ?;",('FA', id_jogador)) # REMOVE O JOGADOR DO TIME
    self.conn.commit()
  
# -------------------------------------------------------------
  
  def substituir_jogador(self, id_jogador_saindo, tag_time, id_jogador_entrando):
    
    if exist(self.cursor, tag_time, "time", "tag_time") == False or exist(self.cursor, id_jogador_saindo, "jogador", "id_jogador") == False or exist(self.cursor, id_jogador_entrando, "jogador", "id_jogador") == False:
      return (cores.RED + "\nERRO: Time ou Jogador não encontrado!" + cores.RESET)

    else: #Todos existem
      self.free_agent(id_jogador_saindo)

      self.cursor.execute("UPDATE jogador SET tag_time = ? WHERE id_jogador = ?;",(tag_time, id_jogador_entrando))
      self.conn.commit()
      return (cores.GREEN + "\nSubstituição efetuada com sucesso!" + cores.RESET)

# ---------------------------------------------------------------
  def sexto_player(self, id_jogador, tag_time):
      if exist(self.cursor, tag_time, "time", "tag_time") == False or exist(self.cursor, id_jogador, "jogador", "id_jogador") == False:
        return (cores.RED + "\nERRO: Time ou Jogador não encontrado!" + cores.RESET)
  
      else: #Todos existem
        self.cursor.execute("UPDATE jogador SET tag_time = ? WHERE id_jogador = ?;",(tag_time, id_jogador))
        self.conn.commit()
        return (cores.GREEN + "\nJogador adicionado com sucesso!" + cores.RESET) 
      