# ===========================================================================================================================================
#                       Quarta Prova - Programador Back End - João Marcos de Siqueira da Costa
#============================================================================================================================================

from Controllers.guilda_controller import (
    inicializar, registrar_heroi, remover_heroi, listar_herois, buscar_heroi
)

from Controllers.missao_controller import(
    inicializar, criar_missao, concluir_missao
)

from Views.menu import menu

inicializar()

menu()


