from model.func_gerais import exist, deseja_continuar, exibir_tabela
import cores

class Partida:

  import sqlite3
  
#MÉTODO CONSTRUTOR
  def __init__ (self, conn):
    self.id_partida = ""
    self.conn = conn
    self.cursor = self.conn.cursor()
  
# --------------------------------------------------------------------------------------------
#INSERIR OS VALORES EM PARTIDA 

  def inserir_partida(self, res_time_01, res_time_02, id_mapa):
    if exist(self.cursor, id_mapa, "mapa", "id_mapa") == False:# O REGISTRO NÃO EXISTE
      return (cores.RED + "\nERRO: Insira um mapa válido.\n" + cores.RESET)
        
    else:
      self.cursor.execute("INSERT INTO partida VALUES (?,?,?,?)", (None ,res_time_01, res_time_02, id_mapa))
      self.conn.commit()
      return(cores.GREEN + "\nPartida inserido com sucesso!" + cores.RESET)

# ----------------------------------------------------------------------------------------------
#EXIBIR TODOS OS PARTIDA:
  
  def exibir_partida(self):
    self.cursor.execute("SELECT p.id_partida as 'ID', p.res_time_01 as 'Placar Time 1', p.res_time_02 as 'Placar Time 2', p.id_mapa as 'ID Mapa', m.nome_mapa as 'Mapa' FROM partida p INNER JOIN mapa m ON p.id_mapa = m.id_mapa;")
    
    exibir_tabela(self.cursor)# Exibe a tabela formatada da consulta
    print("\n")
    return "Consulta realizada"

# -----------------------------------------------------------------
# EXCLUIR JOGADOR

  def excluir_partida(self, id):
    if exist(self.cursor, id, "partida", "id_partida") == False:
      return (cores.RED + "\nERRO: Registro não encontrado!" + cores.RESET)
      
    else:
      while True:
        print(cores.GOLD + "\nALERT: Os dados serão apagados permanentemente." + cores.RESET)
        resp = deseja_continuar() #Função de apresenta e análisa continuidade
        if resp == True:
          self.cursor.execute("DELETE FROM partida WHERE id_partida = (?);", (id,))
          self.conn.commit()
          return (cores.GREEN + f"Partida {id} excluído com sucesso" + cores.RESET)
          
        elif resp == False:
          return (cores.PINK + "Operação cancelada!" + cores.RESET)
          
        else:
          print(cores.RED + "\nERRO: Valor inválido!" + cores.RESET)

#----------------------------------------------------------------------------------------------
#ATUALIZA OS DADOS DA PARTIDA
  def atualizar_partida(self, id_partida, dado_att, op_att):
    try:
      if exist(self.cursor, id_partida, "partida", "id_partida") == False:
        return (cores.RED + "\nERRO: Partida não encontrada." + cores.RESET)
  
      else:
        if dado_att == None or dado_att == "" or op_att == None: return(cores.GOLD + "\nALERT: Todos os campos devem ser preenchidos" + cores.RESET)
          
        else: # Todos os valores foram inseridos
          opcoes = {1:"res_time_01", 2:"res_time_02", 3:"id_mapa"}

          if op_att == 3: 
            if exist(self.cursor, dado_att, "mapa", "id_mapa") == False: return(cores.RED + "\nERRO: Mapa não encontrado!" + cores.RESET)

          self.cursor.execute(f"UPDATE partida SET {opcoes[op_att]} = ? WHERE id_partida = ?", (dado_att, id_partida))
          self.conn.commit()
          return(cores.GREEN + "\nValores atualizados com sucesso!" + cores.RESET)
    
    except KeyError:
      return (cores.RED + "\nErro: Informe apenas opções válidas" + cores.RESET)
      