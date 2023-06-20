import control.schema
from control.cleaner import limpar
from control.dados_iniciais import dados_banco, dados_init
import sqlite3

import view.menu_principal


#INSTANCIA E EXIBE O MENU
#menu = view.menu_inicial.menu_principal()
#menu.menu_interativo()

if __name__ == '__main__':
  limpar()
  banco = "testes"
  conn = control.schema.criar_banco(banco)
  func_subs = view.func_submenus.func_subs(conn)

  if dados_banco(conn) == False: #O BANCO ESTÁ VAZIO
    dados_init(conn)

  while True:
    retorno = view.menu_principal.menu_principal(conn)
    if(retorno == False):
      break
  
  