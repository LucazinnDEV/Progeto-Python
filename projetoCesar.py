Arquivo_treino = "Treinos.txt"

def inicializar () :
    pergunta = menu()
    match (pergunta) :
            case "1" :
                adicionar()
            case "2" :
                visualizar()
    
def menu () :
    print ("==== Bem vindo ao menu! ====")
    print ("1 - Adicionar treino.")
    print ("2 - Visualisar treinos.")
    print ("3 - Atualizar treinos.")
    print ("4 - Filtrar treino.")
    print ("5 - Excluir treinos.")
    print ("6 - Definir metas.")
    print ("7 - Sujestões de treinos.")
    print ("8 - Sair.")
    return input("Escolha uma opção: ")

menu()

def adicionar () :
    data = input ("Digite a data do treino (dd/mm/aa) : ")
    distancia = input ("Digite a distãncia em metros : ")
    tempo = input ("Digite o tempo em minutos : ")
    local = input ("Digite o lcal do treino :" )
    condicoes = input ("Informe as condições climaticas da data do treino: ")
    treino = {"Data": data, "Distancia": distancia, "Tempo": tempo, "Local": local, "Condições": condicoes}

    print(treino)

    with open("C:\\Users\\lukin\\Desktop\\estudos\\AulasFacul\\Python\\projetoPython\\teste2.txt", "a") as file:
        file.write(f"{treino}\n")
    print ("Treino adicionado! ")

def visualizar () :
    print ("==== Treinos ====")
    try :
        with open(Arquivo_treino, "r") as file:
            for t in Arquivo_treino :
                print (f"Data :{t['data']}")
                print (f"Distância : {t['distancia']}")
                print (f"Tempo : {t['tempo']}")
                print (f"Local : {t['local']}")
                print (f"Condições : {t['condicoes']}")
    except FileNotFoundError () :
        print ("Nenhum treino foi adicionado ainda.")

def atualizar () :
    dataTreino = input ("Digite a data do treino que deseja modificar (dd/mm/aa): ")
    try :
        with open(Arquivo_treino, "r") as file:
            for treino in dataTreino :  
                if treino["data"] == dataTreino :
                    resposta = input("Digite S ou N se deseja modificar a Data: ").upper()
                    match (resposta) :
                        case "S" :
                            treino['data'] = input ("Digite a nova data (dd/mm/aa): ")
                        case "N" :
                            print ("Data não alterada")
                    resposta1 = input ("Digite S ou N se deseja modificar a distância ? ").upper()
                    match (resposta1) :
                        case "S" :
                            treino['distancia'] = input ("Digite a nova distância :")
                        case "N" :
                            print ("Distância não alterada")
                    resposta2 = input("Digite S ou N se deseja modificar o tempo : ").upper()
                    match (resposta2) :
                        case "S" :
                            treino["tempo"] = input ("Digite o novo tempo :")
                        case "N" :
                            print ("Tempo não alterado")
                    resposta3 = input ("Digite S ou N se dejesa modificar o local do treino : ").upper()
                    match (resposta3) :
                        case "S" :
                            treino["local"] = input ("Digite o novo local do treino :")
                        case "N" :
                            print ("Local não alterado.")
                    resposta4 = input("Digite S ou N se deseja modificar as condições climaticas do treino: ")
                    match (resposta4) :
                        case "S" :
                            treino["condicoes"] = input ("Digite as novas condições climaticas: ")
                        case "N" :
                            print ("Condições não alteradas")
    except FileNotFoundError():
        print("Arquivo não encontrado :")
    except ValueError(resposta2):
        print("Somente S ou N")