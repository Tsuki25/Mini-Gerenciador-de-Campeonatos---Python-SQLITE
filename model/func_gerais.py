import sqlite3
import prettytable
import cores 

# VERIFICA SE HÁ REGISTRO CORRESPONDENTE NO BANCO
def exist(cursor, id, tabela, nome_atributo):
    cursor.execute(f"SELECT * FROM {tabela} WHERE {nome_atributo} = ?", (id,))
    res = cursor.fetchall()
    if res == None or res == "" or len(res) == 0:#Se o id não existir
      return False
    else: 
      return True

# -----------------------------------------------------------

def deseja_continuar():
  res = input(cores.GOLD + "Deseja continuar?" + cores.BOLD + "(S/N): " + cores.RESET)
  resposta = res.upper()
  if resposta == "S":
    return True
    
  elif resposta == "N":
    return False

# ----------------------------------------------------------

def exibir_tabela(cursor):
  # Pega o nome das colunas
  titulo_colunas = [column[0] for column in cursor.description]
  
  # cria a tabela com base no banco
  exibir = prettytable.from_db_cursor(cursor)
  # Adiciona cor aos titulos de coluna
  exibir.field_names = [cores.CYAN + titulo + cores.RESET for titulo in titulo_colunas]

  print(exibir)