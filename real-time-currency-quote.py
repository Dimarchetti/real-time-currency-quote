import time
import requests
import json
import datetime


while True:
  req = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')

  cotacao = json.loads(req.text)

  print('#### COTAÇÃO ####')

  print('Cotação do Dólar hoje às: ', datetime.datetime.now(), cotacao['USDBRL']['bid'])

  req = requests.get('https://economia.awesomeapi.com.br/last/EUR-BRL')

  cotacao = json.loads(req.text)

  print('Cotação do Euro hoje  às: ', datetime.datetime.now(), cotacao['EURBRL']['bid'])

  req = requests.get('https://economia.awesomeapi.com.br/last/BTC-BRL')

  cotacao = json.loads(req.text)
  print('Cotação do Bitcoin hoje às ', datetime.datetime.today(), cotacao['BTCBRL']['bid'])
  time.sleep(5)