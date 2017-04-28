# coding: utf-8

''' Arquivo de configuração '''

# Path do modelo classificador.
PATH_MODEL = 'model/teste.model'

# Path do arquivo de banco de dados
_ARQUIVO_BANCO_ = 'db.sqlite'

# Configure aqui informações das features a ser utulizada no modelo classificador.
FEATURES = [
    {'nome': 'fixed_acidity', 'title': 'Acidez fixa', 'min': 3.8, 'max': 14.2},
    {'nome': 'volatile_acidity', 'title': 'Acidez volátil', 'min': 0.08, 'max': 1.1},
    {'nome': 'citric_acid', 'title': 'Ácido cítrico', 'min': 0, 'max': 1.66},
    {'nome': 'residual_sugar', 'title': 'Açúcar residual', 'min': 0.6, 'max': 65.8},
    {'nome': 'chlorides', 'title': 'Cloretos', 'min': 0.009, 'max': 0.346},
    {'nome': 'free_sulfur_dioxide', 'title': 'Dióxido de enxofre', 'min': 2, 'max': 289},
    {'nome': 'total_sulfur_dioxide', 'title': 'Dióxido de enxofre total', 'min': 9, 'max': 440},
    {'nome': 'density', 'title': 'Densidade', 'min': 0.98711, 'max': 1.03898},
    {'nome': 'pH', 'title': 'pH', 'min': 2.72, 'max': 3.82},
    {'nome': 'sulphates', 'title': 'Sulfatos', 'min': 0.22, 'max': 1.08},
    {'nome': 'alcohol', 'title': 'Álcool', 'min': 8, 'max': 14.2}

]
