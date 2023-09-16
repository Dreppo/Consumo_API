import json
import webbrowser
import re

with open('json\world_universities_and_domains.json', 'r', encoding='utf-8') as arquivo:
    dados_json = json.load(arquivo)

lista_nomes = []
lista_siglas = []
dic_exemplo1 = {}
dic_exemplo2 = {}

def lista_n():
    for universidade in dados_json:
        if universidade["country"] not in lista_nomes:
            lista_nomes.append(universidade["country"])
    
    print(lista_nomes)

def lista_s():
    for universidade in dados_json:
        if universidade["alpha_two_code"] not in lista_siglas:
            lista_siglas.append(universidade["alpha_two_code"])
    print(lista_siglas)
    
def mostrar_dic1(str1 , x):
    for universidade in dados_json:
        if universidade["country"] == str1:
            x = x + 1
            dic_exemplo1[x] = {x:[universidade["name"],universidade["web_pages"]]}
    for itens in dic_exemplo1.values():
        print(itens)           
            
def mostrar_dic2(str2,x):
    for universidade in dados_json:
        if universidade["alpha_two_code"] == str2:
            x = x + 1
            dic_exemplo2[x] = {x:[universidade["name"],universidade["web_pages"]]}
    for itens in dic_exemplo2.values():
        print(itens) 
        
def mostrar_escolha(dic, id):
    if id in dic:
        nome_universidade, link = dic[id][id][0], dic[id][id][1]
        print(f"Nome da Universidade: {nome_universidade}")
        print(f"Link da Universidade: {link[0]}")
        try:
            webbrowser.open(link[0])
        except Exception:
            print("Não foi possivel acessar o Site")
    else:
        print("Universidade não encontrada")

    
    

def escolha1():
    opc = 0
    while opc != 3:
        print("1 - Procurar Pelo Pais")
        print("2 - Procurar Pela sigla do Pais Ex: BR(Brazil)")
        print("3 - Voltar")     
        escolha = int(input("digite um número para fazer uma ação: "))
        opc = escolha
        match opc :
            case 1:
                lista_n()
                busca = str(input("Digite o nome do país: "))
                if busca not in lista_nomes:
                    print("Digite um nome valido para a pesquisa")
                mostrar_dic1(busca, 0)
                id = int(input("Digite o Número da Universidade que deseja ver: "))  
                mostrar_escolha(dic_exemplo1,id) 
                print()
            case 2:
                lista_s()
                aux = str(input("Digite a sigla do país: "))
                busca = aux.upper()
                if busca not in lista_siglas:
                    print("Digite uma sigla valida para a pesquisa: ")
                else:
                    mostrar_dic2(busca, 0)
                    id = int(input("Digite o Número da Universidade que deseja ver: "))  
                    mostrar_escolha(dic_exemplo2,id) 
             
                

def escolha2(str2):
    for universidade in dados_json:
        nome_universidade = universidade["name"]
        if re.search(re.escape(str2), nome_universidade, re.IGNORECASE):
            print ("Nome: ", nome_universidade)
            print ("País: ", universidade["country"])
            print ("Sigla do País: ", universidade["alpha_two_code"])
            web_pages = ", ".join(universidade["web_pages"])
            print("Sites da Universidade:", web_pages)
                
def escolha3(str3):
    for universidade in dados_json:
        for url in universidade["web_pages"]:
            if re.search(re.escape(str3), url, re.IGNORECASE):
                webbrowser.open(url)
                return
    print("Universidade não encontrada")
                

def menu():
    opc = 0
    while opc != 4:
        print("Bem vindo a busca por universidades pelo mundo")
        print("----------------------------------------------")
        print("1 - Procurar universidades pelo país")
        print("2 - Procurar universidades pelo nome")
        print("3 - Procurar site de uma universidade")
        print("4 - Sair")
        print("----------------------------------------------")
        escolha = int(input("digite um número para fazer uma ação: "))
        opc = escolha
        match opc :
            case 1:
                escolha1()
            case 2:
                busca = str(input("Digite o nome da Universidade: "))
                escolha2(busca)
            case 3:
                busca1 = str(input("Digite o link para o site da Universidade: "))
                escolha3(busca1)

    




menu()
