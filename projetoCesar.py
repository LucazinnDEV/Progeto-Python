import os

Arquivo_treino = 'Treino.txt'

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
    print ("8 - Sair.") #faltando
    
    return input("Escolha uma opção: ")