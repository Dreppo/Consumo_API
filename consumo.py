import json

with open('Consumo_API\json\world_universities_and_domains.json', 'r', encoding='utf-8') as arquivo:
    dados_json = json.load(arquivo)

for universidade in dados_json:
    print("Nome da Universidade:", universidade["name"])
    print("Domínios:", universidade["domains"])
    print("Páginas da Web:", universidade["web_pages"])
    print("País:", universidade["country"])
    print("Código Alfa-2:", universidade["alpha_two_code"])
    print("Estado/Província:", universidade["state-province"])
    print()