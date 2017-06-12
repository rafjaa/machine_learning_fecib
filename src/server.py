# coding: utf-8

''' Servidor '''
from db import registra_usuario, registra_vinho
from db import verifica_banco, get_ranking
from db import busca_vinho_nome, busca_vinho

from flask import render_template
from flask import Flask, redirect, url_for
from flask import request

from settings import PATH_MODEL, FEATURES

from sklearn.externals import joblib

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from math import log
import numpy as np

# Servidor HTTP
app = Flask(__name__)
app.debug = True


def media_features():
    '''
    calcula média dos valores das features
    '''
    for i in range(len(FEATURES)):
        FEATURES[i]['media'] = round(
            (FEATURES[i]['max'] + FEATURES[i]['min']) / 2., 3)


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

    X = [[round(float(kwargs[e['nome']]), 2) for e in FEATURES]]

    return model.predict(X)[0]


@app.route('/', methods=["GET"])
def inicial():
    '''
    Exibe tela inicial com classificação dos vinhos produzidos pelos usuário.
    '''
    # Recebe lista com usuários cadastrados e ordena em ordem decrescente
    users = get_ranking()

    return render_template(
        'ranking.html', users=users, total=len(users)
    )


@app.route('/novovinho', methods=["GET"])
def novo_vinho(mensagem=''):
    '''
    Exibe tela para cadastro de um novo vinho
    '''
    return render_template(
        'novovinho.html',
        features=FEATURES,
        mensagem=mensagem
    )


@app.route('/', methods=["POST"])
def processa():
    '''
    Classifica o vinho e resgistra nota.
    '''
    form_data = request.form.to_dict()

    # Verifica vinho repetido
    if busca_vinho_nome(form_data['nome_vinho']):
        msg = '* O vinho que você tentou cadastrar já existe'
        return novo_vinho(msg)

    # Obtém e registra usuário
    nome = form_data.pop('nome')
    curso = form_data.pop('curso')
    periodo = form_data.pop('periodo')

    # Verifica se foi inserido período
    periodo = 0 if len(periodo) == 0 else int(periodo)

    id_usuario = registra_usuario(nome, curso, periodo)

    # Avalia caracteristicas e registra a nota do vinho
    nota = avalia_feature(**form_data)

    form_data['nota'] = round(nota, 4)
    form_data['id_usuario'] = id_usuario
    registra_vinho(**form_data)

    return redirect(url_for('inicial', id=id_usuario))


@app.route('/grafico', methods=['GET'])
def exibe_grafico():
    ''' Exibe um gráfico interativo 3D do resultado'''

    users = get_ranking()

    if len(users) < 4:
        return inicial()

    fig = plt.figure(figsize=(15, 10))
    ax = fig.add_subplot(111, projection='3d')

    color_sequence = ['#0404B4', '#B40404', '#088A08', '#FFFF00', '#151515',
                      '#01DFD7', '#F7BE81', '#ff9896', '#82FA58', '#FE2E2E',
                      '#c49c94']

    legend = []
    vinho = None
    for z, user in zip(range(1, 5), users):

        # Busca features do vinho do usuário
        vinho = busca_vinho(user['id_vinho'])

        # Remove Parâmetros não usados
        for atr in ['nome_vinho', 'id_vinho', 'nota', 'id_usuario']:
            del vinho[atr]

        # Ordena e obtém features
        vinho = sorted(vinho.items(), key=lambda x: x[0])

        xs = np.arange(1, 12)
        ys = [y[1] for y in vinho]

        # Aplica log (y+1), base 2
        ys_scale_log = [log(y + 1, 2) for y in ys]

        ax.bar(xs, ys_scale_log, zs=z, zdir='y',
               color=color_sequence, alpha=0.8)

        # Adiciona legenda e rotulos
        for i, x, y, y_log in zip(range(len(ys)), xs, ys, ys_scale_log):
            legend.append(plt.Rectangle((0, 0), 1, 1, fc=color_sequence[i]))

            # rótulos
            ax.text(x, z, y_log, '%2.1f' % y, ha='center', va='bottom')

    ax.set_title('Resultado')
    ax.set_xticklabels('')
    ax.set_zticklabels('')
    ax.set_yticklabels(['1°', '', '2°', '', '3°', '', '4°'])

    ax.set_xlabel('Parâmetros')
    ax.set_zlabel('Valores')
    ax.set_ylabel('Posição')

    ax.legend(legend, [x['title'] for x in FEATURES])

    plt.show()
    # return inicial()
    return redirect(url_for('inicial'))


@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('inicial'))


if __name__ == "__main__":
    verifica_banco()
    media_features()
    app.run(host='0.0.0.0')
