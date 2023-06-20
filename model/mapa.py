from model.func_gerais import exist, deseja_continuar, exibir_tabela
import cores

class Mapa:
  
  import sqlite3

#MÉTODO CONSTRUTOR
  def __init__ (self, conn):
    self.nome_mapa = ""
    self.conn = conn
    self.cursor = self.conn.cursor()


#----------------------------------------------------------------------------------------------
#INSERIR OS VALORES DE MAPA
  def inserir_mapa(self, nome_mapa):
    try:
      if len(nome_mapa) == 0 or nome_mapa == "":
        return(cores.GOLD + "\nALERT: Nome do mapa é um atributo obrigatório." + cores.RESET)
      else:
        self.cursor.execute("INSERT INTO mapa VALUES (?, ?);", (None, nome_mapa))
        self.conn.commit()
        return (cores.GREEN + "\nMapa inserido com sucesso!" + cores.RESET)
      
    except Exception:   
      return(cores.RED + "ERRO: Inválido, mapa já cadastrado." + cores.RESET)

#----------------------------------------------------------------------------------------------
#EXIBIR OS VALORES EM MAPA
  
  def exibir_mapa(self):
    self.cursor.execute("SELECT id_mapa as 'ID', nome_mapa as 'Nome' FROM mapa;")
    
    exibir_tabela(self.cursor)# Exibe a tabela formatada da consulta 
    print("\n")
    return "Consulta realizada"

#----------------------------------------------------------------------------------------------
#EXCLUIR OS VALORES EM MAPA
  
  def excluir_mapa(self, id_mapa):
    if exist(self.cursor, id_mapa, "mapa", "id_mapa") == False:
      return (cores.RED + "\nERRO: Mapa não encontrado!" + cores.RESET)
    else:
      
      while True:
        print(cores.GOLD + "\nALERT: Os dados serão apagados permanentemente." + cores.RESET)
        resp = deseja_continuar() #Função de apresenta e análisa continuidade
        if resp == True:
          self.cursor.execute("DELETE FROM mapa WHERE id_mapa = (?);", (id_mapa,))
          self.conn.commit()
          return (cores.GREEN + f"\nMapa '{id_mapa}' excluído com sucesso" + cores.RESET)
          
        elif resp == False:
          return (cores.PINK +"\nOperação cancelada!" + cores.RESET)
          
        else:
          print(cores.RED + "\nERRO: Valor inválido!" + cores.RESET)

#----------------------------------------------------------------------------------------------
#ATUALIZA OS DADOS DO MAPA
  
  def atualizar_mapa(self, id_mapa, dado_att):
    if exist(self.cursor, id_mapa, "mapa", "id_mapa") == False: # VERIFICA SE O MAPA EXISTE NO BANCO
      return (cores.RED + "\nERRO: Mapa não encontrado." + cores.RESET)

    else:
      if dado_att == None or dado_att == "": return(cores.GOLD + "\nALERT: Todos os campos devem ser preenchidos" + cores.RESET)# INSCRICAO NÃO INFORMADO
        
      else: # Todos os valores foram inseridos
        self.cursor.execute("UPDATE mapa SET nome_mapa = ? WHERE id_mapa = ?", (dado_att, id_mapa))
        self.conn.commit()
        return(cores.GREEN + "\nValores atualizados com sucesso!" + cores.RESET)