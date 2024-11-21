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

def atualizar () :
    dataTreino = input ("Digite a data do treino que deseja modificar (dd/mm/aa): ")
    try :
        with open(Arquivo_treino, "r") as file:
            for treino in dataTreino :  
                if treino["data"] == dataTreino :
                    resposta = input("Digite S ou N caso queira modificar a Data: ").upper()
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

def filtrar () :
    escolha = input ("Deseja filtrar por por (1) Distância ou (2) Tempo ?/n:")
    escolha2 = float (input("Digite o valor do filtro/n : "))

    with open(Arquivo_treino, "r") as file:
        for t in Arquivo_treino :
            data, distancia, tempo, local, condicoes = Arquivo_treino.sptrip().split(',')
            distancia = float (distancia)
            tempoH, tempoM, = map(int, tempo.split(":"))
            tempoT = tempoH * 60 + tempoM

            if escolha == "1" and distancia >= escolha2 :
                print (f"Data: {data}, Distância 2: {distancia}, Tempo: {tempoH}:{tempoM}, Local: {local}, Condições: {condicoes}")
            elif escolha2 == "2" and tempoT <= escolha2 :
                print (f"Data: {data}, Distância: {distancia}, Tempo: {tempoH}:{tempoM}, Local: {local}, Condições: {condicoes}")

def excluir () :
    try:
        with open(Arquivo_treino, "r" ,encoding = "utf8") as file:
            treinos = file.readlines()
        if not treinos:
            print('Nenhum treino encontrado!')
            return

        dataparaexcluir = input('Digite uma data de treino que deseja excluir (dd/mm/aa):  ').strip()
        treinos_atualizados = [treino for treino in treinos if dataparaexcluir not in treino]

        if len (treinos) == len(treinos_atualizados):
            print(f'Nenhum treino encontrado com a data: {dataparaexcluir}')
            return

        with open(Arquivo_treino, 'w', encoding='utf8') as file:
            file.writelines(treinos_atualizados)

        print(f'Treino com a data: {dataparaexcluir} excluído com sucesso!')

    except FileNotFoundError:
        print('Arquivo de treino não encontrado.')
    except ValueError:
        print('Erro inesperado ao processar o arquivo.')

def metas () :
    print("==== Definir Metas ====")
    
    meta_distancia = input("Digite para definir a meta pessoal de distância em km: ")
    meta_tempo = input("Digite para definir a meta pessoal de tempo em minutos : ")

    metas_treinos = f"meta de distância : {meta_distancia} km meta de tempo {meta_tempo} min"

    metas_arquivo = 'Metas.txt'

    with open (metas_arquivo , "w" ,encoding = "utf8") as file :
        file.write(metas_treinos)

    print("\n==== Metas semanais definidas com sucesso ! ====")
    print(metas_treinos)

    input("\nPressione qualquer tecla para retornar ao menu...")

def escolhas_menu () :
    while True:
        try: 
            opcao = menu()
            if opcao == '1' :
                adicionar()
            elif opcao == '2' :
                visualizar()
            elif opcao == '3' :
                atualizar()
            elif opcao == '4' :
                filtrar()
            elif opcao == '5' :
                excluir()
            elif opcao == '6' :
                metas()
            elif opcao == '7' :
                sugestoes()
            elif opcao == '8' :
                print("Saindo do programa...")
                break
        except ValueError :
            print ("Opção inexistente.")
            print ("Digite de 1 à 8 para acessar as opções.")      
        input("Pressione qualquer tecla para continuar")

if __name__ == "__main__":
    escolhas_menu()