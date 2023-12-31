import sqlite3 

def dados_banco(conn):
  cursor = conn.cursor()
  # SE NÃO HÁ ADMINISTRADORES CADASTRADOS, ENTÃO O BANCO NÃO FOI INICIADO
  cursor.execute("""
    SELECT * FROM administrador;
  """)
  res = cursor.fetchall() 
  if res == None or res == "" or len(res) == 0:#Se o id não existir
     return False
  else: 
     return True

def dados_init(conn):
  cursor = conn.cursor()
  # INSERE O TIME PARA JOGADORES QUE FICARAM SEM TIME APÓS SEREM CADASTRADOS. 
  cursor.execute("""
  INSERT INTO time VALUES ('FA','FREE AGENT', 0);
  """)
  conn.commit()

  #INSERE UM ADMINISTRADOR PADRÃO
  cursor.execute("INSERT INTO administrador VALUES (?, 'ADMIN', 'admin@gmail.com');",(None,))
  conn.commit()

  # INSERE ALGUNS TIMES PARA DEMONSTRAÇÃO DO PROJETO
  cursor.execute("INSERT INTO time VALUES ('EXP','EXEMPLO', '1'),('TST','TESTES', '2');")
  conn.commit()

  # INSERE ALGUNS JOGADORES PARA DEMONSTRAÇÃO DO PROJETO
  cursor.execute("""
    INSERT INTO jogador (nome, data_nasc, elo, tag_time) VALUES 
    ('EXP APOSTROFO', '06/03/1995',1, 'EXP'),
    ('EXP FULL', '02/08/1999',1, 'EXP'),
    ('EXP ZYUT', '25/01/2000',1, 'EXP'),
    ('EXP NIZNAUAC', '16/07/2001',1, 'EXP'),
    ('EXP MATHIAS', '01/01/1990',1, 'EXP'),
    ('TST FNS', '07/03/1989',2, 'TST'),
    ('EXP VIKTOR', '02/09/1994',2, 'TST'),
    ('EXP XAND', '28/03/2002',1, 'TST'),
    ('EXP DIMAS', '19/05/2004',2, 'TST'),
    ('EXP ALEX', '03/07/1997',2, 'TST'),
    ('COLD', '02/09/1997',9, 'FA');
  """)
  conn.commit()

  # INSERE ALGUNS MAPAS PARA DEMONSTRAÇÃO DO PROJETO
  cursor.execute("""
    INSERT INTO mapa (nome_mapa) VALUES 
    ('ASCENT'),
    ('BIND'),
    ('PEARL'),
    ('LOTUS');
  """)
  conn.commit()

  # INSERE ALGUNS PARTIDA PARA DEMONSTRAÇÃO DO PROJETO
  cursor.execute("""
    INSERT INTO partida (res_time_01, res_time_02, id_mapa) VALUES 
    (13, 2, 1),
    (13, 11, 2),
    (14, 12, 3),
    (9, 13, 4);
  """)
  conn.commit()

  # INSERE ALGUNS PARTIDA-INDIVIDUAL PARA DEMONSTRAÇÃO DO PROJETO
  cursor.execute("""
    INSERT INTO partida_individual VALUES 
    (1, 'EXP', 13, '20/06/2023', 1),
    (1, 'TST', 2, '20/06/2023', 1),
    (2, 'EXP', 13, '20/06/2023', 1),
    (2, 'TST', 11, '20/06/2023', 1),
    (3, 'EXP', 14, '20/06/2023', 1),
    (3, 'TST', 12, '20/06/2023', 1),
    (4, 'EXP', 09, '15/05/2023', 1),
    (4, 'TST', 13, '15/05/2023', 1);
  """)
  conn.commit()