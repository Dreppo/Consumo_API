import json
import webbrowser

with open('Consumo_API\json\world_universities_and_domains.json', 'r', encoding='utf-8') as arquivo:
    dados_json = json.load(arquivo)

def verificacao_de_escolha(num1,num2):
    if escolha < num1:
        print("Digite um número valido")   
    elif escolha > num2:
        print("Digite um número valido")
        

def menu():
    opc = 0
    while opc != 4:
        print("Bem vindo a busca por universidades pelo mundo")
        print("----------------------------------------------")
        print("1 - Procurar universdades pelo país")
        print("2 - Procurar universidades pelo nome")
        print("3 - Procurar site de uma universidade")
        print("4 - Sair")
        print("----------------------------------------------")
        escolha = int(input("digite um número para fazer uma ação: "))
        opc = escolha
        print("")        

def escolha1(escolha):
    opc = 0
    while opc != 3:
        print("1 - Procurar Pelo nome do Pais")
        print("2 - Procurar Pela sigla do Pais  Ex: BR(Brasil)")
        print("3 - Voltar")
    




menu()