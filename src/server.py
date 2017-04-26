# coding: utf-8

from db import registra_nota, verifica_banco, get_all

from flask import render_template
from flask import Flask
from flask import request

from settings import PATH_MODEL, FEATURES

from sklearn.externals import joblib

# Servidor HTTP
app = Flask(__name__)
app.debug = True


def load_model(path_model=PATH_MODEL):
    '''
    Carrega e retorna o modelo treinado, salvo em disco, especificado no
    arquivo de configuraçao (settings.py).
    '''
    return joblib.load(path_model)


def avalia_feature(**kwargs):
    '''
    Realiza uma avaliaçao.Recebe como parâmetro um dicionarios de features.
    '''
    # Carrega classificador.
    model = load_model()

    X = [[kwargs[e['nome']] for e in FEATURES]]

    return model.predict(X)


@app.route('/', methods=["GET"])
def inicial():
    '''
    Exibe tela inicial com classificação dos vinhos produzidos pelos usuário.
    '''
    # Recebe lista com usuários cadastrados e ordena em ordem decrescente
    users = get_all()
    users = sorted(users, key=lambda x: x['nota'], reverse=True)
    
    return render_template('index.html', users=users, features=FEATURES, posicao='pesquisa')


@app.route('/', methods=["POST"])
def processa():
    '''
    Classifica o vinho e resgistra nota.
    '''
    form_data = request.form.to_dict()
    
    # Obtém identificação do usuário
    nome = form_data.pop('nome')
    curso = form_data.pop('curso')
    periodo = int(form_data.pop('periodo'))
    
    # Avalia caracteristicas e registra a nota retornada pelo classificador
    nota = avalia_feature(**form_data)
    registra_nota(nome, curso, periodo, nota)
    
    # Recebe lista com usuários cadastrados e a ordena em ordem decrescente
    users = get_all()
    users = sorted(users, key=lambda x: x['nota'], reverse=True)
    
    # Recupera posição do usuário no ranking
    posicao = users.index(max(users, key=lambda x: x['id'])) + 1

    return render_template('index.html', users=users, features=FEATURES, posicao=posicao)


if __name__ == "__main__":
    verifica_banco()
    app.run()