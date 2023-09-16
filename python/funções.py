import json
import webbrowser
import re

lista_nomes = []
lista_siglas = []
dicionario_nomes = {}
dicionario_siglas = {}

with open('json/world_universities_and_domains.json', 'r', encoding='utf-8') as arquivo:
    dados_json = json.load(arquivo)

def adicionar_lista_nomes():
    for universidade in dados_json:
        if universidade["country"] not in lista_nomes:
            lista_nomes.append(universidade["country"])
    print(lista_nomes)

def adicionar_lista_siglas():
    for universidade in dados_json:
        if universidade["alpha_two_code"] not in lista_siglas:
            lista_siglas.append(universidade["alpha_two_code"])
    print(lista_siglas)
    
def adicionar_dicionario1(str1 , x):
    for universidade in dados_json:
        if universidade["country"] == str1:
            x = x + 1
            dicionario_nomes[x] = {x:[universidade["name"],universidade["web_pages"]]}
    for itens in dicionario_nomes.values():
        print(itens)           
            
def adicionar_dicionario2(str2,x):
    for universidade in dados_json:
        if universidade["alpha_two_code"] == str2:
            x = x + 1
            dicionario_siglas[x] = {x:[universidade["name"],universidade["web_pages"]]}
    for itens in dicionario_siglas.values():
        print(itens) 
        
def pesquisa_dicionario(dic, id):
    if id in dic:
        nome_universidade, link = dic[id][id][0], dic[id][id][1]
        print(f"Nome da Universidade: {nome_universidade}")
        print(f"Link da Universidade: {link[0]}")
        abrir_link(link[0])
    else:
        print("Universidade não encontrada")

def abrir_link(x):
    try:
        webbrowser.open(x)
    except Exception:
        print("Não foi possivel acessar o Site")

    

def escolha1(x):
    
        match x :
            case 1:
                adicionar_lista_nomes()
                busca = str(input("Digite o nome do país: "))
                if busca not in lista_nomes:
                    print("Digite um nome valido para a pesquisa")
                adicionar_dicionario1(busca, 0)
                id = int(input("Digite o Número da Universidade que deseja ver: "))  
                pesquisa_dicionario(dicionario_nomes,id) 
            case 2:
                adicionar_lista_siglas()
                aux = str(input("Digite a sigla do país: "))
                busca = aux.upper()
                if busca not in lista_siglas:
                    print("Digite uma sigla valida para a pesquisa: ")
                else:
                    adicionar_dicionario2(busca, 0)
                    id = int(input("Digite o Número da Universidade que deseja ver: "))  
                    pesquisa_dicionario(dicionario_siglas,id) 
             
                

def escolha2(str2):
    for universidade in dados_json:
        nome_universidade = universidade["name"]
        if re.search(re.escape(str2), nome_universidade, re.IGNORECASE):
            print ("Nome: ", nome_universidade)
            print ("País: ", universidade["country"])
            print ("Sigla do País: ", universidade["alpha_two_code"])
            web_pages = ", ".join(universidade["web_pages"])
            print("Sites da Universidade:", web_pages)
        else:
            print ("Universidade não encontrada tente outra vez")
                
def escolha3(str3):
    for universidade in dados_json:
        for url in universidade["web_pages"]:
            if re.search(re.escape(str3), url, re.IGNORECASE):
                abrir_link(url)
                return
    print("Universidade não encontrada")


                
    