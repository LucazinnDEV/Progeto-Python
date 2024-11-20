import os

Arquivo_treino = 'Treino.txt'

def menu ():
    limpaMenu()
    print ("==== Bem vindo ao menu! ====")
    print ("1 - Adicionar treino.") #feito
    print ("2 - Visualisar treinos.") #feito
    print ("3 - Atualizar treinos.") #feito
    print ("4 - Filtrar treino.") #feito
    print ("5 - Excluir treinos.") #faltando
    print ("6 - Definir metas.") #faltando
    print ("7 - Sujestões de treinos.") #faltando
    print ("8 - Sair.") #faltando
    
    return input("Escolha uma opção: ")

def limpaMenu () :
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar () :
    data = input ("Digite a data do treino (dd/mm/aa) : ")
    distancia = input ("Digite a distãncia em quilômetros : ")
    tempo = input ("Digite o tempo em minutos : ")
    local = input ("Digite o local do treino :" )
    condicoes = input ("Informe as condições climaticas da data do treino: ")
    treino = f"Data: {data}, Distância: {distancia} 2km, Tempo: {tempo} min, Local: {local}, Condições: {condicoes}\n"

    print(treino)

    with open(Arquivo_treino, "a") as file:
        file.write(treino)

    print ("Treino adicionado! ")

def visualizar () :
    print ("==== Treinos ====")
    try:
        with open(Arquivo_treino, "r") as file:
            for linha in file:
                data, distancia, tempo, local, condicoes = linha.strip().split(',')
                print(f"{data}, {distancia} km, {tempo}, {local}, {condicoes}")
    except FileNotFoundError:
        print("Nenhum treino cadastrado ainda.")