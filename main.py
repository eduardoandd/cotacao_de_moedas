import requests
import json

request = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

cotacao=request.json()

cotacao_btc=cotacao['BTCBRL']['bid']
cotacao_dolar=cotacao['USDBRL']['bid']
cotacao_euro=cotacao['EURBRL']['bid']