# Consultando a cotação do dólar em tempo real

import requests

url = requests.get("https://economia.awesomeapi.com.br/json/all/USD-BRL")

if url.status_code == 200:
    dolar = url.json()["USD"]["low"]
    print(f"O valor do dolar eh: {dolar}")
else:
    print("Erro ao buscar o valor do dolar")
