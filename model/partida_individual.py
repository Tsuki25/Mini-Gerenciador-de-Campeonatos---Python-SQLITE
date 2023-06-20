from model.func_gerais import exist, deseja_continuar, exibir_tabela
import cores

class Partida_individual:

  import sqlite3 
  import time
  import datetime

#MÉTODO CONSTRUTOR
  def __init__ (self, conn):
    self.conn = conn
    self.cursor = self.conn.cursor()

# --------------------------------------------------------------------------------------------
  #VERIFICA SE HÁ REGISTRO CORRESPONDENTE NO BANCO
  def partida_ind_exist(self, id, tag_time):
    self.cursor.execute("SELECT * FROM partida_individual WHERE id_partida = ? and tag_time = ?", (id, tag_time))
    res = self.cursor.fetchall()
    if res == None or res == "" or len(res) == 0:#Se o id não existir
      return False
    else: 
      return True
      
# --------------------------------------------------------------------------------------------
#INSERIR OS VALORES EM PARTIDA INDIVIDUAL 
  
  def inserir_partida_individual(self, id_partida, tag_time, placar_time, data_partida, id_adm):
    try:
      if exist(self.cursor, id_partida, "partida", "id_partida") ==  False or exist(self.cursor, tag_time, "time", "tag_time") == False or exist(self.cursor, id_adm, "administrador", "id_adm") == False: #CONFIRMA QUE os dados inseridos existem
        return (cores.RED + "\nERRO: Dado inválido, utilize apenas partidas, times e administradores existentes.\n" + cores.RESET)
        
      else:
        if data_partida == None or data_partida == "":return(cores.GOLD + "\nALERT: Todos os dados devem ser inseridos!" + cores.RESET)
        data_partida = self.datetime.datetime.strptime(data_partida, '%d/%m/%Y').date()
        self.cursor.execute("INSERT INTO partida_individual VALUES (?,?,?,?,?)", (id_partida, tag_time, placar_time, data_partida, id_adm))
        self.conn.commit()
        return(cores.GREEN + "\nPartida do time, inserida com sucesso" + cores.RESET)

    except ValueError:
      return (cores.GOLD+ "\nALERT: Formato de data inválido, tente utilizar dia/mês/ano.\n" + cores.RESET)

# ----------------------------------------------------------------------------------------------
#EXIBIR TODOS AS PARTIDAS INDIVIDUAIS:
  
  def exibir_partida_individual(self):
    self.cursor.execute("SELECT id_partida as 'ID', tag_time as 'Time', placar_time as 'Placar', data_partida as 'Data', id_adm as 'ADM' FROM partida_individual;")
    
    exibir_tabela(self.cursor)# Exibe a tabela formatada da consulta 
    print("\n")
    return "Consulta realizada"

# ----------------------------------------------------------------------------------------------
#EXCLUIR JOGADOR

  def excluir_registro_partida(self, id_partida, tag_time):
    if self.partida_ind_exist(id_partida, tag_time) == False:
      return (cores.RED + "\nERRO: Registro não encontrado!" + cores.RESET)
    else:
      
      while True:
        print(cores.GOLD + "\nALERT: Os dados serão apagados permanentemente." + cores.RESET)
        resp = deseja_continuar() #Função de apresenta e análisa continuidade
        
        if resp == True:
          self.cursor.execute("DELETE FROM partida_individual WHERE id_partida = (?) and tag_time = (?);", (id_partida, tag_time))
          self.conn.commit()
          return (cores.GREEN + "\nRegistro excluído com sucesso" + cores.RESET)
          
        elif resp == False:
          return (cores.PINK + "\nOperação cancelada!" + cores.RESET)
          
        else:
          print(cores.RED + "\nERRO: Valor inválido!" + cores.RESET)

#----------------------------------------------------------------------------------------------
#ATUALIZA OS DADOS DO JOGADOR
  def atualizar_partida_individual(self, id_partida, tag_time, dado_att, op_att):
    try:
      if self.partida_ind_exist(id_partida, tag_time) == False:
        return (cores.RED + "\nERRO: Registro não encontrado." + cores.RESET)
  
      else:
        if dado_att == None or dado_att == "" or op_att == None: return(cores.GOLD + "ALERT: Todos os campos devem ser preenchidos" + cores.RESET)# INSCRICAO NÃO INFORMADO
          
        else: # Todos os valores foram inseridos
          #ARMAZENA AS OPÇÕES DE ATUALIZAÇÃO
          opcoes = {1:"tag_time", 2:"placar_time", 3:"data_partida"} 
          
          self.cursor.execute(f"UPDATE partida_individual SET {opcoes[op_att]} = ? WHERE id_partida = ? and tag_time = ?", (dado_att, id_partida, tag_time))
          self.conn.commit()
          return(cores.GREEN + "\nValores atualizados com sucesso!" + cores.RESET)
            
    except ValueError:
      return (cores.GOLD + "\nALERT: Formato de data inválido, tente utilizar dias/mês/ano.\n" + cores.RESET)

    except KeyError:
      return (cores.RED + "Erro: Informe apenas opções válidas" + cores.RESET)
      
      