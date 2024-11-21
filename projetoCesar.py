import os
import random   

Arquivo_treino = 'Treino.txt'

data_treino = []
lista_vm = []

def limpaMenu () :
    os.system('cls' if os.name == 'nt' else 'clear')


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
    print ("9 - Visualizar velocidade média dos treinos.") #feito
    
    return input("Escolha uma opção: ")

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
                        print(f"Data: {data}, Distância: {distancia} km, Tempo: {tempo}, Local: {local}, Condições: {condicoes}, Velocidade Média: {vm_ind} ")
                    except ValueError:
                        print("Erro no formato dos dados de um treino. Verifique o arquivo.")
    except FileNotFoundError:
        print("Nenhum treino cadastrado ainda.")

def atualizar():
    dataTreino = input("Digite a data do treino que deseja modificar (dd/mm/aa): ").strip()
    
    try:

        with open(Arquivo_treino, "r", encoding="utf8") as file:
            treinos = file.readlines()

        treino_encontrado = False
        for i, treino in enumerate(treinos):
            if dataTreino in treino:
                treino_encontrado = True
                print(f"\nTreino encontrado: {treino.strip()}")
             
                nova_distancia = input("Digite a nova distância (ou pressione Enter para manter): ").strip()
                novo_tempo = input("Digite o novo tempo em minutos (ou pressione Enter para manter): ").strip()
                novo_local = input("Digite o novo local (ou pressione Enter para manter): ").strip()
                novas_condicoes = input("Digite as novas condições climáticas (ou pressione Enter para manter): ").strip()

                campos = treino.strip().split(", ")
                campos_dict = {campo.split(":")[0].strip(): campo.split(":")[1].strip() for campo in campos}

                campos_dict["Distância"] = nova_distancia if nova_distancia else campos_dict["Distância"]
                campos_dict["Tempo"] = novo_tempo if novo_tempo else campos_dict["Tempo"]
                campos_dict["Local"] = novo_local if novo_local else campos_dict["Local"]
                campos_dict["Condições"] = novas_condicoes if novas_condicoes else campos_dict["Condições"]

                nova_vm = float(campos_dict["Distância"]) / (float(campos_dict["Tempo"]) / 60)
                campos_dict["Velocidade Média"] = f"{nova_vm:.2f} km/h"

                treinos[i] = ", ".join([f"{chave}: {valor}" for chave, valor in campos_dict.items()]) + "\n"
                print("\nTreino atualizado com sucesso!")
                break

        if not treino_encontrado:
            print("Treino com a data fornecida não encontrado.")

        with open(Arquivo_treino, "w", encoding="utf8") as file:
            file.writelines(treinos)

    except FileNotFoundError:
        print("Arquivo de treino não encontrado.")
    except ValueError:
        print("Erro ao processar os dados. Verifique os valores inseridos.")

def filtrar():
    print("\n==== Filtrar Treinos ====")
    escolha = input("Deseja filtrar por (1) Distância ou (2) Tempo? Digite o número correspondente: ")

    try:
        filtro = float(input("Digite o valor do filtro (em km ou minutos): "))

        with open(Arquivo_treino, "r", encoding="utf8") as file:
            treinos = file.readlines()

        if not treinos:
            print("Nenhum treino registrado para filtrar.")
            return

        print("\nTreinos filtrados:")
        encontrou = False

        for linha in treinos:
            try:
                # Dividir os dados do treino
                dados = linha.strip().split(", ")
                distancia = float(dados[1].split(": ")[1].replace("km", "").strip())
                tempo = int(dados[2].split(": ")[1].replace("min", "").strip())

                if escolha == "1" and distancia >= filtro:
                    print(linha.strip())
                    encontrou = True
                elif escolha == "2" and tempo <= filtro:
                    print(linha.strip())
                    encontrou = True
            except (IndexError, ValueError):
                print("Erro ao processar os dados do treino. Verifique o formato do arquivo.")
        
        if not encontrou:
            print("Nenhum treino encontrado com os critérios fornecidos.")
    except ValueError:
        print("Por favor, insira um valor numérico válido para o filtro.")


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

def velocidade():
    try:
        with open(Arquivo_treino, "r", encoding="utf8") as file:
            linhas = file.readlines()

        velocidades = []
        for linha in linhas:
            if "Tipo: treino" in linha:
                try:
                    velocidade = float(linha.split("Velocidade Média: ")[1].replace(" km/h", "").strip())
                    velocidades.append(velocidade)
                except (IndexError, ValueError):
                    print(f"Erro ao processar a linha: {linha.strip()}. Ignorando.")
        
        if not velocidades:
            print("\nNenhuma Velocidade Média registrada para treinos.")
            return

        media_geral = sum(velocidades) / len(velocidades)
        print(f"\nVelocidade média geral dos treinos: {media_geral:.2f} km/h\n")
    except FileNotFoundError:
        print("\nArquivo de treinos e competições não encontrado.")
    except Exception as e:
        print(f"\nErro inesperado: {e}")

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
