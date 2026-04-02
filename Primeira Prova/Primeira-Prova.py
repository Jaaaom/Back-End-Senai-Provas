#========================================================================================================================================
#                   1ª Prova - Programador Back End: João Marcos de Siqueira da Costa
#========================================================================================================================================
import random

if __name__ == "__main__":
    numeroAleatorio = random.randint(1,100)

    for i in range(15):
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
    
    if i+1 == 15:
        print(" Você esgotou todas as tentativas")
    else:
        print("Foram necessárias ",i+1,"tentativas")