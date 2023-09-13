import json

with open('Consumo_API\json\world_universities_and_domains.json', 'r') as arquivo:
    dados_json = json.load(arquivo)
    
print(dados_json)