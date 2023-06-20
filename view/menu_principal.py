import curses
from view.submenu import menu_time, menu_jogador, menu_mapa, menu_partida, menu_partida_ind, menu_administracao

#----------------------------------------------------------------------------------------------
#tela padrao do menu principal
def exibir_menu(stdscr, opcoes, selecionado):
  stdscr.clear()
  #estrutura básica do menu^^^^

  curses.start_color() #permite que cores sejam utilizadas
  curses.use_default_colors()#garante que sejam usadas as cores padrão do terminal
  
  curses.init_pair(1, 120,-1)  # Selecionado
  curses.init_pair(2, 178,-1)  # Não selecionado
  curses.init_pair(3, 141, -1) #caixa escrito menu principal
  #exibe as opcoes:
  for i, opcao in enumerate(opcoes):
      if i == selecionado:
          stdscr.addstr(i+4, 3, "\u25b6 " + opcao, curses.color_pair(1))
      else:
          '''teste = str(i)'''
          stdscr.addstr(i+4, 4, " " + opcao, curses.color_pair(2))

  stdscr.addstr(0, 2, '''
╔════════════════════════════════════════╗
║             Menu Principal             ║
╚════════════════════════════════════════╝
''', curses.color_pair(3))
  
  stdscr.refresh()

#----------------------------------------------------------------------------------------------
#Menu principal

def menu_principal(conn):  
  
  #opções do menu
  
  opcoes = [
        "1. Operações com Time",
        "2. Operações com Jogador",
        "3. Operações com Mapa",
        "4. Operações com Partida",
        "5. Operações com Partida individual",
        "6. Opções de administração",
        "7. Sair"
  ]
  total_opcoes = len(opcoes)
  selecionado = 0

  #configurações de terminal
  stdscr = curses.initscr()
  curses.cbreak()
  stdscr.keypad(True)
  curses.noecho()
  
  # Exibe o menu atualizado
  exibir_menu(stdscr, opcoes, selecionado)

  #Configurações do teclado 
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
    exibir_menu(stdscr, opcoes, selecionado)


  # Restaura as configurações do terminal
  curses.nocbreak()
  stdscr.keypad(False)
  curses.echo()
  curses.endwin()


  #Chama o submenu e utiliza-o até que a opção sair seja selecionada
  while(True):
    if(selecionado == 0):
      entidade = "       Time       "
      retorno = menu_time(entidade, conn)
      if(retorno == False):
        break
    elif(selecionado == 1):
      entidade = "      Jogador     "
      retorno = menu_jogador(entidade, conn)
      if(retorno == False):
        break
    elif(selecionado == 2):
      entidade = "       Mapa        "
      retorno = menu_mapa(entidade, conn)
      if(retorno == False):
        break
    elif(selecionado == 3):
      entidade = "     Partida      "
      retorno = menu_partida(entidade, conn)
      if(retorno == False):
        break
    elif(selecionado == 4):
      entidade = "Partida Individual"
      retorno = menu_partida_ind(entidade, conn)
      if(retorno == False):
        break
    elif(selecionado == 5):
      entidade = "   Administraçao  "
      retorno = menu_administracao(entidade, conn)
      if(retorno == False):
        break
    elif(selecionado == 6):
      print("Encerrando sistemas...")
      return False
