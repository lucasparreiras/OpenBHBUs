# app.py

from flask import Flask
from flask import jsonify
from flask import request
from flask import redirect
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'database'
app.config['MONGO_URI'] = 'connection'

mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def home():
  return redirect("https://lucasparreiras.github.io/feedreader/", code=302)

@app.route('/linhas/BuscarTarifa', methods=['GET'])
def get_all_tarifa():
  linha = mongo.db.tarifas
  output = []
  for s in linha.find():
    output.append({'COD_LINH' : s['COD_LINH'], 'NUM_EMPR' : s['NUM_EMPR'], 'DES_TIPO_TARI' : s['DES_TIPO_TARI'], 'NOM_LINH' : s['NOM_LINH'], 'VAL_TARI' : s['VAL_TARI'], 'DAT_VIGE_PLLH' : s['DAT_VIGE_PLLH'], 'TIP_TRAN' : s['TIP_TRAN']})
  return jsonify({'result' : output})

@app.route('/linhas/BuscarTarifa/<string:cod_linha>', methods=['GET'])
def get_one_tarifa(cod_linha):
  linha = mongo.db.tarifas
  output = []
  s = linha.find_one({'COD_LINH' : cod_linha})
  if s:
    output = {'COD_LINH' : s['COD_LINH'], 'NUM_EMPR' : s['NUM_EMPR'], 'DES_TIPO_TARI' : s['DES_TIPO_TARI'], 'NOM_LINH' : s['NOM_LINH'], 'VAL_TARI' : s['VAL_TARI'], 'DAT_VIGE_PLLH' : s['DAT_VIGE_PLLH'], 'TIP_TRAN' : s['TIP_TRAN']}
  else:
    output = "Linha de onibus nao encontrada."
  return jsonify({'result' : output})

@app.route('/linhas/BuscarItinerario', methods=['GET'])
def get_all_itinerario():
  linha = mongo.db.itinerarios
  output = []
  for s in linha.find():
    output.append({'COD_LINH' : s['COD_LINH'], 'NUM_SUBL' : s['NUM_SUBL'], 'NUM_PONT_CTRL' : s['NUM_PONT_CTRL'], 'NUM_SEQU_ITIN' : s['NUM_SEQU_ITIN'], 'DAT_VIGE_ESPF' : s['DAT_VIGE_ESPF'], 'NOM_LINH' : s['NOM_LINH'], 'NOM_SUBL' : s['NOM_SUBL'], 'DES_PONT_CTRL' : s['DES_PONT_CTRL'], 'NOM_MUNC' : s['NOM_MUNC'], 'TIP_LOGR' : s['TIP_LOGR'], 'NOM_LOGR' : s['NOM_LOGR'], 'TIP_TRAN' : s['TIP_TRAN']})
  return jsonify({'result' : output})

@app.route('/linhas/BuscarItinerario/<string:cod_linha>', methods=['GET'])
def get_one_itinerario(cod_linha):
  linha = mongo.db.itinerarios
  output = []
  for s in linha.find({'COD_LINH' : cod_linha}):  
    output.append({'COD_LINH' : s['COD_LINH'], 'NUM_SUBL' : s['NUM_SUBL'], 'NUM_PONT_CTRL' : s['NUM_PONT_CTRL'], 'NUM_SEQU_ITIN' : s['NUM_SEQU_ITIN'], 'DAT_VIGE_ESPF' : s['DAT_VIGE_ESPF'], 'NOM_LINH' : s['NOM_LINH'], 'NOM_SUBL' : s['NOM_SUBL'], 'DES_PONT_CTRL' : s['DES_PONT_CTRL'], 'NOM_MUNC' : s['NOM_MUNC'], 'TIP_LOGR' : s['TIP_LOGR'], 'NOM_LOGR' : s['NOM_LOGR'], 'TIP_TRAN' : s['TIP_TRAN']})
  if not output:
    output = "Linha de onibus nao encontrada."
  return jsonify({'result' : output})

@app.route('/linhas/BuscarHorarioDiaUtil', methods=['GET'])
def get_all_h_util():
  output = []
  output = get_all_horarios('h_dia_util')
  return jsonify({'result' : output})
  
@app.route('/linhas/BuscarHorarioDiaUtil/<string:cod_linha>', methods=['GET'])
def get_one_h_util(cod_linha):
  output = []
  output = get_one_horario(cod_linha, 'h_dia_util')
  return jsonify({'result' : output})

@app.route('/linhas/BuscarHorarioSabado', methods=['GET'])
def get_all_h_sabado():
  output = []
  output = get_all_horarios('h_sabado')
  return jsonify({'result' : output})
  
@app.route('/linhas/BuscarHorarioSabado/<string:cod_linha>', methods=['GET'])
def get_one_h_sabado(cod_linha):
  output = []
  output = get_one_horario(cod_linha, 'h_sabado')
  return jsonify({'result' : output})

@app.route('/linhas/BuscarHorarioDomingoFeriado', methods=['GET'])
def get_all_h_domingo():
  output = []
  output = get_all_horarios('h_domingo')
  return jsonify({'result' : output})
  
@app.route('/linhas/BuscarHorarioDomingoFeriado/<string:cod_linha>', methods=['GET'])
def get_one_h_domingo(cod_linha):
  output = []
  output = get_one_horario(cod_linha, 'h_domingo')
  return jsonify({'result' : output})

@app.route('/linhas/BuscarHorarioDiaAtipico', methods=['GET'])
def get_all_h_atipico():
  output = []
  output = get_all_horarios('h_atipico')
  return jsonify({'result' : output})
  
@app.route('/linhas/BuscarHorarioDiaAtipico/<string:cod_linha>', methods=['GET'])
def get_one_h_atipico(cod_linha):
  output = []
  output = get_one_horario(cod_linha, 'h_atipico')
  return jsonify({'result' : output})

def select_table(tipo_dia):
  if tipo_dia == 'h_dia_util':
    return mongo.db.h_dia_util
  elif tipo_dia == 'h_sabado':
    return mongo.db.h_sabado
  elif tipo_dia == 'h_domingo':
    return mongo.db.h_domingo
  elif tipo_dia == 'h_atipico':
    return mongo.db.h_atipico

def get_all_horarios(tipo_dia):
  linha = select_table(tipo_dia)
  output = []
  for s in linha.find():
    output.append({'COD_LINH' : s['COD_LINH'], 'NUM_SUBL' : s['NUM_SUBL'], 'DES_PONT_CTRL' : s['DES_PONT_CTRL'], 'DES_TIPO_DIA' : s['DES_TIPO_DIA'], 'HOR_SAID_VIAG' : s['HOR_SAID_VIAG'], 'MIN_SAID_VIAG' : s['MIN_SAID_VIAG'], 'NOM_LINH' : s['NOM_LINH'], 'NOM_SUBL' : s['NOM_SUBL'], 'DAT_VIGE_ESPF' : s['DAT_VIGE_ESPF'], 'IND_VEIC_ESPC' : s['IND_VEIC_ESPC'], 'TIP_TRAN' : s['TIP_TRAN'] })
  return output

def get_one_horario(cod_linha, tipo_dia):
  linha = select_table(tipo_dia)
  output = []
  for s in linha.find({'COD_LINH' : cod_linha}):
    output.append({'COD_LINH' : s['COD_LINH'], 'NUM_SUBL' : s['NUM_SUBL'], 'DES_PONT_CTRL' : s['DES_PONT_CTRL'], 'DES_TIPO_DIA' : s['DES_TIPO_DIA'], 'HOR_SAID_VIAG' : s['HOR_SAID_VIAG'], 'MIN_SAID_VIAG' : s['MIN_SAID_VIAG'], 'NOM_LINH' : s['NOM_LINH'], 'NOM_SUBL' : s['NOM_SUBL'], 'DAT_VIGE_ESPF' : s['DAT_VIGE_ESPF'], 'IND_VEIC_ESPC' : s['IND_VEIC_ESPC'], 'TIP_TRAN' : s['TIP_TRAN'] })
  if not output:
    output = "Linha de onibus nao encontrada."
  return output


@app.route('/linhas/tarifa', methods=['POST'])
def add_tarifa():
  linha = mongo.db.tarifas
  COD_LINH = request.json['COD_LINH']
  NUM_EMPR = request.json['NUM_EMPR']
  DES_TIPO_TARI = request.json['DES_TIPO_TARI']
  NOM_LINH = request.json['NOM_LINH']
  VAL_TARI = request.json['VAL_TARI']
  DAT_VIGE_PLLH = request.json['DAT_VIGE_PLLH']
  TIP_TRAN = request.json['TIP_TRAN']
  linha_id = linha.insert({'COD_LINH' : COD_LINH, 'NUM_EMPR' : NUM_EMPR, 'DES_TIPO_TARI' : DES_TIPO_TARI, 'NOM_LINH' : NOM_LINH, 'VAL_TARI' : VAL_TARI, 'DAT_VIGE_PLLH' : DAT_VIGE_PLLH, 'TIP_TRAN' : TIP_TRAN})
  new_linha = linha.find_one({'_id': linha_id })
  output = {'COD_LINH' : new_linha['COD_LINH'], 'NUM_EMPR' : new_linha['NUM_EMPR'], 'DES_TIPO_TARI' : new_linha['DES_TIPO_TARI'], 'NOM_LINH' : new_linha['NOM_LINH'], 'VAL_TARI' : new_linha['VAL_TARI'], 'DAT_VIGE_PLLH' : new_linha['DAT_VIGE_PLLH'], 'TIP_TRAN' : new_linha['TIP_TRAN']}
  return jsonify({'result' : output})
  
if __name__ == '__main__':
    app.run(debug=True)
