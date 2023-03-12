import random as rd
tentativas =3
aleatorio =rd.randint(1, 50)
print("\nBem vindo ao jogo de adivinhação\n")

while tentativas>0:
    print("tentativas: ", tentativas)
    chute = input("Digite um número de 1 até 50 ")
    if chute.isnumeric():
        chute = int(chute)
    
        if chute ==aleatorio:
            print("parabéns, você acertou!")
            break
        elif chute >aleatorio:
            print("é maior que o numero secreto " )
        elif chute<aleatorio:
            print("é menor que o número secreto" )
        tentativas -=1
    else:
        print("por favor, digite um numero")
