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

