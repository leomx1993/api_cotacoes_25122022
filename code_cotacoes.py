# bibliotecas -> Pandas p/ df e Flask p/ contrução da API:

import pandas as pd
from flask import Flask, jsonify

cotacoes = pd.read_csv(r'C:\Users\Leonardo Xavier\Desktop\api_cotacoes\cotacoes_25_12_2022.csv',sep=';')
print(cotacoes)

# Inicializando aplicativo:

app = Flask(__name__)

# Funcionalidades:

#Sempre utilizar um decorator "@app.route" p/ cada página

@app.route('/')
def homepage_api():
  return 'Olá, essa API fornece as cotacoes do dólar, euro e yuan'

@app.route('/dolar')
def cotacao_dolar():
  cot_dol = cotacoes['Cotacao'][0]
  resposta = {'cotacao_dolar': cot_dol}
  return jsonify(resposta)

@app.route('/euro')
def cotacao_euro():
  cot_eur = cotacoes['Cotacao'][1]
  resposta = {'cotacao_euro': cot_eur}
  return jsonify(resposta)

@app.route('/yuan')
def cotacao_yuan():
  cot_eur = cotacoes['Cotacao'][2]
  resposta = {'cotacao_yuan': cot_eur}
  return jsonify(resposta)

# rodar app:
app.run()











