import curses
import view.func_submenus
from control.cleaner import limpar
import cores

#----------------------------------------------------------------------------------------------
#tela padrao de todos os submenus

def exibir_submenu(stdscr, opcoes, selecionado, entidade):
  stdscr.clear()

  curses.start_color()
  curses.use_default_colors()

  curses.init_pair(1, 190, -1)
  curses.init_pair(2, 194, -1)
  curses.init_pair(3, 199, -1)

  for i, opcao in enumerate(opcoes):
    if i == selecionado:
      stdscr.addstr(i+4, 2, "\u25b6 " + opcao, curses.color_pair(1))
    else:
      stdscr.addstr(i+4, 4, opcao, curses.color_pair(2))

  stdscr.addstr(0, 2, f'''
╔════════════════════════════════════════╗
║          {entidade}            ║
╚════════════════════════════════════════╝
''', curses.color_pair(3))

  stdscr.refresh()
  
#----------------------------------------------------------------------------------------------
#submenu de times
def menu_time(entidade, conn):
  func_subs = view.func_submenus.func_subs(conn)
  opcoes = [
      "1. Inserir time",
      "2. Atualizar time",
      "3. Consultar time",
      "4. Excluir time",
      "5. Remover jogador do time",
      "6. Adicionar sexto jogador",
      "7. Menu principal"
  ]
  total_opcoes = len(opcoes)
  selecionado = 0

  #configurações de terminal
  stdscr = curses.initscr()
  curses.cbreak()
  stdscr.keypad(True)
  curses.noecho()
  
  # Exibe o menu 
  exibir_submenu(stdscr, opcoes, selecionado, entidade)

  while True:
    key = stdscr.getch()

    # Movimentação para cima
    if key == curses.KEY_UP:
        selecionado = (selecionado - 1) % total_opcoes

    # Movimentação para baixo
    elif key == curses.KEY_DOWN:
        selecionado = (selecionado + 1) % total_opcoes

    # Seleciona a opção
    elif key == curses.KEY_ENTER or key == 10 or key == 13:
        break

    # Exibe o menu atualizado
    exibir_submenu(stdscr, opcoes, selecionado, entidade)

   #Restaura as configurações do terminal
  curses.nocbreak()
  stdscr.keypad(False)
  curses.echo()
  curses.endwin()

  #print("Opção selecionada: ", opcoes[selecionado])
  if(selecionado == 0):#INSERIR
    func_subs.include_time() #FUNÇÃO QUE INSERE TIMES
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    
  elif(selecionado == 1):#ATUALIZAR
    func_subs.atualizar_time() #FUNÇÃO QUE ATUALIZA TIMES
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    
  elif(selecionado == 2):#CONSULTAR
    func_subs.exibir_time() #FUNÇÃO QUE EXIBE A LISTA DE TIMES CADASTRADOS
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    
  elif(selecionado == 3):#EXCLUIR
    func_subs.excluir_time() #FUNÇÃO QUE EXCLUE TIMES
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()

  elif(selecionado == 4):#Remover jogador do time
    func_subs.remover_jogador_time()
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()

  elif(selecionado == 5):#Adicionar sexto jogador do time
    func_subs.sexto_player()
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    
  elif(selecionado == 6):#MENU PRINCIPAL
    print(cores.BLUE + "Retornando ao menu principal!" + cores.RESET)
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    return False
    #view.menu_principal.menu_principal(conn)

#----------------------------------------------------------------------------------------------
#submenu de jogador

def menu_jogador(entidade, conn):
  func_subs = view.func_submenus.func_subs(conn)
  opcoes = [
      "1. Inserir jogador",
      "2. Atualizar jogador",
      "3. Consultar jogador",
      "4. Excluir jogador",
      "5. Menu principal"
  ]
  total_opcoes = len(opcoes)
  selecionado = 0

  #configurações de terminal
  stdscr = curses.initscr()
  curses.cbreak()
  stdscr.keypad(True)
  curses.noecho()

  #exibe o menu
  exibir_submenu(stdscr, opcoes, selecionado, entidade)

  while True:
    key = stdscr.getch()

    # Movimentação para cima
    if key == curses.KEY_UP:
        selecionado = (selecionado - 1) % total_opcoes

    # Movimentação para baixo
    elif key == curses.KEY_DOWN:
        selecionado = (selecionado + 1) % total_opcoes

    # Seleciona a opção
    elif key == curses.KEY_ENTER or key == 10 or key == 13:
        break

    # Exibe o menu atualizado
    exibir_submenu(stdscr, opcoes, selecionado, entidade)

   #Restaura as configurações do terminal
  curses.nocbreak()
  stdscr.keypad(False)
  curses.echo()
  curses.endwin()

  if(selecionado == 0):#INSERIR
    func_subs.include_jogador() # FUNÇÃO QUE INSERE JOGADORES
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    
  elif(selecionado == 1):#ATUALIZAR
    func_subs.atualizar_jogador() # FUNÇÃO QUE ATUALIZA JOGADORES
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    
  elif(selecionado == 2):#CONSULTAR
    func_subs.exibir_jogador() # FUNÇÃO QUE LISTA JOGADORES CADASTRADOS
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    
  elif(selecionado == 3):#EXCLUIR
    func_subs.excluir_jogador() # FUNÇÃO QUE INSERE JOGADORES
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    
  elif(selecionado == 4):#MENU PRINCIPAL
    print(cores.BLUE + "Retornando ao menu principal!" + cores.RESET)
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    return False
    

#----------------------------------------------------------------------------------------------
#submenu de mapa
def menu_mapa(entidade, conn):
  func_subs = view.func_submenus.func_subs(conn)
  opcoes = [
      "1. Inserir mapa",
      "2. Atualizar mapa",
      "3. Consultar mapa",
      "4. Excluir mapa",
      "5. Menu principal"
  ]

  total_opcoes = len(opcoes)
  selecionado = 0

  #configurações de terminal
  stdscr = curses.initscr()
  curses.cbreak()
  stdscr.keypad(True)
  curses.noecho()

  # Exibe o menu 
  exibir_submenu(stdscr, opcoes, selecionado, entidade)

  while True:
    key = stdscr.getch()

    # Movimentação para cima
    if key == curses.KEY_UP:
        selecionado = (selecionado - 1) % total_opcoes

    # Movimentação para baixo
    elif key == curses.KEY_DOWN:
        selecionado = (selecionado + 1) % total_opcoes

    # Seleciona a opção
    elif key == curses.KEY_ENTER or key == 10 or key == 13:
        break

    # Exibe o menu atualizado
    exibir_submenu(stdscr, opcoes, selecionado, entidade)

  #Restaura as configurações do terminal
  curses.nocbreak()
  stdscr.keypad(False)
  curses.echo()
  curses.endwin()

  
  if(selecionado == 0):# INSERIR
    func_subs.include_mapa() # FUNÇÃO QUE INCLUI MAPA
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    
  elif(selecionado == 1):# ATUALIZAR 
    func_subs.atualizar_mapa() # FUNÇÃO QUE ATUALIZA O NOME DO MAPA
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    
  elif(selecionado == 2):# CONSULTAR
    func_subs.exibir_mapa() # FUNÇÃO QUE LISTA OS MAPAS CADASTRADOS
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    
  elif(selecionado == 3):# EXCLUIR
    func_subs.excluir_mapa() # FUNÇÃO QUE EXCLUI MAPA
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    
  elif(selecionado == 4):# RETORNA AO MENU PRINCIPAL
    print(cores.BLUE + "Retornando ao menu principal!" + cores.RESET)
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    return False


#----------------------------------------------------------------------------------------------
#submenu de partida

def menu_partida(entidade, conn):
  func_subs = view.func_submenus.func_subs(conn)
  opcoes = [
      "1. Inserir partida",
      "2. Atualizar partida",
      "3. Consultar partida",
      "4. Excluir partida",
      "5. Pickrate",
      "6. Menu principal"
  ]

  total_opcoes = len(opcoes)
  selecionado = 0

  #configurações de terminal
  stdscr = curses.initscr()
  curses.cbreak()
  stdscr.keypad(True)
  curses.noecho()

  # Exibe o menu 
  exibir_submenu(stdscr, opcoes, selecionado, entidade)

  while True:
    key = stdscr.getch()

    # Movimentação para cima
    if key == curses.KEY_UP:
        selecionado = (selecionado - 1) % total_opcoes

    # Movimentação para baixo
    elif key == curses.KEY_DOWN:
        selecionado = (selecionado + 1) % total_opcoes

    # Seleciona a opção
    elif key == curses.KEY_ENTER or key == 10 or key == 13:
        break

    # Exibe o menu atualizado
    exibir_submenu(stdscr, opcoes, selecionado, entidade)

  #Restaura as configurações do terminal
  curses.nocbreak()
  stdscr.keypad(False)
  curses.echo()
  curses.endwin()

  if(selecionado == 0):#INCLUIR
    func_subs.include_partida() # FUNÇÃO QUE INCLUI UMA PARTIDA
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    
  elif(selecionado == 1):#ATUALIZAR
    func_subs.atualizar_partida()# FUNÇÃO QUE ATUALIZA UMA PARTIDA
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    
  elif(selecionado == 2):#CONSULTAR
    func_subs.exibir_partida()# FUNÇÃO QUE LISTA AS PARTIDAS
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    
  elif(selecionado == 3):#EXCLUIR
    func_subs.excluir_partida() # FUNÇÃO QUE EXCLUI UMA PARTIDA
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()

  elif(selecionado == 4):
    func_subs.pickrate(conn)
    print("gráfico")
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    
  elif(selecionado == 5):
    print(cores.BLUE + "Retornando ao menu principal!" + cores.RESET)
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    return False


#----------------------------------------------------------------------------------------------
#submenu de partida individual

def menu_partida_ind(entidade, conn):
  func_subs = view.func_submenus.func_subs(conn)
  opcoes = [
      "1. Inserir partida individual",
      "2. Atualizar partida individual",
      "3. Consultar partida individual",
      "4. Excluir partida individual",
      "5. Menu principal"
  ]

  total_opcoes = len(opcoes)
  selecionado = 0

  #configurações de terminal
  stdscr = curses.initscr()
  curses.cbreak()
  stdscr.keypad(True)
  curses.noecho()

  # Exibe o menu 
  exibir_submenu(stdscr, opcoes, selecionado, entidade)

  while True:
    key = stdscr.getch()

    # Movimentação para cima
    if key == curses.KEY_UP:
        selecionado = (selecionado - 1) % total_opcoes

    # Movimentação para baixo
    elif key == curses.KEY_DOWN:
        selecionado = (selecionado + 1) % total_opcoes

    # Seleciona a opção
    elif key == curses.KEY_ENTER or key == 10 or key == 13:
        break

    # Exibe o menu atualizado
    exibir_submenu(stdscr, opcoes, selecionado, entidade)

  #Restaura as configurações do terminal
  curses.nocbreak()
  stdscr.keypad(False)
  curses.echo()
  curses.endwin()

  if(selecionado == 0):#INCLUIR
    func_subs.include_partida_ind()
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    
  elif(selecionado == 1):#ATUALIZAR
    func_subs.atualizar_partida_ind()
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    
  elif(selecionado == 2):#CONSULTAR
    func_subs.exibir_partida_ind()
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    
  elif(selecionado == 3):#EXCLUIR
    func_subs.excluir_partida_ind()
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()

  elif(selecionado == 4):
    #exibir o gráfico
    limpar()
  elif(selecionado == 5):
    print(cores.BLUE + "Retornando ao menu principal!" + cores.RESET)
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    return False


#----------------------------------------------------------------------------------------------
#submenu de administração

def menu_administracao(entidade, conn):
  func_subs = view.func_submenus.func_subs(conn)
  opcoes = [
      "1. Inserir administrador",
      "2. Atualizar administrador",
      "3. Consultar administrador",
      "4. Excluir administrador",
      "5. Menu principal"
  ]

  total_opcoes = len(opcoes)
  selecionado = 0

  #configurações de terminal
  stdscr = curses.initscr()
  curses.cbreak()
  stdscr.keypad(True)
  curses.noecho()

  # Exibe o menu 
  exibir_submenu(stdscr, opcoes, selecionado, entidade)

  while True:
    key = stdscr.getch()

    # Movimentação para cima
    if key == curses.KEY_UP:
        selecionado = (selecionado - 1) % total_opcoes

    # Movimentação para baixo
    elif key == curses.KEY_DOWN:
        selecionado = (selecionado + 1) % total_opcoes

    # Seleciona a opção
    elif key == curses.KEY_ENTER or key == 10 or key == 13:
        break

    # Exibe o menu atualizado
    exibir_submenu(stdscr, opcoes, selecionado, entidade)

  #Restaura as configurações do terminal
  curses.nocbreak()
  stdscr.keypad(False)
  curses.echo()
  curses.endwin()

  if(selecionado == 0):#INCLUIR
    func_subs.include_adm()
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    
  elif(selecionado == 1):#ATUALIZAR
    func_subs.atualizar_adm()
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    
  elif(selecionado == 2):#CONSULTAR
    func_subs.exibir_adm()
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    
  elif(selecionado == 3):#EXCLUIR
    func_subs.excluir_adm()
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    
  elif(selecionado == 4):
    print(cores.BLUE + "Retornando ao menu principal!" + cores.RESET)
    enter = input(cores.CYAN + "Pressione <ENTER> para continuar..." + cores.RESET)
    limpar()
    return False
