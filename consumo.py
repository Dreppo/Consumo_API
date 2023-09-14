import json
import webbrowser

with open('Consumo_API\json\world_universities_and_domains.json', 'r', encoding='utf-8') as arquivo:
    dados_json = json.load(arquivo)

lista_nomes = []
lista_siglas = []
dic_exemplo1 = {}
dic_exemplo2 = {}

def verificacao_de_escolha(num1,num2,esco):
    if esco < num1:
        print("Digite um número valido")   
    elif esco > num2:
        print("Digite um número valido")

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
           
            dic_exemplo1["id"] = x
            dic_exemplo1["name"] = universidade["name"]
            dic_exemplo1["web_pages"] = universidade["web_pages"]
            print(dic_exemplo1)
            
def mostrar_dic(x):
    for universidade in dados_json:
        x = x + 1  
        dic_exemplo1["id"] = x
        dic_exemplo1["name"] = universidade["name"]
        dic_exemplo1["web_pages"] = universidade["web_pages"]
        print(dic_exemplo1)

def item_dic(id):
    for item in dic_exemplo1["id"]:
        if dic_exemplo1["id"] == id:
            print(dic_exemplo1[item])
            link =  dic_exemplo1["web_pages"]
            webbrowser.open(link)

              

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
                id = int(input("Digite o ID da Universidade que deseja ver: "))  
                item_dic(id) 
                print()
            case 2:
                lista_s()
                aux = str(input("Digite a sigla do país: "))
                busca = aux.upper()
                if busca not in lista_siglas:
                    print("Digite uma sigla valida para a pesquisa")
                

def escolha2():    
    busca = str(input("Digite o nome da Universidade"))
    busca         
                
                
        
        
    

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
                escolha2()
                
        print("")        


    




menu()
