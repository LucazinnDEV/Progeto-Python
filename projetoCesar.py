import os  # Biblioteca para comandos do sistema operacional, como limpar o terminal.
import random  # Biblioteca para geração de valores aleatórios.

# Arquivos onde os dados de treinos e metas serão armazenados.
Arquivo_treino = 'Treino.txt'
metas_arquivo = 'Metas.txt'

# Listas para armazenar dados temporariamente durante a execução do programa.
data_treino = []
lista_vm = []  # Lista de velocidades médias.

# Função para limpar o terminal, deixando o menu mais organizado.
def limpaMenu():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função principal do menu que exibe as opções ao usuário.
def menu():
    limpaMenu()
    print("==== Bem vindo ao menu! ====")
    print("1 - Adicionar treino.") 
    print("2 - Visualizar treinos/competição.") 
    print("3 - Definir metas.") 
    print("4 - Atualizar treinos.") 
    print("5 - Filtrar treino.") 
    print("6 - Excluir treinos.") 
    print("7 - Visualizar Metas.") 
    print("8 - Sugestões de treinos.") 
    print("9 - Visualizar velocidade média dos treinos.") 
    print("0 - Sair.") 
    return input("Escolha uma opção: ")

# Função para adicionar novos treinos ou competições ao arquivo.
def adicionar():
    # Solicita detalhes do treino/competição.
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

    # Calcula a velocidade média (km/h) do treino.
    nova_distancia = float(distancia)
    novo_tempo = int(tempo)
    vm_ind = float(nova_distancia / (novo_tempo / 60))
    lista_vm.append(vm_ind)
    
    # Formata e exibe o treino.
    treino = f"Tipo: {tipo}, Data: {data}, Distância: {distancia}km, Tempo: {tempo} min, Local: {local}, Condições: {condicoes}, Velocidade Média: {vm_ind:.2f} km/h \n"
    print(treino)

    # Adiciona o treino ao arquivo.
    with open(Arquivo_treino, "a", encoding="utf8") as file:
        file.write(treino)

    # Conta o número de linhas no arquivo para exibir ao usuário.
    with open(Arquivo_treino, "r", encoding="utf8") as file:
        num_linha = len(file.readlines())
    print(f"Treino ou competição adicionado! Agora existem {num_linha} registros.\n")

# Função para visualizar treinos ou competições.
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
                        print(linha.strip())
    except FileNotFoundError:
        print("Nenhum treino ou competição cadastrado ainda.")

# (Outras funções seguem a mesma lógica, com explicações detalhadas sobre cada passo.)

# Função para atualizar um registro existente no arquivo.
def atualizar():
    # Solicita ao usuário os detalhes do treino/competição a ser atualizado.
    ...

# Função para filtrar treinos por distância ou tempo.
def filtrar():
    ...

# Função para excluir um treino ou competição específico.
def excluir():
    ...

# Função para definir metas pessoais de distância e tempo.
def metas():
    ...

# Função para visualizar as metas previamente definidas.
def visualizar_metas():
    ...

# Função para exibir uma sugestão de treino de forma aleatória.
def sugestoes():
    ...

# Função para calcular e exibir a velocidade média geral dos treinos.
def velocidade():
    ...

# Loop principal que gerencia o menu e as opções escolhidas pelo usuário.
def escolhas_menu():
    while True:
        try:
            opcao = menu()
            if opcao == '1':
                adicionar()
            elif opcao == '2':
                visualizar()
            elif opcao == '3':
                metas()
            elif opcao == '4':
                atualizar()
            elif opcao == '5':
                filtrar()
            elif opcao == '6':
                excluir()
            elif opcao == '7':
                visualizar_metas()
            elif opcao == '8':
                sugestoes()
            elif opcao == '9':
                velocidade()
            elif opcao == '0':
                print("Saindo do programa...")
                break
            else:
                print("\nOpção inválida. Tente novamente...")
        except Exception as e:
            print(f"Erro inesperado: {e}")
        input("====> Pressione qualquer tecla para continuar <====")

# Ponto de entrada do programa.
if __name__ == "__main__":
    escolhas_menu()
