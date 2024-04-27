import requests
from django.shortcuts import render


def home(request):
  ##The api below allows us to access the exchange rates of currencies, cryptos & tokens  to the dolar.
  ## I chose this Api due to my interest in Finance, World Economics and Foreign affairs.
  response = requests.get(
      'https://api.fxratesapi.com/latest?api_key=fxr_live_b5eb21ba7b883b5d889760319e186a5e2a11'
  )
  data = response.json()
  KES = data['rates']['KES']
  GBP = data['rates']['GBP']
  EUR = data['rates']['EUR']
  AUD = data['rates']['AUD']
  CAD = data['rates']['CAD']
  CHF = data['rates']['CHF']
  JPY = data['rates']['JPY']
  NZD = data['rates']['NZD']
  BTC = data['rates']['BTC']
  SOL = data['rates']['SOL']
  DOT = data['rates']['DOT']

  context = {
      'KES': KES,
      'GBP': GBP,
      'EUR': EUR,
      'AUD': AUD,
      'CAD': CAD,
      'CHF': CHF,
      'JPY': JPY,
      'NZD': NZD,
      'BTC': BTC,
      'SOL': SOL,
      'DOT': DOT
  }

  return render(request, 'templates/index.html', context)
