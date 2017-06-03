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
        cursor.executescript('''
            CREATE TABLE usuario (
                id_usuario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome_usuario TEXT NOT NULL,
                curso TEXT,
                periodo INTEGER
            );

            CREATE TABLE vinho (
                id_vinho INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome_vinho TEXT NOT NULL UNIQUE,
                nota REAL NOT NULL,
                fixed_acidity REAL,
                volatile_acidity REAL,
                citric_acid REAL,
                residual_sugar REAL,
                chlorides REAL,
                free_sulfur_dioxide REAL,
                total_sulfur_dioxide REAL,
                density REAL,
                pH REAL,
                sulphates REAL,
                alcohol REAL,
                id_usuario INTEGER NOT NULL,
                FOREIGN KEY(id_usuario) REFERENCES usuario ON DELETE CASCADE,
                CONSTRAINT uk_vinho UNIQUE (nome_vinho, id_usuario)
            );
        ''')

        conn.close()


def executa_query(query):
    '''
    Executa uma instrução sql. Retorna o útimo id inserido caso seja uma
    operação de inserção, retorna uma lista das linhas correspondentes caso
    seja uma operação de consulta e False em caso de erro.
    '''

    # Identifica tipo de instrução sql
    tipo_instrucao = 1 if 'select' in query.lower() else 0

    try:
        conn = connect(_ARQUIVO_BANCO_)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        if tipo_instrucao == 0:
            return cursor.lastrowid
        # Retorna nome das columas e linhas recuperadas
        return next(zip(*cursor.description)), cursor.fetchall()
    except IntegrityError:
        return False
    finally:
        conn.close()


def registra_usuario(nome, curso, periodo):
    ''' Armazena usuário no banco de dados '''

    sql = '''INSERT INTO usuario (nome_usuario, curso, periodo)
            VALUES ('%s', '%s', '%d')''' % (nome, curso, periodo)

    return executa_query(sql)


def registra_vinho(**kwargs):
    ''' Armazena vinho no banco de dados '''

    columns = kwargs.keys()
    values = map(str, kwargs.values())

    sql = 'INSERT INTO vinho %s VALUES %s' % (tuple(columns), tuple(values))
    return executa_query(sql)


def busca_vinho(id):
    '''
    Busca e retorna features do vinho armazenadas no banco
    '''
    sql = 'SELECT * FROM vinho WHERE id_vinho={}'.format(id)

    # Executa instrução sql
    nome_colunas, row = executa_query(sql)

    # Retorna None ou o registro
    return None if len(row) == 0 else dict(zip(nome_colunas, row[0]))


def busca_vinho_nome(nome):
    '''
    Busca e retorna features do vinho armazenadas no banco
    '''
    sql = 'SELECT * FROM vinho WHERE nome_vinho="{}"'.format(nome)

    # Executa instrução sql
    nome_colunas, row = executa_query(sql)

    # Retorna None ou o registro
    return None if len(row) == 0 else dict(zip(nome_colunas, row[0]))


def get_ranking(limit=-1):
    '''
    Retorna vinhos e seus usuários criadores, ordenado pela nota do vinho em
    ordem decrescente. Caso seja especificado, retorna o número de linhas
    desejavéis.
    '''

    sql = '''
        SELECT usuario.id_usuario, vinho.id_vinho, usuario.nome_usuario,
        vinho.nome_vinho, curso, periodo, nota
        FROM usuario LEFT JOIN vinho on usuario.id_usuario=vinho.id_usuario
        ORDER BY nota desc
        '''
    nome_colunas, rows = executa_query(sql)

    ranking = []
    for indice, row in enumerate(rows):
        ranking.append(dict(zip(nome_colunas, row)))

        if indice == limit:
            break

    return ranking
