import os
import random   

Arquivo_treino = 'Treino.txt'
metas_arquivo = 'Metas.txt'

data_treino = []
lista_vm = []

def limpaMenu () :
    os.system('cls' if os.name == 'nt' else 'clear')

def menu () :
    limpaMenu()
    print ("==== Bem vindo ao menu! ====")
    print ("1 - Adicionar treino.") 
    print ("2 - Visualizar treinos/competição.") 
    print ("3 - Definir metas.") 
    print ("4 - Atualizar treinos.") 
    print ("5 - Filtrar treino.") 
    print ("6 - Excluir treinos.") 
    print ("7 - Visualizar Metas.") 
    print ("8 - Sugestões de treinos.") 
    print ("9 - Visualizar velocidade média dos treinos.") 
    print ("0 - Sair.") 
    
    return input("Escolha uma opção: ")

def adicionar():
    tipo = input("Digite o tipo (treino ou competição): ").strip().lower()
    while tipo not in ["treino", "competição"]:
        print("Opção inválida! Por favor, escolha 'treino' ou 'competição'.")
        tipo = input("Digite o tipo (treino ou competição): ").strip().lower()

    data = input("Digite a data do treino ou competição (dd/mm/aa): ")
    data_treino.append(data)
    distancia = input("Digite a distância em quilômetros: ")
    tempo = input("Digite o tempo em minutos: ")
    local = input("Digite o local do treino ou competição: ")
    condicoes = input("Informe as condições climáticas da data: ")
    nova_distancia = float(distancia)
    novo_tempo = int(tempo)
    vm_ind = float(nova_distancia/(novo_tempo/60))
    lista_vm.append(vm_ind)
    
    treino = f"Tipo: {tipo}, Data: {data}, Distância: {distancia}km, Tempo: {tempo} min, Local: {local}, Condições: {condicoes}, Velocidade Média: {vm_ind:.2f} km/h \n"
    print(treino)

    with open(Arquivo_treino, "a" ,encoding = "utf8") as file:
        file.write(treino)

    with open(Arquivo_treino, "r", encoding="utf8") as file:
        num_linha = len(file.readlines())

    print(f"Treino ou competição adicionado! Agora existem {num_linha} registros.\n")

def visualizar():
    tipo = input("Você deseja visualizar treino ou competição ").strip().lower()
    while tipo not in ["treino", "competição"]:
        print("Opção inválida! Por favor, escolha 'treino' ou 'competição'.")
        tipo = input("Você deseja visualizar treinos ou competições? ").strip().lower()

    print(f"==== {tipo.capitalize()} ====")
    try:
        with open(Arquivo_treino, "r", encoding="utf8") as file:
            linhas = file.readlines()
            if not linhas:
                print("Nenhum treino ou competição cadastrado ainda.")
            else:
                for linha in linhas:
                    if tipo in linha: 
                        try:
                            dados = linha.strip().split(', ')
                            print(", ".join(dados))
                        except ValueError:
                            print("Erro no formato dos dados de um treino ou competição. Verifique o arquivo.")
    except FileNotFoundError:
        print("Nenhum treino ou competição cadastrado ainda.")

def atualizar():
    tipo = input("Digite o tipo (treino ou competição) que deseja modificar: ").strip().lower()
    while tipo not in ["treino", "competição"]:
        print("Opção inválida! Por favor, escolha 'treino' ou 'competição'.")
        tipo = input("Digite o tipo (treino ou competição) que deseja modificar: ").strip().lower()

    dataTreino = input(f"Digite a data do {tipo} que deseja modificar (dd/mm/aa): ").strip()
    
    try:
        with open(Arquivo_treino, "r", encoding="utf8") as file:
            treinos = file.readlines()

        treino_encontrado = False
        for i, treino in enumerate(treinos):
            if dataTreino in treino and tipo in treino:
                treino_encontrado = True
                print(f"\n{tipo.capitalize()} encontrado: {treino.strip()}")
             
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
                print("\nRegistro atualizado com sucesso!")
                break

        if not treino_encontrado:
            print(f"{tipo.capitalize()} com a data fornecida não encontrado.")

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
            registros = file.readlines()

        if not registros:
            print("Nenhum treino ou competição registrado para filtrar.")
            return

        print("\nTreinos filtrados:")
        encontrou = False

        for linha in registros:
            try:
                if "treino" not in linha.lower():
                    continue
                
                dados = linha.strip().split(", ")
                tipo = dados[0].split(": ")[1]
                distancia = dados[2].split(": ")[1].replace("km", "").strip()
                tempo = dados[3].split(": ")[1].replace("min", "").strip()

                distancia = float(distancia)
                tempo = int(tempo)

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

def excluir():
    tipo = input("Você deseja excluir um treino ou uma competição? ").strip().lower()
    while tipo not in ["treino", "competição"]:
        print("Opção inválida! Por favor, escolha 'treino' ou 'competição'.")
        tipo = input("Você deseja excluir um treino ou uma competição? ").strip().lower()

    try:
        with open(Arquivo_treino, "r", encoding="utf8") as file:
            registros = file.readlines()
        
        if not registros:
            print('Nenhum treino ou competição encontrado!')
            return
        
        dataparaexcluir = input(f'Digite a data de {tipo} que deseja excluir (dd/mm/aa): ').strip()
        registros_atualizados = [registro for registro in registros if dataparaexcluir not in registro or tipo not in registro]

        if len(registros) == len(registros_atualizados):
            print(f'Nenhum {tipo} encontrado com a data: {dataparaexcluir}')
            return
        
        with open(Arquivo_treino, 'w', encoding='utf8') as file:
            file.writelines(registros_atualizados)
        
        print(f'{tipo.capitalize()} com a data: {dataparaexcluir} excluído com sucesso!')

    except FileNotFoundError:
        print('Arquivo de treino ou competição não encontrado.')
    except ValueError:
        print('Erro inesperado ao processar o arquivo.')

def metas():
    print("\n==== Definir Metas ====")
    
    try:
        meta_distancia = input("Digite a meta pessoal de distância em km: ").strip()
        while not meta_distancia.replace('.', '', 1).isdigit():
            print("Por favor, insira um valor numérico válido.")
            meta_distancia = input("Digite a meta pessoal de distância em km: ").strip()

        meta_tempo = input("Digite a meta pessoal de tempo em minutos: ").strip()
        while not meta_tempo.isdigit():
            print("Por favor, insira um valor numérico válido.")
            meta_tempo = input("Digite a meta pessoal de tempo em minutos: ").strip()

        metas_treinos = f"meta de distância: {meta_distancia} km meta de tempo: {meta_tempo} min"

        with open(metas_arquivo, "w", encoding="utf8") as file:
            file.write(metas_treinos)

        print("\n==== Metas definidas com sucesso! ====")
        print(f"- Meta de distância: {meta_distancia} km")
        print(f"- Meta de tempo: {meta_tempo} min")

    except Exception as e:
        print(f"Erro inesperado ao definir metas: {e}")

    input("\nPressione qualquer tecla para retornar ao menu...")

def visualizar_metas():
    print("\n==== Metas ====")
    try:
        with open(metas_arquivo, "r", encoding="utf8") as file:
            linhas = file.readlines()

        if not linhas:
            print("Nenhuma meta cadastrada ainda.")
            return

        for linha in linhas:
            try:
                if "Meta de distância" in linha and "meta de tempo" in linha:
                    partes = linha.split("meta de distância:")[1].split("meta de tempo:")
                    meta_distancia = partes[0].strip().replace("km", "").strip()
                    meta_tempo = partes[1].strip().replace("min", "").strip()

                    print(f"- Meta de distância: {meta_distancia} km")
                    print(f"- Meta de tempo: {meta_tempo} min\n")
                else:
                    print(f"Erro: Formato inesperado na linha: {linha.strip()}")
            except (IndexError, ValueError):
                print(f"Erro ao processar a linha: {linha.strip()}. Verifique o arquivo.")
    except FileNotFoundError:
        print("Arquivo de metas não encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

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
            elif opcao == '4' :
                atualizar()
            elif opcao == '5' :
                filtrar()
            elif opcao == '6' :
                excluir()
            elif opcao == '3' :
                metas()
            elif opcao == '8' :
                sugestoes()
            elif opcao == '9':
                velocidade()    
            elif opcao == '7' :
                visualizar_metas ()
            elif opcao == '0' :
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