import os
import random   

Arquivo_treino = 'Treino.txt'

data_treino = []
lista_vm = []

def menu () :
    limpaMenu()
    print ("==== Bem vindo ao menu! ====")
    print ("1 - Adicionar treino.") #feito
    print ("2 - Visualisar treinos.") #feito
    print ("3 - Atualizar treinos.") #feito
    print ("4 - Filtrar treino.") #feito
    print ("5 - Excluir treinos.") #faltando
    print ("6 - Definir metas.") #faltando
    print ("7 - Sujestões de treinos.") #faltando
    print ("8 - Sair.") #feito
    print ("9 - Visualizar velocidade média.") #feito
    
    return input("Escolha uma opção: ")

def limpaMenu () :
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar () :
    data = input ("Digite a data do treino (dd/mm/aa) : ")
    data_treino.append(data)
    distancia = input ("Digite a distãncia em quilômetros : ")
    tempo = input ("Digite o tempo em minutos : ")
    local = input ("Digite o local do treino : ")
    condicoes = input ("Informe as condições climaticas da data do treino: ")
    nova_distancia = float(distancia)
    novo_tempo = int(tempo)
    vm_ind = float(nova_distancia/(novo_tempo/60))
    lista_vm.append(vm_ind)
    
    treino = f"Data: {data}, Distância: {distancia}km, Tempo: {tempo} min, Local: {local}, Condições: {condicoes}, Velocidade Média: {vm_ind:.2f} km/h \n"
    print(treino)

    with open(Arquivo_treino, "a" ,encoding = "utf8") as file:
        file.write(treino)

    with open(Arquivo_treino, "r", encoding="utf8") as file:
        num_linha = len(file.readlines())

    print(f"Treino adicionado! Agora existem {num_linha} treinos registrados.\n")

def visualizar () :
    print ("==== Treinos ====")
    try:
        with open(Arquivo_treino, "r" ,encoding = "utf8") as file:
            linhas = file.readlines()
            if not linhas:  
                print("Nenhum treino cadastrado ainda.")
            else:
              for linha in linhas:
                    try:
                        data, distancia, tempo, local, condicoes, vm_ind = linha.strip().split(',')
                        print(f"Data: {data}, Distância: {distancia} km, Tempo: {tempo}, Local: {local}, Condições: {condicoes}, Velocidade Média: {vm_ind} km/h ")
                    except ValueError:
                        print("Erro no formato dos dados de um treino. Verifique o arquivo.")
    except FileNotFoundError:
        print("Nenhum treino cadastrado ainda.")

def atualizar () :
    dataTreino = input ("Digite a data do treino que deseja modificar (dd/mm/aa): ")
    try :
        with open(Arquivo_treino, "r" ,encoding = "utf8") as file:
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

    with open(Arquivo_treino, "r" ,encoding = "utf8") as file:
        for t in Arquivo_treino :
            data, distancia, tempo, local, condicoes = Arquivo_treino.sptrip().split(',')
            distancia = float (distancia)
            tempoH, tempoM, = map(int, tempo.split(":"))
            tempoT = tempoH * 60 + tempoM

            if escolha == "1" and distancia >= escolha2 :
                print (f"Data: {data}, Distância: {distancia}, Tempo: {tempoH}:{tempoM}, Local: {local}, Condições: {condicoes}")
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

def sugestoes () :
    
    treinos_principais = [
        "Intervalados: 1 minuto rápido + 2 minutos leve (repetir 6 vezes)",
        "Corrida contínua: Ritmo moderado por 20 minutos",
        "Tiros: 400 metros forte x 8, descanso de 2 minuto entre séries",
        "Corrida longa: 5 km em ritmo confortável",
        "Progressivo: Comece lento e aumente o ritmo a cada quilômetro até terminar rápido"
    ]
    print(random.choice(treinos_principais))

def velocidade () :
    if not lista_vm: 
        print("\nNenhuma velocidade média registrada ainda.")
        return
    
    media_geral = sum(lista_vm) / len(lista_vm)
    print(f"Velocidade média geral: {media_geral:.2f} km/h\n")
    

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
            elif opcao == '9':
                velocidade()    
            elif opcao == '8' :
                print("Saindo do programa...")
                os.system("exit")
                break
            else: 
                print("\nOpção inválida. Tente novamente...")
            
        except ValueError :
            print ("Opção inexistente.")
            print ("Digite de 1 à 8 para acessar as opções.")      
        input("====> Pressione qualquer tecla para continuar <====")
    
if __name__ == "__main__":
    escolhas_menu()