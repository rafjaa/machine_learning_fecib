# coding: utf-8

''' Arquivo de configuração '''

# Path do modelo classificador.
PATH_MODEL = 'model/model.pk1'

# Path do arquivo de banco de dados
_ARQUIVO_BANCO_ = 'db.sqlite'

'''
Configure aqui informações das features a ser utulizada
no modelo classificador. Obs.: máximo de 3 casas decimais.
'''
FEATURES = [
    {'nome': 'fixed_acidity', 'title': 'Acidez fixa', 'min': 3.8, 'max': 14.2},
    {'nome': 'volatile_acidity', 'title': 'Acidez volátil', 'min': 0.12, 'max': 1.58},
    {'nome': 'citric_acid', 'title': 'Ácido cítrico', 'min': 0, 'max': 1},
    {'nome': 'residual_sugar', 'title': 'Açúcar residual', 'min': 0.9, 'max': 15.5},
    {'nome': 'chlorides', 'title': 'Cloretos', 'min': 0.012, 'max': 0.611},
    {'nome': 'free_sulfur_dioxide', 'title': 'Dióxido de enxofre', 'min': 1, 'max': 72},
    {'nome': 'total_sulfur_dioxide', 'title': 'Dióxido de enxofre total', 'min': 6, 'max': 289},
    {'nome': 'density', 'title': 'Densidade', 'min': 0.991, 'max': 1.003},
    {'nome': 'pH', 'title': 'pH', 'min': 2.74, 'max': 4.01},
    {'nome': 'sulphates', 'title': 'Sulfatos', 'min': 0.33, 'max': 2},
    {'nome': 'alcohol', 'title': 'Álcool', 'min': 8.4, 'max': 14.9}

]
