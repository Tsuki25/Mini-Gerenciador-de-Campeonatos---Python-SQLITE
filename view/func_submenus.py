import model.administradores
import model.jogador
import model.mapa
import model.partida_individual
import model.partida
import model.times
import model.func_gerais
import matplotlib.pyplot as plt

import cores
from control.cleaner import limpar

class func_subs:
# INSTANCIANDO OBJETOS DAS DEMAIS CLASSES DO SISTEMA
  def __init__(self,conn):
    self.admin = model.administradores.Administradores(conn)
    self.team = model.times.Time(conn)
    self.player = model.jogador.Jogador(conn)
    self.mapa = model.mapa.Mapa(conn)
    self.partida = model.partida.Partida(conn)
    self.partida_ind = model.partida_individual.Partida_individual(conn)

  def lista_elos(self):
    print("Cada elo possui um valor que o representa, baseado na tabela a seguir: ")
    elos = [cores.GRAY_UNBOLD + "1 - Ferro" + cores.RESET,
            cores.RED_UNBOLD + "2 - Bronze" + cores.RESET,
            cores.GRAY_UNBOLD + "3 - Prata" + cores.RESET,
            cores.GOLD_UNBOLD + "4 - Ouro" + cores.RESET,
            cores.CYAN + "5 - Platina" + cores.RESET,
            cores.PINK + "6 - Diamante" + cores.RESET,
            cores.GREEN + "7 - Ascendente" + cores.RESET,
            cores.RED + "8 - Imortal" + cores.RESET,
            cores.GOLD + "9 - Radiante" + cores.RESET]
    for i in elos:
      print(i)
    print("\n")
  
# ------------------ ADMIN --------------------------------
  #INCLUDE
  def include_adm(self):
    nome = input("Nome do administrador: ")
    email = input("Email do Administrador: ")
    print(self.admin.inserir_administradores(nome, email))

  #READ
  def exibir_adm(self):
   self.admin.exibir_administrador()

  #EXCLUDE
  def excluir_adm(self):
    try:
      id_adm = int(input("Insira o id do administrador: "))
      print(self.admin.excluir_administrador(id_adm))
    except ValueError: 
      print(cores.GOLD + "\nALERT: Informe apenas valores válidos!")
      print("O ID informado deve ser um valor inteiro." + cores.RESET)

  #UPDATE
  def atualizar_adm(self):
    try:
      id_adm = int(input("Insira o id do administrador: "))
      dado_att = input("Informe o novo nome: ")
      print(self.admin.atualizar_administrador(id_adm, dado_att))
    except ValueError: 
      print(cores.GOLD + "\nInforme apenas valores válidos!")
      print("O ID informado deve ser um valor inteiro." + cores.RESET)


# -----------------------------------------------------------
# ------------------ JOGADOR --------------------------------
  def include_jogador_time(self, tag_time):
    try:
      self.lista_elos()
      nome = input("Nick do jogador: ")
      data_nasc = input("Data de nascimento (formato: dd/mm/aaaa): ")
      elo = int(input("Rank atual: "))
      if elo > 9 or elo < 1: print(cores.RED + "ERRO: Elo de 1 - 9" + cores.RESET)#VALIDA O ELO INFORMADO
      else: print(self.player.inserir_jogador(nome, data_nasc, elo, tag_time))   
    except ValueError: 
      print(cores.GOLD + "\nALERT: Informe apenas valores válidos!")
      print("O Elo informado deve ser um valor inteiro."  + cores.RESET)

  #INCLUDE
  def include_jogador(self):
    try:
      self.lista_elos()
      nome = input("Nick do jogador: ")
      data_nasc = input("Data de nascimento (formato: dd/mm/aaaa): ")
      tag_time = input("Tag do Time: ").upper()
      elo = int(input("Rank atual: "))
      if elo > 9 or elo < 1: print(cores.RED + "ERRO: Elo de 1 - 9"  + cores.RESET)
      else: print(self.player.inserir_jogador(nome, data_nasc, elo, tag_time))   
    except ValueError: 
      print(cores.GOLD + "\nALERT: Informe apenas valores válidos!")
      print("O Elo informado deve ser um valor inteiro." + cores.RESET)

  #READ
  def exibir_jogador(self):
    self.lista_elos()
    self.player.exibir_jogador()

  #EXCLUDE
  def excluir_jogador(self):
    try:
      id_jogador = int(input("Insira o id do jogador: "))
      print(self.player.excluir_jogador(id_jogador))
    except ValueError: 
      print(cores.GOLD + "\nALERT: Informe apenas valores válidos!")
      print("O ID informado deve ser um valor inteiro." + cores.RESET)

  #UPDATE
  def atualizar_jogador(self):
    try:
      id_jogador = int(input("Insira o id do jogador: "))
      
      while True:
        op_att = int(input(cores.GRAY + "\nQual dado deseja atualizar\n\n" + cores.RESET + cores.BLUE + "1- " + cores.RESET + "Nome do Jogador\n" + cores.BLUE + "2- " + cores.RESET + "Data de Nascimento\n" + cores.BLUE + "3- " + cores.RESET + "Elo\n" + cores.BLUE + "4- " + cores.RESET + "Voltar\n "))
        if(op_att == 1 or op_att == 2 or op_att == 3 or op_att == 4): break

      if op_att == 1: # NOME
        dado_att = input("\nInsira o novo nick: ")
        print(self.player.atualizar_jogador(id_jogador, dado_att, op_att))
      elif op_att == 2: # DATA DE NASCIMENTO
        dado_att = input("Data de nascimento (formato: dd/mm/aaaa): ")
        print(self.player.atualizar_jogador(id_jogador, dado_att, op_att))
      elif op_att == 3: # ELO
        self.lista_elos()
        dado_att = int(input("Insira o novo Elo: "))
        if dado_att > 9 or dado_att < 1: print(cores.RED + "\nERRO: Elo de 1 - 9" + cores.RESET)
        else: print(self.player.atualizar_jogador(id_jogador, dado_att, op_att))
      else: print(cores.CYAN + "\nRetornando!" + cores.RESET)
      
    except ValueError: 
      print(cores.GOLD + "\nALERT: Informe apenas valores válidos!")
      print("O ID informado deve ser um valor inteiro." + cores.RESET)


# -----------------------------------------------------------
# ---------------------- MAPA --------------------------------
  #INCLUDE
  def include_mapa(self):
    nome = input("Nome do Mapa: ").upper()
    print(self.mapa.inserir_mapa(nome))

  #READ
  def exibir_mapa(self):
   self.mapa.exibir_mapa()

  #EXCLUDE
  def excluir_mapa(self):
    try:
      id_mapa = int(input("Insira o id do mapa: "))
      print(self.mapa.excluir_mapa(id_mapa))
    except ValueError: 
      print(cores.GOLD + "\nInforme apenas valores válidos!")
      print("O ID informado deve ser um valor inteiro." + cores.RESET)

  #UPDATE
  def atualizar_mapa(self):
    try:
      id_mapa = int(input("Insira o id do mapa: "))
      dado_att = input("Informe o novo nome do mapa: ").upper()
      print(self.mapa.atualizar_mapa(id_mapa, dado_att))
    except ValueError: 
      print(cores.GOLD + "\nALERT: Informe apenas valores válidos!")
      print("O ID informado deve ser um valor inteiro." + cores.RESET)


# ---------------------------------------------------------------
# ---------------------- PARTIDA --------------------------------
  #INCLUDE
  def include_partida(self):
    try:
      while True:
        res_time1 = int(input("Placar time 1: "))
        res_time2 = int(input("Placar time 2: "))
        if res_time1 >= 0 and res_time2 >= 0: break#VERIFICA SE O VALOR INSERIDO É VÁLIDO
        else: print(cores.RED + "\nERRO: Insire um placar válido, placar maior ou iguail a 0.\n" + cores.RESET)
      mapa = int(input("Informe o id do mapa: "))
      print(self.partida.inserir_partida(res_time1, res_time2, mapa))
    except ValueError: 
      print(cores.GOLD + "\nALERT: Informe apenas valores válidos!")
      print("O ID informado deve ser um valor inteiro." + cores.RESET)

  #READ
  def exibir_partida(self):
   self.partida.exibir_partida()

  #EXCLUDE
  def excluir_partida(self):
    try:
      id_partida = int(input("Insira o id da partida: "))
      print(self.partida.excluir_partida(id_partida))
    except ValueError: 
      print(cores.GOLD + "\nInforme apenas valores válidos!")
      print("O ID informado deve ser um valor inteiro." 
+ cores.RESET)

  #UPDATE
  def atualizar_partida(self):
    try:
      id_partida= int(input("Insira o id da partida: "))
      
      while True:
        op_att = int(input(cores.GRAY + "\nQual dado deseja atualizar\n\n" + cores.RESET + cores.BLUE + "1- " + cores.RESET + " Placar time 1\n" + cores.BLUE + "2- " + cores.RESET + "Placar time 2\n" + cores.BLUE + "3- " + cores.RESET + "Mapa\n" + cores.BLUE + "4- " + cores.RESET + "Voltar\n "))
        if(op_att == 1 or op_att == 2 or op_att == 3 or op_att == 4): break

      if op_att == 1: # PLACAR TIME 01
        dado_att = int(input("\nInsira o novo placar do time 1: "))
        if dado_att < 0: return(print(cores.RED + "\nERRO: Dado inválido" + cores.RESET))# VERIFICA SE O PLACAR É VALIDO
        print(self.partida.atualizar_partida(id_partida, dado_att, op_att))
        
      elif op_att == 2: # PLACAR TIME 2
        dado_att = int(input("\nInsira o novo placar do time 2: ")) 
        if dado_att < 0: return(print(cores.RED + "\nERRO: Dado inválido" + cores.RESET))#VERIFICA SE O PLACAR É VALIDO
        print(self.partida.atualizar_partida(id_partida, dado_att, op_att))
        
      elif op_att == 3: # MAPA
        dado_att = int(input("Insira o ID do novo mapa: "))
        print(self.partida.atualizar_partida(id_partida, dado_att, op_att))
      else: print(cores.CYAN + "\nRetornando!" + cores.RESET)
        
    except ValueError: 
      print(cores.GOLD + "\nInforme apenas valores válidos!")
      print("Todos os valores devem ser do tipo inteiro." + cores.RESET)


# ------------------------------------------------------------- 
# ---------------------- TIMES --------------------------------
  #INCLUDE
  def include_time(self):
    try:
      self.lista_elos()
      tag_time = input("Tag do Time: ").upper()
      nome_time = input("Nome do Time: ")
      #elo = int(input("Elo do time: "))
      elo = 1# ELO APENAS PARA CRIAÇÃO DO TIME
      if self.team.inserir_time(tag_time, nome_time, elo) == True:
        print(cores.GREEN + "\nTime inserido com sucesso" + cores.RESET) #EXIBE A MENSAGEM AQUI, PARA PERMITIR A VERIFICAÇÃO ACIMA
        
        print("\n------ " + cores.BLUE + "Inserindo jogadores do time" + cores.RESET + "------ ")
        for i in range(5): #REALIZA A INSERÇÃO DOS JOGADORES AO TIME JÁ NA CRIAÇÃO
          print(cores.BLUE + f"\nInsira o {i+1}° Jogador" + cores.RESET)
          self.include_jogador_time(tag_time)
          limpar()
  
        print(cores.PINK + "\nEspaço para sexto jogador disponível!" + cores.RESET)
        if model.func_gerais.deseja_continuar() == True: 
          self.include_jogador_time(tag_time)

        self.team.elo_medio(tag_time) #CALCULA E SETA O ELO MEDIO DO TIME BASEADO NO ELO DOS JOGADORES
              
      else:
        print(cores.RED + "\nERRO: A TAG já está sendo utilizada." + cores.RESET)
      
    except ValueError: 
      print(cores.GOLD + "\nInforme apenas valores válidos!")
      print("O ID informado deve ser um valor inteiro." + cores.RESET)

  #READ
  def exibir_time(self):
    self.team.exibir_time()

  #EXCLUDE
  def excluir_time(self):
    try:
      tag_time = input("Insira a TAG do time: ").upper()
      print(self.team.excluir_time(tag_time))
    except ValueError: 
      print(cores.GOLD + "\nInforme apenas valores válidos!")
      print("O ID informado deve ser um valor inteiro." + cores.RESET)

  #UPDATE
  def atualizar_time(self):
    try:
      tag_time = input("Insira a TAG do time: ").upper()
      
      while True:
        op_att = int(input(cores.GRAY + "\nQual dado deseja atualizar\n\n" + cores.RESET + cores.BLUE + "1- " + cores.RESET + "Nome Time \n" + cores.BLUE + "2- " + cores.RESET + "Elo Médio \n" + cores.BLUE + "3- " + cores.RESET + "Voltar\n"))
        if(op_att == 1 or op_att == 2 or op_att == 3): break

      if op_att == 1: # Nome time
        dado_att = input("\nInsira o novo nome do time: ")
        print(self.team.atualizar_times(tag_time, dado_att, op_att))
      elif op_att == 2: # elo medio
        self.lista_elos()
        dado_att = int(input("\nInsira o novo elo: "))
        if dado_att > 9 or dado_att < 1: print(cores.RED + "\nERRO: Elo de 1 - 9" + cores.RESET)
        else: print(self.team.atualizar_times(tag_time, dado_att, op_att))
      else: print(cores.CYAN + "Retornando!" + cores.RESET)
        
    except ValueError: 
      print(cores.GOLD +"\nInforme apenas valores válidos!")
      print("Elo deve ser do tipo inteiro." + cores.RESET)

  # FUNÇÕES EXTRAS - time =================================================
  def remover_jogador_time(self):
    try:
      id_jogador = int(input("ID do jogador para remoção: "))
      tag_time = input("TAG Time para remoção: ")
      
      if self.team.jogadores_time(tag_time) == 6:
        print(self.team.remover_jogador_time(id_jogador, tag_time))
          
      else: 
        print(cores.PINK + "\nO time possui exatamente cinco jogadores para prosseguir com a remoção informe um novo jogador para completar o time\n")
        while True:
          op_att = int(input(cores.GRAY + "\nComo deseja inserir o novo jogador?\n\n" + cores.RESET + cores.BLUE + "1- " + cores.RESET + "Jogador Free Agent (FA) \n" + cores.BLUE + "2- " + cores.RESET + "Novo Jogador \n" + cores.BLUE + "3- " + cores.RESET + "Voltar\n"))
            
          #VERIFICA SE A OPÇÃO INSERIDA É VALIDA
          if (op_att == 1 or op_att == 2 or op_att == 3): break
          else: print(cores.GOLD + "ALERT: Insira apenas opções válidas." + cores.RESET)
    
        if op_att == 1: #JOGADOR FREE AGENT/SEM TIME
          new_jogador = int(input("ID do jogador FA para substituição: "))
          if (self.player.get_time(new_jogador) == 'FA'): #VERIFICA SE O TIME É O DE JOGADORES LIVRES
            print(self.team.substituir_jogador(id_jogador, tag_time, new_jogador))      
          else:
            print(cores.RED + "\nERRO: Jogador já está cadastrado em um time")
        elif op_att == 2: #JOGADOR NOVO
          limpar()
          self.team.free_agent(id_jogador)
          self.include_jogador_time(tag_time)

        else:
          print(cores.CYAN + "\nRetornando..." + cores.RESET)
            
    except ValueError: 
      print(cores.GOLD + "\nALERT: Informe apenas valores válidos!")
      print("O ID informado deve ser um valor inteiro."  + cores.RESET)

# ----------------------------------------------------------------------
  def sexto_player(self):
    try:
      tag_time = input("TAG Time para inclusão: ")
      
      if self.team.jogadores_time(tag_time) == 6:
        print(cores.GOLD + "ALERT: O time já possui seis jogadores, operação cancelada!" + cores.RESET)
          
      else: 
        print("\n----- " + cores.CYAN + "Inserindo novo jogador" + cores.RESET + " -----")
        while True:
          op_att = int(input(cores.GRAY + "\nComo deseja inserir o novo jogador?\n\n" + cores.RESET + cores.BLUE + "1- " + cores.RESET + "Jogador Free Agent (FA) \n" + cores.BLUE + "2- " + cores.RESET + "Novo Jogador \n" + cores.BLUE + "3- " + cores.RESET + "Voltar\n"))
            
          #VERIFICA SE A OPÇÃO INSERIDA É VALIDA
          if (op_att == 1 or op_att == 2 or op_att == 3): break
          else: print(cores.GOLD + "\nALERT: Insira apenas opções válidas." + cores.RESET)
    
        if op_att == 1: #JOGADOR FREE AGENT/SEM TIME
          new_jogador = int(input("ID do jogador FA para inclusão: "))
          if (self.player.get_time(new_jogador) == 'FA'): #VERIFICA SE O TIME É O DE JOGADORES LIVRES
            print(self.team.sexto_player(new_jogador, tag_time))      
          else:
            print(cores.RED + "\nERRO: Jogador já está cadastrado em um time")
        elif op_att == 2: #JOGADOR NOVO
          self.include_jogador_time(tag_time)

        else:
          print(cores.CYAN + "\nRetornando..." + cores.RESET)
            
    except ValueError: 
      print(cores.GOLD + "\nALERT: Informe apenas valores válidos!")
      print("O ID informado deve ser um valor inteiro."  + cores.RESET)

# --------------------------------------------------------------------
# ---------------------- PARTIDAS INDIVIDUAIS ------------------------
  #INCLUDE
  def include_partida_ind(self):
    try:
      id_partida = int(input("ID Partida: "))
      tag_time = input("TAG Time: ").upper()
      while True:
        placar_time = int(input("Placar time: "))
        if placar_time > 0: break#VERIFICA SE O VALOR INSERIDO É VÁLIDO
        else: print(cores.RED + "\nERRO: Insire um placar válido, placar maior ou iguai a 0.\n" + cores.RESET)
      
      data_partida = input("Data da partida (formato: dd/mm/aaaa): ")
      id_adm = int(input("ID Administrador: "))
      print(self.partida_ind.inserir_partida_individual(id_partida, tag_time,placar_time, data_partida, id_adm))
      
    except ValueError: 
      print(cores.GOLD + "\nInforme apenas valores válidos!")
      print("O ID informado deve ser um valor inteiro." + cores.RESET)

  #READ
  def exibir_partida_ind(self):
   self.partida_ind.exibir_partida_individual()

  #EXCLUDE
  def excluir_partida_ind(self):
    try:
      id_partida = int(input("ID Partida: "))
      tag_time = input("Insira a TAG do time: ").upper()
      print(self.partida_ind.excluir_registro_partida(id_partida, tag_time))
    except ValueError: 
      print(cores.GOLD + "\nInforme apenas valores válidos!")
      print("O ID informado deve ser um valor inteiro." + cores.RESET)

  #UPDATE
  def atualizar_partida_ind(self):
    try:
      id_partida = int(input("ID Partida: "))
      tag_time = input("Insira a TAG do time: ").upper()
      
      while True:
        limpar()
        op_att = int(input(cores.GRAY + "\nQual dado deseja atualizar\n\n" + cores.RESET + cores.BLUE + "1- " + cores.RESET + "Time \n" + cores.BLUE + "2- " + cores.RESET + "Placar do time\n" + cores.BLUE + "3- " + cores.RESET + "Data partida \n" + cores.BLUE + "4- " + cores.RESET + "Voltar\n"))
        if(op_att == 1 or op_att == 2 or op_att == 3 or op_att == 4): break

      if op_att == 1: # Time
        dado_att = input("Insira a nova TAG do time: ").upper()
        print(self.partida_ind.atualizar_partida_individual(id_partida, tag_time, dado_att, op_att))
      elif op_att == 2: # Placar do Time
        dado_att = int(input("Insira o novo placar: "))
        print(self.partida_ind.atualizar_partida_individual(id_partida, tag_time, dado_att, op_att))
      elif op_att == 3: # Data
        dado_att = input("Data da partida (formato: dd/mm/aaaa): ")
        print(self.partida_ind.atualizar_partida_individual(id_partida, tag_time, dado_att, op_att))
      else: print(cores.CYAN + "\nRetornando!" + cores.RESET)
        
    except ValueError: 
      print(cores.GOLD + "\nInforme apenas valores válidos!")
      print("Todos os valores devem ser do tipo inteiro." + cores.RESET)

#Gráfico pickrate-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  def pickrate(self, conn):
    cursor = conn.cursor()
    mapa = []
    cursor.execute("SELECT m.nome_mapa, count(m.id_mapa) FROM PARTIDA p INNER JOIN MAPA m ON m.id_mapa = p.id_mapa GROUP BY m.id_mapa")
    res = cursor.fetchall()
    for resp in res: #PEGA A LISTA DE DADOS DE UM ITEM
      for item in resp:
          mapa.append(item)
      
    print(mapa)
   
    nome_mapa = []
    mapa_cont = []
    tot_partidas = 0
    for i in range(len(mapa)):
      if i%2 == 0:
        nome_mapa.append(mapa[i])#PEGA O NOME DO MAPA JOGADO
      elif i%2 != 0:  
        mapa_cont.append(int(mapa[i]))#PEGA A QUANTIDADE DE VEZES QUE UM MAPA FOI JOGADO
        tot_partidas += int(mapa[i])#PEGA O TOTAL DE MAPAS JOGADOS

    for mapa in mapa_cont: # calcula a porcentagem do pickrate
      mapa = (mapa/tot_partidas) * 100

    plt.pie(mapa_cont, labels = nome_mapa, autopct='%1.1f%%')
    plt.title("Taxa de escolhas de cada mapa")
    plt.show()

    
    


    