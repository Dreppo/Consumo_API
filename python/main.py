import funções

def menu():
    print("Bem vindo a busca por universidades pelo mundo")
    opc = 0
    while opc != 4:
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
                opc = 0
                while opc != 3:
                    print("1 - Procurar Pelo Pais")
                    print("2 - Procurar Pela sigla do Pais Ex: BR(Brazil)")
                    print("3 - Voltar")     
                    escolha = int(input("digite um número para fazer uma ação: "))
                    opc = escolha
                    funções.escolha1(opc)
            case 2:
                busca = str(input("Digite o nome da Universidade: "))
                funções.escolha2(busca)
            case 3:
                busca1 = str(input("Digite o link para o site da Universidade: "))
                funções.escolha3(busca1)

    

menu()
