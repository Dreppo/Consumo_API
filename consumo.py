import json
import webbrowser

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
                    mostrar_escolha(id,dic_exemplo2) 
             
                

def escolha2(str2):
    for universidade in dados_json:
        if universidade["name"] == str2:
                print (universidade["name"])
                print (universidade["country"])
                print (universidade["alpha_two_code"])
        else:
            print("Universidade não encontrada")
            break

        
             
                
                
        
        
    

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
        match opc :
            case 1:
                escolha1()
            case 2:
                busca = str(input("Digite o nome da Universidade: "))
                escolha2(busca)
                
        print("")        


    




menu()
