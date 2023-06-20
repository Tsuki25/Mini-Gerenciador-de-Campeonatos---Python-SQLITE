import sqlite3
from sqlite3 import Error
import cores

def criar_banco(banco):
  conn = sqlite3.connect(banco)
  c = conn.cursor()


  try:
    #TABELA TIME
    c.execute("""
      CREATE TABLE IF NOT EXISTS "time"(
        "tag_time" TEXT NOT NULL,
        "nome_time" TEXT NOT NULL,
        "elo_medio" INTEGER NOT NULL,
        PRIMARY KEY("tag_time")
      );
    """)

    # TABELA DE ADMINISTRADOR
    c.execute("""
      CREATE TABLE IF NOT EXISTS "administrador"(
        "id_adm" INTEGER NOT NULL,
        "nome" TEXT NOT NULL,
        "email" TEXT NOT NULL UNIQUE,
        PRIMARY KEY("id_adm" AUTOINCREMENT)
      );
    """)

        # TABELA DE MAPA
    c.execute("""
      CREATE TABLE IF NOT EXISTS "mapa"(
        "id_mapa" INTEGER NOT NULL,
        "nome_mapa" TEXT NOT NULL UNIQUE,
        PRIMARY KEY("id_mapa" AUTOINCREMENT)
      );
    """)

    
    #TABELA JOGADOR
    c.execute("""
      CREATE TABLE IF NOT EXISTS "jogador"(
        "id_jogador" INTEGER NOT NULL, 
        "nome" TEXT NOT NULL UNIQUE, 
        "data_nasc" DATE NOT NULL,
        "elo" INTEGER NOT NULL,
        "tag_time" INTERGER,
        PRIMARY KEY("id_jogador" AUTOINCREMENT),
        FOREIGN KEY ("tag_time") REFERENCES "time"("tag_time")
      );
    """)

     # TABELA PARTIDA
    c.execute("""
      CREATE TABLE IF NOT EXISTS "partida"(
        "id_partida" INTEGER NOT NULL,
        "res_time_01" INTEGER NOT NULL,
        "res_time_02" INTEGER NOT NULL,
        "id_mapa" INTEGER NOT NULL,
        PRIMARY KEY("id_partida" AUTOINCREMENT),
        FOREIGN KEY("id_mapa") REFERENCES "mapa" ("id_mapa")
      );
    """)

    #TABELA PARTIDA_INDIVIDUAL
    c.execute("""
      CREATE TABLE IF NOT EXISTS "partida_individual"(
        "id_partida" INTEGER NOT NULL,
        "tag_time" INTEGER NOT NULL,
        "placar_time" INTEGER NOT NULL,
        "data_partida" DATE NOT NULL,
        "id_adm" INTEGER NOT NULL,
        PRIMARY KEY("id_partida", "tag_time"),
        FOREIGN KEY ("id_partida") REFERENCES "partida" ("id_partida")ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY ("tag_time") REFERENCES "time"("tag_time")
        ON DELETE CASCADE 
        ON UPDATE CASCADE
      );
    """)

    print(cores.GREEN + "Tabelas criadas com sucesso!\n" + cores.RESET)
    return conn

  except Error as e:
    print(e)
  
    
