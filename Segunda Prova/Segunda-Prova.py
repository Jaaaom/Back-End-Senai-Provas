#========================================================================================================================================
#                       Programador Back End - Segunda Prova: João Marcos de Siqueira da Costa
#========================================================================================================================================

import sqlite3

def conectar():
    return sqlite3.connect("Loja-Segunda-Prova.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Produtos(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT NOT NULL,
            Quantidade INTEGER,
            Preco DECIMAL
        );
""")
    
    conn.commit()
    conn.close()

def inserir_produtos(nome,quantidade,preco):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Produtos(Nome,Quantidade,Preco) VALUES (?,?,?)
    """,(nome,quantidade,preco))

    conn.commit()
    conn.close()

def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()

    opcao = int(input(" Como deseja listar seus produtos ? 1 - ID, 2 - Nome , 3 - Preço , 4 - Quantidade: "))

    match opcao:
        case 1:
            cursor.execute("""
                SELECT * FROM Produtos ORDER BY ID
            """)
        case 2:
            cursor.execute("""
                SELECT * FROM Produtos ORDER BY Nome
            """)
        case 3:
            cursor.execute("""
                SELECT * FROM Produtos ORDER BY Preco
            """)
        case 4:
            cursor.execute("""
                SELECT * FROM Produtos ORDER BY Quantidade
            """)        
        case _:
            print("Opção Inválida !!!!!!!!!")

    produtos = cursor.fetchall()

    conn.commit()
    conn.close()

    for produto in produtos:
        print(f"ID: {produto[0]} | Nome: {produto[1]} | Quantidade: {produto[2]} | Preço: R${produto[3]}")

    

def atualizar_produtos(id_produto,nome=None, quantidade=None,preco=None):
    conn = conectar()
    cursor = conn.cursor()

    if id_produto != None:
        if nome != None:
            cursor.execute("""
                UPDATE Produtos SET Nome = ? WHERE ID == ?
            """,(nome,id_produto))
        if quantidade != None:
            cursor.execute("""
                UPDATE Produtos SET Quantidade= ? WHERE ID == ?
            """,(quantidade,id_produto))
        if preco != None:
            cursor.execute("""
                UPDATE Produtos SET Preco = ? WHERE ID == ?
            """,(preco,id_produto))
        conn.commit()
        conn.close()
        return True

    conn.close()
    return False
    

def deletar_produtos(id_produto):
    conn = conectar()
    cursor = conn.cursor()

    if( id_produto !=None):
        cursor.execute(f"""
            DELETE FROM Produtos WHERE ID == {id_produto}
        """)
        conn.commit()
        conn.close()
        return True

    conn.close()
    return False

def buscar_produtos(id_produto,nome=None):
    conn = conectar()
    cursor = conn.cursor()
    if id_produto != None:
        cursor.execute(f"""
                SELECT * FROM Produtos WHERE ID == {id_produto}
        """)
        produtos = cursor.fetchall()

        conn.commit()
        conn.close()

        for produto in produtos:
            print(f"ID: {produto[0]} | Nome: {produto[1]} | Quantidade: {produto[2]} | Preço: R${produto[3]}")
    elif nome!=None:
        cursor.execute(f"""
                SELECT * FROM Produtos WHERE Nome == '{nome}'
            """)
        produtos = cursor.fetchall()

        conn.commit()
        conn.close()

        for produto in produtos:
            print(f"ID: {produto[0]} | Nome: {produto[1]} | Quantidade: {produto[2]} | Preço: R${produto[3]}")

    conn.close()
    return False


def main():

    criar_tabela()

    condicao = 1

    while condicao==1:
        print("====================================================================================================================")
        opcao = int(input(" 1 - Inserir Produtos \n 2 - Listar Produtos \n 3 - Atualizar Produtos \n 4 - Deletar Produto \n 5 - Buscar Produto \n 0 - sair : "))
        match opcao:
            case 1:
                print("Cadastrando Produtos ---------------------------------")
                nome = input("Nome: ")
                j=0
                while j==0:
                    quantidade = int(input("Quantidade: "))

                    if quantidade <0:
                        print("Quantidade inválida")
                    else:
                        j=1
                
                j=0
                while j==0:
                    preco = float(input("Preço: "))

                    if preco <=0:
                        print("Preço Inválido")
                    else:
                        j=1
                
                inserir_produtos(nome,quantidade,preco)


            case 2:
                print("Listagem dos Produtos")
                listar_produtos()

            case 3:
                print("Atualizando Dados dos Produtos")
                identidade = int(input("ID do Produto: "))
                buscar_produtos(identidade)

                opcao2 = int(input(" Quer Atualizar: 1 - Nome, 2 - Quantidade , 3 - Preço: "))

                match opcao2:
                    case 1:
                        nome = input("Nome: ")
                        if atualizar_produtos(identidade,nome):
                            print("Deu Certo - Dado Atualizado")
                            buscar_produtos(identidade)
                        else:
                            print("Deu Ruim")

                    case 2:
                        j=0
                        while j==0:
                            quantidade = int(input("Quantidade Atualizada: "))

                            if quantidade <0:
                                print("Quantidade Inválida")
                            else:
                                j=1


                        if atualizar_produtos(identidade,None ,quantidade):
                            print("Deu Certo - Dado Atualizado")
                            buscar_produtos(identidade)
                        else:
                            print("Deu Ruim")

                    case 3:
                        j=0
                        while j==0:
                            preco = float(input("Preço Atualizado: "))

                            if preco <=0:
                                print("Quantidade Inválida")
                            else:
                                j=1


                        if atualizar_produtos(identidade,None, None, preco):
                            print("Deu Certo - Dado Atualizado")
                            buscar_produtos(identidade)
                        else:
                            print("Deu Ruim")
                    
                    case _:
                        print("Opção Inválida!!!!")
                    

            case 4:
                identidade = int(input("Qual produto quer deletar\nID:"))
                if deletar_produtos(identidade):
                    print("Excluído")
                else:
                    print("Não excluído")

            case 5:
                opcao3 = int(input("Deseja buscar o produto por ? 1 -ID , 2 - Nome: "))

                if opcao3 == 1:
                    identidade = int(input("ID: "))
                    buscar_produtos(identidade)
                if opcao3 ==2:
                    nome = input("Nome do Produto: ")
                    buscar_produtos(None, nome)

            case 0:
                print("FIM!!!!!!")
                condicao = 0

            case _:
                print("Opção Inválida!!!!!!!!!")

if __name__ == "__main__":
   main()