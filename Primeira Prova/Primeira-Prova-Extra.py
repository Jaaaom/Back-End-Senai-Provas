#========================================================================================================================================
#                   1ª Prova - Programador Back End: João Marcos de Siqueira da Costa
#========================================================================================================================================
import random

def jogo(modo):
    numeroAleatorio = random.randint(1,100)

    for i in range(modo):
        print("Tentativa nº:",i+1)
        tentativa = int(input("Digite um número entre 1 e 100: "))
        
        if tentativa == numeroAleatorio:
            print("Parabéns você acertou o número gerado pelo programa!!!")
            print("Numero gerado:", numeroAleatorio )
            break
        elif tentativa < numeroAleatorio:
            print(" Seu número é menor que o número gerado! ")
            print("Numero gerado:", numeroAleatorio )
        else:
            print(" Seu número é maior que o número gerado! ")
            print("Numero gerado:", numeroAleatorio )
    
    return i+1

def pontuacao(modo, sucesso_nas_tentativas):

    if modo.upper() == 'F':
        return 100/sucesso_nas_tentativas
    elif modo.upper() == 'M':
        return 150/sucesso_nas_tentativas
    elif modo.upper() == 'D':
        return 250/sucesso_nas_tentativas
    elif modo.upper() == 'E':
        return 400/sucesso_nas_tentativas
    if modo.upper() == 'MS':
        return 1000/sucesso_nas_tentativas
    



def main():

    contador = 0

    # Escolha do modo de dificuldade
    while contador == 0:
        modo = input(" Escolha um modo: F - Fácil , M - Médio , D - Difícil , E - Expert , MS - Morte Súbita:  ")

        if modo.upper() != 'F' or modo.upper() != 'M' or modo.upper() != 'D' or modo.upper() != 'E' or modo.upper() != 'MS':
            contador = 1
        else:
            print("Dificuldade Inválida!!! ")


    # Jogando 

    contador2 = 0
    pontuacao_max = []
    while contador2 == 0:


        match modo.upper():
            case 'F':
                print("Você escolheu o modo fácil! Terá direito a 20 tentativas")
                quantidade_tentativas = jogo(20)
                if quantidade_tentativas == 20:
                    print(" Você esgotou todas as tentativas")
                    pontuacao_max.append(0)
                else:
                    print("Foram necessárias ",quantidade_tentativas,"tentativas")
                    pontuacao_max.append(pontuacao(modo.upper(), quantidade_tentativas))
            case 'M':
                print("Você escolheu o modo médio! Terá direito a 14 tentativas")
                quantidade_tentativas = jogo(14)
                if quantidade_tentativas == 14:
                    print(" Você esgotou todas as tentativas")
                    pontuacao_max.append(0)
                else:
                    print("Foram necessárias ",quantidade_tentativas,"tentativas")
                    pontuacao_max.append(pontuacao(modo.upper(), quantidade_tentativas))
            case 'D':
                print("Você escolheu o modo difícil! Terá direito a 10 tentativas")
                quantidade_tentativas = jogo(10)
                if quantidade_tentativas == 10:
                    print(" Você esgotou todas as tentativas")
                    pontuacao_max.append(0)
                else:
                    print("Foram necessárias ",quantidade_tentativas,"tentativas")
                    pontuacao_max.append(pontuacao(modo.upper(), quantidade_tentativas))
            case 'E':
                print("Você escolheu o modo expert! Terá direito a 5 tentativas")
                quantidade_tentativas = jogo(5)
                if quantidade_tentativas == 5:
                    print(" Você esgotou todas as tentativas")
                    pontuacao_max.append(0)
                else:
                    print("Foram necessárias ",quantidade_tentativas,"tentativas")
                    pontuacao_max.append(pontuacao(modo.upper(), quantidade_tentativas))
            case 'MS':
                print("Você escolheu o modo morte súbita! Terá direito a 1 tentativa")
                quantidade_tentativas = jogo(1)
                if quantidade_tentativas == 1:
                    print(" Você Falhou")
                    pontuacao_max.append(0)
                else:
                    print(" Você não é um mero mortal. Jogue agora na mega sena e fique milionário")
                    pontuacao_max.append(pontuacao(modo.upper(), quantidade_tentativas))
        
        repeticao = input("Deseja jogar novamente: Sim(S)/Não(N) ?")

        if repeticao.upper() == 'S':
            contador = 0

            # Escolha do modo de dificuldade
            while contador == 0:
                modo = input(" Escolha um modo: F - Fácil , M - Médio , D - Difícil , E - Expert , MS - Morte Súbita:  ")

                if modo.upper() != 'F' or modo.upper() != 'M' or modo.upper() != 'D' or modo.upper() != 'E' or modo.upper() != 'MS':
                    contador = 1
                else:
                    print("Dificuldade Inválida!!! ")
            continue
            
        else:
            contador2 = 1

    print("Pontuação Final: ", sum(pontuacao_max), "pontos")
            
            

if __name__ == "__main__":
    main()