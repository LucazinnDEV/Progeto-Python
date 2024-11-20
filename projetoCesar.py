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

