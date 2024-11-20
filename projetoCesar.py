Arquivo_treino = "Treinos.txt"

def inicializar () :
    pergunta = menu()
    match (pergunta) :
            case "1" :
                adicionar()
            case "2" :
                visualizar()
    
