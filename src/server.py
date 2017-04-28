# coding: utf-8

''' Servidor '''
from db import registra_usuario, registra_vinho, verifica_banco, get_ranking

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
    users = get_ranking()

    return render_template('index.html', users=users, features=FEATURES, posicao='pesquisa')


@app.route('/', methods=["POST"])
def processa():
    '''
    Classifica o vinho e resgistra nota.
    '''
    form_data = request.form.to_dict()

    # Obtém e registra usuário
    nome = form_data.pop('nome')
    curso = form_data.pop('curso')
    periodo = int(form_data.pop('periodo'))

    id_usuario = registra_usuario(nome, curso, periodo)

    # Avalia caracteristicas e registra a nota do vinho
    nota = int(avalia_feature(**form_data))
    form_data['nota'] = nota
    form_data['id_usuario'] = id_usuario
    id_vinho = registra_vinho(**form_data)

    users = get_ranking()
    return render_template('index.html', users=users, features=FEATURES, posicao=id_vinho)


if __name__ == "__main__":
    verifica_banco()
    app.run()
