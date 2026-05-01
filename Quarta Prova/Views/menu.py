from Controllers.guilda_controller import (
    inicializar, registrar_heroi, remover_heroi, listar_herois, buscar_heroi
)

from Controllers.missao_controller import(
    inicializar, criar_missao, concluir_missao, listar_missao
)

def menu():

    condicao = 1

    while condicao==1:
        print("====================================================================================================================")
        opcao = int(input("[1] Registrar Heroi  - [2] Listar Herois  - [3] Criar Missão - [4] Concluir Missão - [0] Sair: "))
        match opcao:
            case 1:
                nome = input("Nome: ")
                classe = input("Classe: ")
                registrar_heroi(nome, classe,1,0)
                

            case 2:
                herois = listar_herois()
                for h in herois:
                    print("\n" + h.resumo())
                    #for m in h.missoes:
                    #    print("\n ", m.resumo())
                    
                    

            case 3:
                titulo = input("Título: ")
                descricao = input("Descrição: ")
                xp = int(input("XP recompensa: "))
                heroi_id = int(input("ID do herói: "))
                criar_missao(titulo, descricao, xp, heroi_id)
                    

            case 4:
                missoes = listar_missao()
                for m in missoes:
                    print("\n ", m.resumo())
                missao_id = int(input("ID da missão: "))
                concluir_missao(missao_id)

            case 0:
                print("FIM!!!!!!")
                condicao = 0

            case _:
                print("Opção Inválida!!!!!!!!!")