# coding: utf-8

''' Responsavel pela manipulaçao do banco de dados '''

from os import path
from sqlite3 import connect
from sqlite3 import IntegrityError
from settings import _ARQUIVO_BANCO_


def verifica_banco():
    ''' Checa se o banco de dados já foi criado caso nao tenha cria.'''

    if not path.isfile(_ARQUIVO_BANCO_):
        conn = connect(_ARQUIVO_BANCO_)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE usuario (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE,
                curso TEXT,
                periodo INTEGER,
                nota INTEGER
                
            );
        ''')


def registra_nota(nome, curso, periodo, nota):
    ''' Armazena nota no banco de dados'''

    try:
        conn = connect(_ARQUIVO_BANCO_)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO usuario (nome, curso, periodo, nota)
            VALUES ('%s', '%s', '%d', '%d')''' % (nome, curso, periodo, nota)
                      )
        conn.commit()
        return True
    except IntegrityError:
        return False
    finally:
        conn.close()


def get_all():
    ''' Retorna todas notas armazenadas no banco '''
    try:    
        usuario_list = []
        con = connect(_ARQUIVO_BANCO_)
        cursor = con.cursor()
        cursor.execute('SELECT * from usuario')
    
        for row in cursor.fetchall():
            usuario_list.append(
                    {'id': row[0], 'nome': row[1], 'curso': row[2],
                     'periodo': row[3], 'nota': row[4]}
            )
    
        return usuario_list
    except IntegrityError:
        return False
    finally:
        con.close()